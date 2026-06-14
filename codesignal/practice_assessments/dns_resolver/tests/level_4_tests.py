import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level4Tests(unittest.TestCase):
	"""
	Level 4 tests for DNS Resolver - Record TTL & Expiration

	Tests cover: ADD_RECORD_WITH_TTL and expiry-aware RESOLVE.
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_4_case_01_add_record_with_ttl_returns_true(self):
		self.assertEqual(self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5), "true")

	@timeout(0.4)
	def test_level_4_case_02_resolve_before_expiry(self):
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.assertEqual(self.dns.resolve(12, "d"), "1.1.1.1")

	@timeout(0.4)
	def test_level_4_case_03_resolve_at_add_time(self):
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.assertEqual(self.dns.resolve(10, "d"), "1.1.1.1")

	@timeout(0.4)
	def test_level_4_case_04_resolve_after_expiry(self):
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.assertEqual(self.dns.resolve(15, "d"), "")

	@timeout(0.4)
	def test_level_4_case_05_expiry_is_exclusive(self):
		# valid for [10, 15); at 15 it is expired
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.assertEqual(self.dns.resolve(14, "d"), "1.1.1.1")
		self.assertEqual(self.dns.resolve(15, "d"), "")

	@timeout(0.4)
	def test_level_4_case_06_permanent_record_does_not_expire(self):
		self.dns.add_record(10, "d", "1.1.1.1")
		self.assertEqual(self.dns.resolve(1000, "d"), "1.1.1.1")

	@timeout(0.4)
	def test_level_4_case_07_resolve_skips_expired_keeps_live(self):
		self.dns.add_record(10, "d", "9.9.9.9")
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.assertEqual(self.dns.resolve(20, "d"), "9.9.9.9")

	@timeout(0.4)
	def test_level_4_case_08_round_robin_skips_expired(self):
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.dns.add_record(10, "d", "2.2.2.2")
		self.assertEqual(self.dns.resolve(20, "d"), "2.2.2.2")
		self.assertEqual(self.dns.resolve(21, "d"), "2.2.2.2")

	@timeout(0.4)
	def test_level_4_case_09_alias_to_all_expired_resolves_empty(self):
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.dns.add_alias(10, "e", "d")
		self.assertEqual(self.dns.resolve(20, "e"), "")

	@timeout(0.4)
	def test_level_4_case_10_alias_to_partially_expired_resolves_live(self):
		self.dns.add_record_with_ttl(10, "d", "1.1.1.1", 5)
		self.dns.add_record(10, "d", "2.2.2.2")
		self.dns.add_alias(10, "e", "d")
		self.assertEqual(self.dns.resolve(20, "e"), "2.2.2.2")


if __name__ == "__main__":
	unittest.main()
