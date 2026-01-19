import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_database_impl import InMemoryDatabaseImpl


class Level2Tests(unittest.TestCase):
    """
    Level 2 tests for In-Memory Database - Filtering and Querying

    Tests cover: SCAN, SCAN_BY_FIELD, TOP_N_KEYS, DELETE
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh InMemoryDatabase instance for each test."""
        self.db = InMemoryDatabaseImpl()

    @timeout(0.4)
    def test_level_2_case_01_scan_with_prefix(self):
        """Test scanning keys with a specific prefix."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user2", "name", "Bob")
        self.db.set_field("user3", "name", "Charlie")
        self.db.set_field("admin1", "name", "Dave")
        result = self.db.scan("user")
        self.assertEqual(result, "user1, user2, user3")

    @timeout(0.4)
    def test_level_2_case_02_scan_single_match(self):
        """Test scanning with prefix that matches single key."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user2", "name", "Bob")
        self.db.set_field("admin1", "name", "Dave")
        result = self.db.scan("admin")
        self.assertEqual(result, "admin1")

    @timeout(0.4)
    def test_level_2_case_03_scan_by_field_value(self):
        """Test scanning keys by field value."""
        self.db.set_field("user1", "city", "NYC")
        self.db.set_field("user2", "city", "LA")
        self.db.set_field("user3", "city", "NYC")
        result = self.db.scan_by_field("city", "NYC")
        self.assertEqual(result, "user1, user3")

    @timeout(0.4)
    def test_level_2_case_04_scan_by_field_different_values(self):
        """Test scanning by field with multiple different values."""
        self.db.set_field("user1", "age", "30")
        self.db.set_field("user2", "age", "25")
        self.db.set_field("user3", "age", "30")
        result = self.db.scan_by_field("age", "30")
        self.assertEqual(result, "user1, user3")

    @timeout(0.4)
    def test_level_2_case_05_top_n_keys_by_field_count(self):
        """Test getting top N keys by number of fields."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        self.db.set_field("user1", "city", "NYC")
        self.db.set_field("user2", "name", "Bob")
        self.db.set_field("user2", "city", "LA")
        self.db.set_field("user3", "name", "Charlie")
        self.db.set_field("user3", "age", "30")
        self.db.set_field("user3", "city", "NYC")
        self.db.set_field("user3", "country", "USA")
        result = self.db.top_n_keys(3)
        self.assertEqual(result, "user3(4), user1(3), user2(2)")

    @timeout(0.4)
    def test_level_2_case_06_delete_key(self):
        """Test deleting a key returns true."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user2", "name", "Bob")
        result = self.db.delete("user2")
        self.assertEqual(result, "true")

    @timeout(0.4)
    def test_level_2_case_07_scan_after_delete(self):
        """Test scanning after deleting a key."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user2", "name", "Bob")
        self.db.set_field("user3", "name", "Charlie")
        self.db.delete("user2")
        result = self.db.scan("user")
        self.assertEqual(result, "user1, user3")

    @timeout(0.4)
    def test_level_2_case_08_top_n_after_delete(self):
        """Test top N keys after deletion."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        self.db.set_field("user1", "city", "NYC")
        self.db.set_field("user2", "name", "Bob")
        self.db.set_field("user2", "city", "LA")
        self.db.set_field("user3", "name", "Charlie")
        self.db.set_field("user3", "age", "30")
        self.db.set_field("user3", "city", "NYC")
        self.db.set_field("user3", "country", "USA")
        self.db.delete("user2")
        result = self.db.top_n_keys(2)
        self.assertEqual(result, "user3(4), user1(3)")

    @timeout(0.4)
    def test_level_2_case_09_top_n_with_limit(self):
        """Test top N with fewer keys than requested."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user2", "name", "Bob")
        result = self.db.top_n_keys(5)
        # Should return only 2 keys even though 5 were requested
        self.assertIn("user1", result)
        self.assertIn("user2", result)

    @timeout(0.4)
    def test_level_2_case_10_complete_scenario(self):
        """Test complete scenario from test_data_2."""
        self.assertEqual(self.db.set_field("user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.set_field("user1", "age", "30"), "30")
        self.assertEqual(self.db.set_field("user1", "city", "NYC"), "NYC")
        self.assertEqual(self.db.set_field("user2", "name", "Bob"), "Bob")
        self.assertEqual(self.db.set_field("user2", "city", "LA"), "LA")
        self.assertEqual(self.db.set_field("user3", "name", "Charlie"), "Charlie")
        self.assertEqual(self.db.set_field("user3", "age", "30"), "30")
        self.assertEqual(self.db.set_field("user3", "city", "NYC"), "NYC")
        self.assertEqual(self.db.set_field("user3", "country", "USA"), "USA")
        self.assertEqual(self.db.set_field("admin1", "name", "Dave"), "Dave")
        self.assertEqual(self.db.scan("user"), "user1, user2, user3")
        self.assertEqual(self.db.scan("admin"), "admin1")
        self.assertEqual(self.db.scan_by_field("city", "NYC"), "user1, user3")
        self.assertEqual(self.db.scan_by_field("age", "30"), "user1, user3")
        self.assertEqual(self.db.top_n_keys(3), "user3(4), user1(3), user2(2)")
        self.assertEqual(self.db.delete("user2"), "true")
        self.assertEqual(self.db.scan("user"), "user1, user3")
        self.assertEqual(self.db.top_n_keys(2), "user3(4), user1(3)")


if __name__ == '__main__':
    unittest.main()
