import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from file_storage_impl import FileStorageImpl


class Level3Tests(unittest.TestCase):
    """
    Level 3 tests for File Storage - Time-Aware Operations with TTL

    Tests cover: FILE_UPLOAD_AT, FILE_GET_AT, FILE_COPY_AT, FILE_SEARCH_AT
    with timestamp-based operations and TTL (time-to-live) support.
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh FileStorage instance for each test."""
        self.storage = FileStorageImpl()

    @timeout(0.4)
    def test_level_3_case_01_upload_at_without_ttl(self):
        """Test uploading a file at a specific timestamp without TTL."""
        result = self.storage.file_upload_at("2021-07-01T12:00:00", "Python.txt", "150kb")
        self.assertEqual(result, "uploaded at Python.txt")

    @timeout(0.4)
    def test_level_3_case_02_upload_at_with_ttl(self):
        """Test uploading a file with TTL."""
        result = self.storage.file_upload_at("2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600)
        self.assertEqual(result, "uploaded at CodeSignal.txt")

    @timeout(0.4)
    def test_level_3_case_03_get_at_existing_file(self):
        """Test getting a file that exists at the given timestamp."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Python.txt", "150kb")
        result = self.storage.file_get_at("2021-07-01T13:00:01", "Python.txt")
        self.assertEqual(result, "got at Python.txt")

    @timeout(0.4)
    def test_level_3_case_04_copy_at(self):
        """Test copying a file at a specific timestamp."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Python.txt", "150kb")
        result = self.storage.file_copy_at("2021-07-01T12:00:00", "Python.txt", "PythonCopy.txt")
        self.assertEqual(result, "copied at Python.txt to PythonCopy.txt")

    @timeout(0.4)
    def test_level_3_case_05_search_at(self):
        """Test searching files at a specific timestamp."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Python.txt", "150kb")
        self.storage.file_copy_at("2021-07-01T12:00:00", "Python.txt", "PythonCopy.txt")
        result = self.storage.file_search_at("2021-07-01T12:00:00", "Py")
        self.assertEqual(result, "found at [Python.txt, PythonCopy.txt]")

    @timeout(0.4)
    def test_level_3_case_06_ttl_expiration(self):
        """Test that files with TTL expire correctly."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Expired.txt", "100kb", 1)
        # Try to get the file 2 seconds later - should be expired
        result = self.storage.file_get_at("2021-07-01T12:00:02", "Expired.txt")
        self.assertEqual(result, "file not found")

    @timeout(0.4)
    def test_level_3_case_07_ttl_not_expired(self):
        """Test that files within TTL are accessible."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600)
        # Get file within 1 hour (3600 seconds)
        result = self.storage.file_get_at("2021-07-01T12:30:00", "CodeSignal.txt")
        self.assertEqual(result, "got at CodeSignal.txt")

    @timeout(0.4)
    def test_level_3_case_08_copy_inherits_properties(self):
        """Test that copied files inherit properties from source."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600)
        self.storage.file_copy_at("2021-07-01T12:00:00", "CodeSignal.txt", "CodeSignalCopy.txt")
        result = self.storage.file_search_at("2021-07-01T12:00:00", "Code")
        self.assertEqual(result, "found at [CodeSignal.txt, CodeSignalCopy.txt]")

    @timeout(0.4)
    def test_level_3_case_09_mixed_ttl_and_permanent(self):
        """Test mix of files with and without TTL."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "Permanent.txt", "200kb")
        self.storage.file_upload_at("2021-07-01T12:00:00", "Temporary.txt", "100kb", 10)
        # After 5 seconds, both should exist
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:00:05", "Permanent.txt"), "got at Permanent.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:00:05", "Temporary.txt"), "got at Temporary.txt")
        # After 15 seconds, only permanent should exist
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:00:15", "Permanent.txt"), "got at Permanent.txt")
        self.assertEqual(self.storage.file_get_at("2021-07-01T12:00:15", "Temporary.txt"), "file not found")

    @timeout(0.4)
    def test_level_3_case_10_search_excludes_expired(self):
        """Test that search results exclude expired files."""
        self.storage.file_upload_at("2021-07-01T12:00:00", "File1.txt", "200kb")
        self.storage.file_upload_at("2021-07-01T12:00:00", "File2.txt", "100kb", 5)
        # Immediately after upload, both should be found
        self.assertEqual(self.storage.file_search_at("2021-07-01T12:00:00", "File"), "found at [File1.txt, File2.txt]")
        # After TTL expires, only File1 should be found
        self.assertEqual(self.storage.file_search_at("2021-07-01T12:00:10", "File"), "found at [File1.txt]")


if __name__ == '__main__':
    unittest.main()
