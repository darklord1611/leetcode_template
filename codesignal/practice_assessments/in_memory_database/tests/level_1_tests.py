import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from in_memory_database_impl import InMemoryDatabaseImpl


class Level1Tests(unittest.TestCase):
    """
    Level 1 tests for In-Memory Database - Basic Field Operations

    Tests cover: SET_FIELD, GET_FIELD, GET, DELETE_FIELD
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh InMemoryDatabase instance for each test."""
        self.db = InMemoryDatabaseImpl()

    @timeout(0.4)
    def test_level_1_case_01_set_and_get_single_field(self):
        """Test setting and retrieving a single field."""
        self.assertEqual(self.db.set_field("user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.get_field("user1", "name"), "Alice")

    @timeout(0.4)
    def test_level_1_case_02_set_multiple_fields_same_key(self):
        """Test setting multiple fields for the same key."""
        self.assertEqual(self.db.set_field("user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.set_field("user1", "age", "30"), "30")
        self.assertEqual(self.db.set_field("user1", "city", "NYC"), "NYC")

    @timeout(0.4)
    def test_level_1_case_03_get_nonexistent_key(self):
        """Test getting field from non-existent key returns empty string."""
        self.db.set_field("user1", "name", "Alice")
        result = self.db.get_field("user3", "name")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_1_case_04_get_all_fields(self):
        """Test GET operation returns all fields alphabetically."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        self.db.set_field("user1", "city", "NYC")
        result = self.db.get("user1")
        self.assertEqual(result, "age(30), city(NYC), name(Alice)")

    @timeout(0.4)
    def test_level_1_case_05_get_multiple_keys(self):
        """Test GET on multiple different keys."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        self.db.set_field("user1", "city", "NYC")
        self.db.set_field("user2", "name", "Bob")
        self.db.set_field("user2", "age", "25")

        self.assertEqual(self.db.get("user1"), "age(30), city(NYC), name(Alice)")
        self.assertEqual(self.db.get("user2"), "age(25), name(Bob)")

    @timeout(0.4)
    def test_level_1_case_06_delete_field_success(self):
        """Test deleting an existing field returns true."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        result = self.db.delete_field("user1", "age")
        self.assertEqual(result, "true")

    @timeout(0.4)
    def test_level_1_case_07_delete_field_and_verify(self):
        """Test that deleted field is no longer in GET result."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        self.db.set_field("user1", "city", "NYC")
        self.db.delete_field("user1", "age")
        result = self.db.get("user1")
        self.assertEqual(result, "city(NYC), name(Alice)")

    @timeout(0.4)
    def test_level_1_case_08_delete_nonexistent_field(self):
        """Test deleting non-existent field returns false."""
        self.db.set_field("user1", "name", "Alice")
        result = self.db.delete_field("user3", "name")
        self.assertEqual(result, "false")

    @timeout(0.4)
    def test_level_1_case_09_get_deleted_field(self):
        """Test getting a deleted field returns empty string."""
        self.db.set_field("user1", "name", "Alice")
        self.db.set_field("user1", "age", "30")
        self.db.delete_field("user1", "age")
        result = self.db.get_field("user1", "age")
        self.assertEqual(result, "")

    @timeout(0.4)
    def test_level_1_case_10_complete_scenario(self):
        """Test complete scenario from test_data_1."""
        self.assertEqual(self.db.set_field("user1", "name", "Alice"), "Alice")
        self.assertEqual(self.db.set_field("user1", "age", "30"), "30")
        self.assertEqual(self.db.set_field("user1", "city", "NYC"), "NYC")
        self.assertEqual(self.db.set_field("user2", "name", "Bob"), "Bob")
        self.assertEqual(self.db.set_field("user2", "age", "25"), "25")
        self.assertEqual(self.db.get_field("user1", "name"), "Alice")
        self.assertEqual(self.db.get_field("user1", "age"), "30")
        self.assertEqual(self.db.get_field("user3", "name"), "")
        self.assertEqual(self.db.get("user1"), "age(30), city(NYC), name(Alice)")
        self.assertEqual(self.db.get("user2"), "age(25), name(Bob)")
        self.assertEqual(self.db.delete_field("user1", "age"), "true")
        self.assertEqual(self.db.get("user1"), "city(NYC), name(Alice)")
        self.assertEqual(self.db.delete_field("user3", "name"), "false")
        self.assertEqual(self.db.get_field("user1", "age"), "")


if __name__ == '__main__':
    unittest.main()
