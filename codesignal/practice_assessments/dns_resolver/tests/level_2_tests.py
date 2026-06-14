import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level2Tests(unittest.TestCase):
	"""
	Level 2 tests for DNS Resolver - CNAME Aliases

	Tests cover: ADD_ALIAS and CNAME-following RESOLVE.
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_2_case_01_add_alias_returns_true(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.assertEqual(self.dns.add_alias(2, "www.example.com", "example.com"), "true")

	@timeout(0.4)
	def test_level_2_case_02_resolve_through_alias(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.dns.add_alias(2, "www.example.com", "example.com")
		self.assertEqual(self.dns.resolve(3, "www.example.com"), "1.2.3.4")

	@timeout(0.4)
	def test_level_2_case_03_resolve_through_alias_chain(self):
		self.dns.add_alias(1, "a", "b")
		self.dns.add_alias(2, "b", "c")
		self.dns.add_record(3, "c", "9.9.9.9")
		self.assertEqual(self.dns.resolve(4, "a"), "9.9.9.9")

	@timeout(0.4)
	def test_level_2_case_04_alias_on_a_record_fails(self):
		self.dns.add_record(1, "x", "1.1.1.1")
		self.assertEqual(self.dns.add_alias(2, "x", "y"), "false")

	@timeout(0.4)
	def test_level_2_case_05_alias_replaced(self):
		self.dns.add_record(1, "b", "2.2.2.2")
		self.dns.add_record(2, "c", "3.3.3.3")
		self.dns.add_alias(3, "a", "b")
		self.dns.add_alias(4, "a", "c")
		self.assertEqual(self.dns.resolve(5, "a"), "3.3.3.3")

	@timeout(0.4)
	def test_level_2_case_06_resolve_alias_to_empty_domain(self):
		self.dns.add_alias(1, "a", "b")
		self.assertEqual(self.dns.resolve(2, "a"), "")

	@timeout(0.4)
	def test_level_2_case_07_resolve_cycle_detection(self):
		self.dns.add_alias(1, "p", "q")
		self.dns.add_alias(2, "q", "p")
		self.assertEqual(self.dns.resolve(3, "p"), "")

	@timeout(0.4)
	def test_level_2_case_08_alias_added_before_target(self):
		self.dns.add_alias(1, "www.example.com", "example.com")
		self.dns.add_record(2, "example.com", "1.2.3.4")
		self.assertEqual(self.dns.resolve(3, "www.example.com"), "1.2.3.4")

	@timeout(0.4)
	def test_level_2_case_09_resolve_alias_still_works_after_target_removed(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.dns.add_alias(2, "www.example.com", "example.com")
		self.dns.remove_record(3, "example.com")
		self.assertEqual(self.dns.resolve(4, "www.example.com"), "")

	@timeout(0.4)
	def test_level_2_case_10_direct_a_record_still_resolves(self):
		self.dns.add_record(1, "example.com", "1.2.3.4")
		self.dns.add_alias(2, "www.example.com", "example.com")
		self.assertEqual(self.dns.resolve(3, "example.com"), "1.2.3.4")


if __name__ == "__main__":
	unittest.main()
