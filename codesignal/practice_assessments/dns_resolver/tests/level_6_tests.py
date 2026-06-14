import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level6Tests(unittest.TestCase):
	"""
	Level 6 tests for DNS Resolver - Reverse DNS

	Tests cover: REVERSE_RESOLVE (sorted, expiry-aware, wildcards excluded).
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_6_case_01_reverse_single(self):
		self.dns.add_record(1, "c.com", "2.2.2.2")
		self.assertEqual(self.dns.reverse_resolve(2, "2.2.2.2"), "c.com")

	@timeout(0.4)
	def test_level_6_case_02_reverse_multiple_sorted(self):
		self.dns.add_record(1, "b.com", "1.1.1.1")
		self.dns.add_record(2, "a.com", "1.1.1.1")
		self.assertEqual(self.dns.reverse_resolve(3, "1.1.1.1"), "a.com,b.com")

	@timeout(0.4)
	def test_level_6_case_03_reverse_no_match(self):
		self.dns.add_record(1, "a.com", "1.1.1.1")
		self.assertEqual(self.dns.reverse_resolve(2, "9.9.9.9"), "")

	@timeout(0.4)
	def test_level_6_case_04_reverse_excludes_expired(self):
		self.dns.add_record_with_ttl(10, "d.com", "5.5.5.5", 5)
		self.assertEqual(self.dns.reverse_resolve(20, "5.5.5.5"), "")

	@timeout(0.4)
	def test_level_6_case_05_reverse_excludes_wildcard(self):
		self.dns.add_record(1, "a.com", "1.1.1.1")
		self.dns.add_record(2, "b.com", "1.1.1.1")
		self.dns.add_record(3, "*.x.com", "1.1.1.1")
		self.assertEqual(self.dns.reverse_resolve(4, "1.1.1.1"), "a.com,b.com")

	@timeout(0.4)
	def test_level_6_case_06_reverse_after_remove(self):
		self.dns.add_record(1, "a.com", "1.1.1.1")
		self.dns.add_record(2, "b.com", "1.1.1.1")
		self.dns.remove_ip(3, "a.com", "1.1.1.1")
		self.assertEqual(self.dns.reverse_resolve(4, "1.1.1.1"), "b.com")

	@timeout(0.4)
	def test_level_6_case_07_reverse_domain_with_multiple_ips(self):
		self.dns.add_record(1, "a.com", "1.1.1.1")
		self.dns.add_record(2, "a.com", "2.2.2.2")
		self.assertEqual(self.dns.reverse_resolve(3, "1.1.1.1"), "a.com")
		self.assertEqual(self.dns.reverse_resolve(4, "2.2.2.2"), "a.com")


if __name__ == "__main__":
	unittest.main()
