import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level5Tests(unittest.TestCase):
	"""
	Level 5 tests for DNS Resolver - Wildcard Records

	Tests cover: wildcard matching, exact precedence, most-specific match.
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_5_case_01_wildcard_match(self):
		self.dns.add_record(1, "*.example.com", "1.1.1.1")
		self.assertEqual(self.dns.resolve(2, "a.example.com"), "1.1.1.1")

	@timeout(0.4)
	def test_level_5_case_02_wildcard_multi_label(self):
		self.dns.add_record(1, "*.example.com", "1.1.1.1")
		self.assertEqual(self.dns.resolve(2, "a.b.example.com"), "1.1.1.1")

	@timeout(0.4)
	def test_level_5_case_03_exact_beats_wildcard(self):
		self.dns.add_record(1, "*.example.com", "1.1.1.1")
		self.dns.add_record(2, "a.example.com", "2.2.2.2")
		self.assertEqual(self.dns.resolve(3, "a.example.com"), "2.2.2.2")
		self.assertEqual(self.dns.resolve(4, "z.example.com"), "1.1.1.1")

	@timeout(0.4)
	def test_level_5_case_04_most_specific_wildcard(self):
		self.dns.add_record(1, "*.example.com", "1.1.1.1")
		self.dns.add_record(2, "*.sub.example.com", "3.3.3.3")
		self.assertEqual(self.dns.resolve(3, "x.sub.example.com"), "3.3.3.3")
		self.assertEqual(self.dns.resolve(4, "x.example.com"), "1.1.1.1")

	@timeout(0.4)
	def test_level_5_case_05_no_match(self):
		self.dns.add_record(1, "*.example.com", "1.1.1.1")
		self.assertEqual(self.dns.resolve(2, "a.other.com"), "")

	@timeout(0.4)
	def test_level_5_case_06_wildcard_does_not_match_apex(self):
		self.dns.add_record(1, "*.example.com", "1.1.1.1")
		self.assertEqual(self.dns.resolve(2, "example.com"), "")

	@timeout(0.4)
	def test_level_5_case_07_exact_cname_beats_wildcard(self):
		self.dns.add_record(1, "target.com", "8.8.8.8")
		self.dns.add_record(2, "*.example.com", "1.1.1.1")
		self.dns.add_alias(3, "a.example.com", "target.com")
		self.assertEqual(self.dns.resolve(4, "a.example.com"), "8.8.8.8")

	@timeout(0.4)
	def test_level_5_case_08_wildcard_round_robin(self):
		self.dns.add_record(1, "*.example.com", "2.2.2.2")
		self.dns.add_record(2, "*.example.com", "1.1.1.1")
		seq = [self.dns.resolve(3 + i, "a.example.com") for i in range(3)]
		self.assertEqual(seq, ["2.2.2.2", "1.1.1.1", "2.2.2.2"])

	@timeout(0.4)
	def test_level_5_case_09_wildcard_with_ttl_expires(self):
		self.dns.add_record_with_ttl(1, "*.example.com", "1.1.1.1", 5)
		self.assertEqual(self.dns.resolve(2, "a.example.com"), "1.1.1.1")
		self.assertEqual(self.dns.resolve(6, "a.example.com"), "")


if __name__ == "__main__":
	unittest.main()
