import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level1Tests(unittest.TestCase):
	"""
	Level 1 tests for DNS Resolver - A Records

	Tests cover: ADD_RECORD, RESOLVE, REMOVE_RECORD
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_1_case_01_add_record_returns_true(self):
		self.assertEqual(self.dns.add_record(1, "example.com", "1.2.3.4"), "true")

	@timeout(0.4)
	def test_level_1_case_02_resolve_existing(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.assertEqual(self.dns.resolve(2, "example.com"), "1.2.3.4")

	@timeout(0.4)
	def test_level_1_case_03_resolve_missing(self):
		self.assertEqual(self.dns.resolve(1, "missing.com"), "")

	@timeout(0.4)
	def test_level_1_case_04_duplicate_ip_ignored(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.assertEqual(self.dns.add_record(2, "example.com", "1.2.3.4"), "true")
		self.assertEqual(self.dns.resolve(3, "example.com"), "1.2.3.4")

	@timeout(0.4)
	def test_level_1_case_05_remove_record_existing(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.assertEqual(self.dns.remove_record(2, "example.com"), "true")
		self.assertEqual(self.dns.resolve(3, "example.com"), "")

	@timeout(0.4)
	def test_level_1_case_06_remove_record_missing(self):
		self.assertEqual(self.dns.remove_record(1, "missing.com"), "false")

	@timeout(0.4)
	def test_level_1_case_07_multiple_domains_independent(self):
		self.dns.add_record(1, "a.com", "1.1.1.1")
		self.dns.add_record(2, "b.com", "2.2.2.2")
		self.assertEqual(self.dns.resolve(3, "a.com"), "1.1.1.1")
		self.assertEqual(self.dns.resolve(4, "b.com"), "2.2.2.2")

	@timeout(0.4)
	def test_level_1_case_08_resolve_after_remove_only_target(self):
		self.dns.add_record(1, "a.com", "1.1.1.1")
		self.dns.add_record(2, "b.com", "2.2.2.2")
		self.dns.remove_record(3, "a.com")
		self.assertEqual(self.dns.resolve(4, "a.com"), "")
		self.assertEqual(self.dns.resolve(5, "b.com"), "2.2.2.2")


if __name__ == "__main__":
	unittest.main()
