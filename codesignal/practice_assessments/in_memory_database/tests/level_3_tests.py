import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_database_impl import InMemoryDatabaseImpl


class Level3Tests(unittest.TestCase):
    """
    Level 3 tests for In-Memory Database - Time-Aware Operations with TTL

    Tests cover: SET_FIELD_AT, SET_FIELD_WITH_TTL, GET_FIELD_AT, GET_AT,
                 SCAN_AT, SCAN_BY_FIELD_AT, DELETE_FIELD_AT
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh InMemoryDatabase instance for each test."""
        self.db = InMemoryDatabaseImpl()

    @timeout(0.4)
    def test_level_3_case_01_set_and_get_field_at_timestamp(self):
        """Test setting and getting field at specific timestamp."""
        self.assertEqual(self.db.set_field_at(1000, "user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.get_field_at(3000, "user1", "name"), "Alice")

    @timeout(0.4)
    def test_level_3_case_02_set_field_with_ttl(self):
        """Test setting field with TTL."""
        self.assertEqual(self.db.set_field_at(1000, "user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 5000), "abc123")
        self.assertEqual(self.db.get_field_at(3000, "user1", "session"), "abc123")

    @timeout(0.4)
    def test_level_3_case_03_ttl_expiration_exact(self):
        """Test that field expires exactly at TTL timestamp."""
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 5000)
        # Valid at timestamp 5999 (1000 + 5000 - 1)
        self.assertEqual(self.db.get_field_at(5999, "user1", "session"), "abc123")
        # Expired at timestamp 6000 (1000 + 5000)
        self.assertEqual(self.db.get_field_at(6000, "user1", "session"), "")

    @timeout(0.4)
    def test_level_3_case_04_get_at_with_mixed_fields(self):
        """Test GET_AT with both permanent and TTL fields."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 5000)
        result = self.db.get_at(3000, "user1")
        self.assertEqual(result, "name(Alice), session(abc123)")

    @timeout(0.4)
    def test_level_3_case_05_get_at_after_ttl_expiration(self):
        """Test GET_AT after TTL field has expired."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 5000)
        # Session expires at 6000, so at 7000 only name should be present
        result = self.db.get_at(7000, "user1")
        self.assertEqual(result, "name(Alice)")

    @timeout(0.4)
    def test_level_3_case_06_multiple_fields_with_different_ttls(self):
        """Test multiple fields with different TTL values."""
        self.db.set_field_at(1000, "user2", "name", "Bob")
        self.db.set_field_with_ttl(2000, "user2", "token", "xyz789", 3000)
        # Token valid until 5000 (2000 + 3000)
        self.assertEqual(self.db.get_field_at(4999, "user2", "token"), "xyz789")
        self.assertEqual(self.db.get_field_at(5000, "user2", "token"), "")

    @timeout(0.4)
    def test_level_3_case_07_scan_at_timestamp(self):
        """Test scanning keys at specific timestamp."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user2", "name", "Bob")
        result = self.db.scan_at(3000, "user")
        self.assertEqual(result, "user1, user2")

    @timeout(0.4)
    def test_level_3_case_08_scan_by_field_at_timestamp(self):
        """Test scanning by field value at specific timestamp."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_at(1000, "user2", "name", "Bob")
        result = self.db.scan_by_field_at(3000, "name", "Alice")
        self.assertEqual(result, "user1")

    @timeout(0.4)
    def test_level_3_case_09_delete_field_at_timestamp(self):
        """Test deleting field at specific timestamp."""
        self.db.set_field_at(1000, "user1", "name", "Alice")
        self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 5000)
        self.assertEqual(self.db.delete_field_at(3000, "user1", "session"), "true")
        # After deletion, field should not be accessible
        self.assertEqual(self.db.get_field_at(4000, "user1", "session"), "")

    @timeout(0.4)
    def test_level_3_case_10_complete_scenario(self):
        """Test complete scenario from test_data_3."""
        self.assertEqual(self.db.set_field_at(1000, "user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.set_field_with_ttl(1000, "user1", "session", "abc123", 5000), "abc123")
        self.assertEqual(self.db.set_field_at(1000, "user2", "name", "Bob"), "Bob")
        self.assertEqual(self.db.set_field_with_ttl(2000, "user2", "token", "xyz789", 3000), "xyz789")
        self.assertEqual(self.db.get_field_at(3000, "user1", "name"), "Alice")
        self.assertEqual(self.db.get_field_at(3000, "user1", "session"), "abc123")
        self.assertEqual(self.db.get_field_at(6000, "user1", "session"), "")
        self.assertEqual(self.db.get_field_at(5999, "user1", "session"), "abc123")
        self.assertEqual(self.db.get_at(3000, "user1"), "name(Alice), session(abc123)")
        self.assertEqual(self.db.get_at(7000, "user1"), "name(Alice)")
        self.assertEqual(self.db.get_field_at(4999, "user2", "token"), "xyz789")
        self.assertEqual(self.db.get_field_at(5000, "user2", "token"), "")
        self.assertEqual(self.db.scan_at(3000, "user"), "user1, user2")
        self.assertEqual(self.db.scan_at(7000, "user"), "user1, user2")
        self.assertEqual(self.db.scan_by_field_at(3000, "name", "Alice"), "user1")
        self.assertEqual(self.db.delete_field_at(3000, "user1", "session"), "true")
        self.assertEqual(self.db.get_field_at(4000, "user1", "session"), "")


if __name__ == '__main__':
    unittest.main()
