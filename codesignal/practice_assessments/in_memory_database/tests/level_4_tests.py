import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_database_impl import InMemoryDatabaseImpl


class Level4Tests(unittest.TestCase):
    """
    Level 4 tests for In-Memory Database - Backup and Restore

    Tests cover: BACKUP, GET_BACKUP_INFO, RESTORE, COMPARE
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh InMemoryDatabase instance for each test."""
        self.db = InMemoryDatabaseImpl()

    @timeout(0.4)
    def test_level_4_case_01_create_backup(self):
        """Test creating a backup."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user1", "age", "30")
        result = self.db.backup(2000)
        self.assertEqual(result, "backup_1")

    @timeout(0.4)
    def test_level_4_case_02_multiple_backups(self):
        """Test creating multiple backups."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.assertEqual(self.db.backup(2000), "backup_1")
        self.db.set_field_at(3000, "user2", "name", "Bob")
        self.assertEqual(self.db.backup(4000), "backup_2")

    @timeout(0.4)
    def test_level_4_case_03_get_backup_info(self):
        """Test getting backup information."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user1", "age", "30")
        self.db.set_field_at(2000, "user2", "name", "Bob")
        self.db.backup(2000)
        result = self.db.get_backup_info("backup_1")
        self.assertEqual(result, "keys:2,fields:3,timestamp:2000")

    @timeout(0.4)
    def test_level_4_case_04_get_backup_info_with_ttl(self):
        """Test backup info includes TTL fields."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user1", "age", "30")
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 10000)
        self.db.set_field_at(2000, "user2", "name", "Bob")
        self.db.backup(2000)
        result = self.db.get_backup_info("backup_1")
        self.assertEqual(result, "keys:2,fields:4,timestamp:2000")

    @timeout(0.4)
    def test_level_4_case_05_compare_backups(self):
        """Test comparing two backups."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user1", "age", "30")
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 10000)
        self.db.set_field_at(2000, "user2", "name", "Bob")
        self.db.backup(2000)
        self.db.set_field_at(3000, "user1", "city", "NYC")
        self.db.set_field_at(3000, "user3", "name", "Charlie")
        self.db.backup(3000)
        result = self.db.compare("backup_1", "backup_2")
        self.assertEqual(result, "user1, user3")

    @timeout(0.4)
    def test_level_4_case_06_restore_backup(self):
        """Test restoring from backup."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user1", "age", "30")
        self.db.backup(2000)
        self.db.delete("user1")
        self.assertEqual(self.db.get_at(3000, "user1"), "")
        # Restore should return number of keys restored
        result = self.db.restore(3000, "backup_1")
        self.assertEqual(result, "1")
        # After restore, data should be accessible
        self.assertEqual(self.db.get_at(3000, "user1"), "age(30), name(Alice)")

    @timeout(0.4)
    def test_level_4_case_07_restore_ttl_recalculation(self):
        """Test TTL recalculation after restore."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 10000)
        self.db.backup(2000)
        self.db.delete("user1")
        self.db.restore(4000, "backup_1")
        # Original TTL: expires at 1000 + 10000 = 11000
        # At backup time (2000), remaining TTL = 11000 - 2000 = 9000
        # After restore at 4000, new expiry = 4000 + 9000 = 13000
        self.assertEqual(self.db.get_field_at(13000, "user1", "session"), "abc123")
        self.assertEqual(self.db.get_field_at(13001, "user1", "session"), "")

    @timeout(0.4)
    def test_level_4_case_08_restore_multiple_keys(self):
        """Test restoring multiple keys."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user1", "age", "30")
        self.db.set_field_at(2000, "user2", "name", "Bob")
        self.db.backup(2000)
        self.db.delete("user1")
        self.db.delete("user2")
        result = self.db.restore(4000, "backup_1")
        self.assertEqual(result, "2")

    @timeout(0.4)
    def test_level_4_case_09_backup_after_modifications(self):
        """Test backup captures latest state."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.backup(2000)
        self.db.set_field_at(3000, "user1", "city", "NYC")
        self.db.set_field_at(3000, "user3", "name", "Charlie")
        self.db.backup(3000)
        info1 = self.db.get_backup_info("backup_1")
        info2 = self.db.get_backup_info("backup_2")
        self.assertEqual(info1, "keys:1,fields:1,timestamp:2000")
        self.assertEqual(info2, "keys:2,fields:2,timestamp:3000")

    @timeout(0.4)
    def test_level_4_case_10_complete_scenario(self):
        """Test complete scenario from test_data_4."""
        self.assertEqual(self.db.set_field_at(1000, "user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.set_field_at(1000, "user1", "age", "30"), "30")
        self.assertEqual(self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 10000), "abc123")
        self.assertEqual(self.db.set_field_at(2000, "user2", "name", "Bob"), "Bob")
        self.assertEqual(self.db.backup(2000), "backup_1")
        self.assertEqual(self.db.set_field_at(3000, "user1", "city", "NYC"), "NYC")
        self.assertEqual(self.db.set_field_at(3000, "user3", "name", "Charlie"), "Charlie")
        self.assertEqual(self.db.backup(3000), "backup_2")
        self.assertEqual(self.db.get_backup_info("backup_1"), "keys:2,fields:4,timestamp:2000")
        self.assertEqual(self.db.get_backup_info("backup_2"), "keys:3,fields:6,timestamp:3000")
        self.assertEqual(self.db.compare("backup_1", "backup_2"), "user1, user3")
        self.assertEqual(self.db.delete("user1"), "true")
        self.assertEqual(self.db.delete("user2"), "true")
        self.assertEqual(self.db.delete("user3"), "true")
        self.assertEqual(self.db.get_at(4000, "user1"), "")
        self.assertEqual(self.db.restore(4000, "backup_1"), "2")
        self.assertEqual(self.db.get_at(4000, "user1"), "age(30), name(Alice), session(abc123)")
        self.assertEqual(self.db.get_at(4000, "user2"), "name(Bob)")
        self.assertEqual(self.db.get_field_at(13000, "user1", "session"), "abc123")
        self.assertEqual(self.db.get_field_at(13001, "user1", "session"), "")


if __name__ == '__main__':
    unittest.main()
