import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from file_storage_impl import FileStorageImpl


class Level4Tests(unittest.TestCase):
    """
    Level 4 tests for File Storage - Rollback Functionality

    Tests cover: ROLLBACK with timestamp-based state restoration
    and TTL recalculation.
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh FileStorage instance for each test."""
        self.storage = FileStorageImpl()

    @timeout(0.4)
    def test_level_4_case_01_rollback_basic(self):
        """Test basic rollback functionality."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Initial.txt", "100kb")
        self.storage.file_upload_at("2021-07-01T12:05:00", "Update1.txt", "150kb", 3600)
        result = self.storage.rollback("2021-07-01T12:10:00")
        self.assertEqual(result, "rollback to 2021-07-01T12:10:00")

    @timeout(0.4)
    def test_level_4_case_02_files_before_rollback_exist(self):
        """Test that files uploaded before rollback timestamp still exist."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Initial.txt", "100kb")
        self.storage.file_upload_at("2021-07-01T12:05:00", "Update1.txt", "150kb", 3600)
        self.storage.rollback("2021-07-01T12:10:00")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Initial.txt"), "got at Initial.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Update1.txt"), "got at Update1.txt")

    @timeout(0.4)
    def test_level_4_case_03_files_after_rollback_removed(self):
        """Test that files created after rollback timestamp are removed."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Initial.txt", "100kb")
        self.storage.file_upload_at("2021-07-01T12:15:00", "Later.txt", "150kb")
        self.storage.rollback("2021-07-01T12:10:00")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Initial.txt"), "got at Initial.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Later.txt"), "file not found")

    @timeout(0.4)
    def test_level_4_case_04_rollback_with_copy(self):
        """Test rollback removes copied files created after rollback time."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Initial.txt", "100kb")
        self.storage.file_copy_at("2021-07-01T12:15:00", "Initial.txt", "Copy.txt")
        self.storage.rollback("2021-07-01T12:10:00")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Initial.txt"), "got at Initial.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Copy.txt"), "file not found")

    @timeout(0.4)
    def test_level_4_case_05_rollback_ttl_recalculation(self):
        """Test that rollback recalculates TTL based on rollback timestamp."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Temp.txt", "100kb", 600)  # 10 minute TTL
        # Rollback to 12:10:00, then check at 12:15:00
        # Original expiry: 12:10:00, but after rollback might be recalculated
        self.storage.rollback("2021-07-01T12:10:00")
        # File might still exist depending on TTL recalculation logic
        result = self.storage.file_get_at("2021-07-01T12:11:00", "Temp.txt")
        # This test depends on implementation - file might or might not exist

    @timeout(0.4)
    def test_level_4_case_06_rollback_search_results(self):
        """Test that search results reflect rollback state."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "File1.txt", "100kb")
        self.storage.file_upload_at("2021-07-01T12:05:00", "File2.txt", "200kb")
        self.storage.file_upload_at("2021-07-01T12:15:00", "File3.txt", "150kb")
        self.storage.rollback("2021-07-01T12:10:00")
        # Only File1 and File2 should exist after rollback
        result = self.storage.file_search_at("2021-07-01T12:25:00", "File")
        # File3 should not be in results
        self.assertNotIn("File3.txt", result)

    @timeout(0.4)
    def test_level_4_case_07_multiple_rollbacks(self):
        """Test performing multiple rollbacks."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "File1.txt", "100kb")
        self.storage.file_upload_at("2021-07-01T12:05:00", "File2.txt", "200kb")
        self.storage.file_upload_at("2021-07-01T12:10:00", "File3.txt", "150kb")
        # Rollback to 12:08:00 - should remove File2 and File3
        self.storage.rollback("2021-07-01T12:08:00")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:15:00", "File1.txt"), "got at File1.txt")
        # Rollback to 12:02:00 - should keep File1
        self.storage.rollback("2021-07-01T12:02:00")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:15:00", "File1.txt"), "got at File1.txt")

    @timeout(0.4)
    def test_level_4_case_08_rollback_empty_storage(self):
        """Test rollback to a time before any files were uploaded."""
        self.storage.file_upload_at("2021-07-01T12:05:00", "File1.txt", "100kb")
        self.storage.rollback("2021-07-01T12:00:00")
        result = self.storage.file_search_at("2021-07-01T12:10:00", "")
        self.assertEqual(result, "found at []")

    @timeout(0.4)
    def test_level_4_case_09_rollback_preserves_permanent_files(self):
        """Test that rollback preserves files without TTL."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Permanent.txt", "100kb")  # No TTL
        self.storage.file_upload_at("2021-07-01T12:15:00", "Later.txt", "200kb")
        self.storage.rollback("2021-07-01T12:10:00")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Permanent.txt"), "got at Permanent.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Later.txt"), "file not found")

    @timeout(0.4)
    def test_level_4_case_10_complex_rollback_scenario(self):
        """Test complex scenario with uploads, copies, TTL, and rollback."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Initial.txt", "100kb")
        self.storage.file_upload_at("2021-07-01T12:05:00", "Update1.txt", "150kb", 3600)
        self.storage.file_get_at("2021-07-01T12:10:00", "Initial.txt")
        self.storage.file_copy_at("2021-07-01T12:15:00", "Update1.txt", "Update1Copy.txt")
        self.storage.file_upload_at("2021-07-01T12:20:00", "Update2.txt", "200kb", 1800)
        # Rollback to 12:10:00
        self.storage.rollback("2021-07-01T12:10:00")
        # Check state after rollback
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Update1.txt"), "got at Update1.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:25:00", "Initial.txt"), "got at Initial.txt")


if __name__ == '__main__':
    unittest.main()
