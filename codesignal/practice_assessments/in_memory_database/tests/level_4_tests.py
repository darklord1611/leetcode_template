import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from in_memory_database_impl import InMemoryDatabaseImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for In-Memory Database - Backup & Restore

	Tests cover: backup, restore plus reopened reads
	"""

	failureException = Exception

	def setUp(self):
		self.db = InMemoryDatabaseImpl()

	@timeout(0.4)
	def test_level_4_case_01_backup_counts_keys(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field(2, "b", "f1", "1")
		self.assertEqual(self.db.backup(3), "2")

	@timeout(0.4)
	def test_level_4_case_02_backup_ignores_expired(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.set_field_with_ttl(1, "b", "f1", "1", 5)
		# at t=10 b is fully expired
		self.assertEqual(self.db.backup(10), "1")

	@timeout(0.4)
	def test_level_4_case_03_backup_empty(self):
		self.assertEqual(self.db.backup(1), "0")

	@timeout(0.4)
	def test_level_4_case_04_restore_returns_true(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.backup(2)
		self.assertEqual(self.db.restore(5, 2), "true")

	@timeout(0.4)
	def test_level_4_case_05_restore_brings_back_state(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.db.backup(2)
		self.db.set_field(3, "a", "f1", "changed")
		self.db.restore(5, 2)
		self.assertEqual(self.db.get_field(6, "a", "f1"), "v1")

	@timeout(0.4)
	def test_level_4_case_06_restore_replaces_whole_db(self):
		self.db.set_field(1, "a", "f1", "1")
		self.db.backup(2)
		self.db.set_field(3, "b", "f1", "1")
		self.db.restore(5, 2)
		self.assertEqual(self.db.get_field(6, "b", "f1"), "")
		self.assertEqual(self.db.get_field(6, "a", "f1"), "1")

	@timeout(0.4)
	def test_level_4_case_07_restore_preserves_remaining_ttl(self):
		# field set at t=1 with ttl 100 -> expires at 101
		self.db.set_field_with_ttl(1, "a", "f1", "v1", 100)
		# backup at t=51: remaining ttl = 101 - 51 = 50
		self.db.backup(51)
		# restore at t=200: new expire = 200 + 50 = 250
		self.db.restore(200, 51)
		self.assertEqual(self.db.get_field(249, "a", "f1"), "v1")
		self.assertEqual(self.db.get_field(250, "a", "f1"), "")

	@timeout(0.4)
	def test_level_4_case_08_restore_picks_most_recent_le(self):
		self.db.set_field(1, "a", "f1", "first")
		self.db.backup(2)
		self.db.set_field(3, "a", "f1", "second")
		self.db.backup(4)
		# restore with backup_timestamp 3 -> most recent backup <= 3 is the t=2 one
		self.db.restore(10, 3)
		self.assertEqual(self.db.get_field(11, "a", "f1"), "first")

	@timeout(0.4)
	def test_level_4_case_09_restore_no_eligible_backup_noop(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.db.backup(5)
		# no backup at time <= 3, so restore does nothing
		self.db.restore(10, 3)
		self.assertEqual(self.db.get_field(11, "a", "f1"), "v1")

	@timeout(0.4)
	def test_level_4_case_10_restore_permanent_stays_permanent(self):
		self.db.set_field(1, "a", "f1", "v1")
		self.db.backup(2)
		self.db.restore(1000, 2)
		self.assertEqual(self.db.get_field(99999, "a", "f1"), "v1")

	@timeout(0.4)
	def test_level_4_case_11_get_record_after_restore(self):
		self.db.set_field(1, "a", "b", "2")
		self.db.set_field(2, "a", "a", "1")
		self.db.backup(3)
		self.db.set_field(4, "a", "c", "3")
		self.db.restore(5, 3)
		self.assertEqual(self.db.get_record(6, "a"), "a=1, b=2")


if __name__ == "__main__":
	unittest.main()
