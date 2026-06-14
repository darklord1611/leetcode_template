import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level3Tests(unittest.TestCase):
	"""
	Level 3 tests for DNS Resolver - Multiple IPs & Round-Robin

	Tests cover: round-robin RESOLVE (observed over successive calls), REMOVE_IP.
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_3_case_01_round_robin(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "d", "2.2.2.2")
		self.dns.add_record(3, "d", "3.3.3.3")
		seq = [self.dns.resolve(4 + i, "d") for i in range(3)]
		self.assertEqual(seq, ["1.1.1.1", "2.2.2.2", "3.3.3.3"])

	@timeout(0.4)
	def test_level_3_case_02_round_robin_wraps(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "d", "2.2.2.2")
		seq = [self.dns.resolve(3 + i, "d") for i in range(3)]
		self.assertEqual(seq, ["1.1.1.1", "2.2.2.2", "1.1.1.1"])

	@timeout(0.4)
	def test_level_3_case_03_single_ip_round_robin(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		seq = [self.dns.resolve(2 + i, "d") for i in range(2)]
		self.assertEqual(seq, ["1.1.1.1", "1.1.1.1"])

	@timeout(0.4)
	def test_level_3_case_04_remove_ip(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "d", "2.2.2.2")
		self.assertEqual(self.dns.remove_ip(3, "d", "1.1.1.1"), "true")
		seq = [self.dns.resolve(4 + i, "d") for i in range(2)]
		self.assertEqual(seq, ["2.2.2.2", "2.2.2.2"])

	@timeout(0.4)
	def test_level_3_case_05_remove_ip_missing(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.assertEqual(self.dns.remove_ip(2, "d", "9.9.9.9"), "false")

	@timeout(0.4)
	def test_level_3_case_06_remove_last_ip_resolves_empty(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.assertEqual(self.dns.remove_ip(2, "d", "1.1.1.1"), "true")
		self.assertEqual(self.dns.resolve(3, "d"), "")

	@timeout(0.4)
	def test_level_3_case_07_round_robin_through_alias(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "d", "2.2.2.2")
		self.dns.add_alias(3, "e", "d")
		seq = [self.dns.resolve(4 + i, "e") for i in range(3)]
		self.assertEqual(seq, ["1.1.1.1", "2.2.2.2", "1.1.1.1"])

	@timeout(0.4)
	def test_level_3_case_08_alias_and_direct_share_round_robin(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "d", "2.2.2.2")
		self.dns.add_alias(3, "e", "d")
		self.assertEqual(self.dns.resolve(4, "d"), "1.1.1.1")
		self.assertEqual(self.dns.resolve(5, "e"), "2.2.2.2")
		self.assertEqual(self.dns.resolve(6, "d"), "1.1.1.1")

	@timeout(0.4)
	def test_level_3_case_09_multiple_domains_independent_state(self):
		self.dns.add_record(1, "a", "1.1.1.1")
		self.dns.add_record(2, "a", "2.2.2.2")
		self.dns.add_record(3, "b", "3.3.3.3")
		self.dns.add_record(4, "b", "4.4.4.4")
		self.assertEqual(self.dns.resolve(5, "a"), "1.1.1.1")
		self.assertEqual(self.dns.resolve(6, "b"), "3.3.3.3")
		self.assertEqual(self.dns.resolve(7, "a"), "2.2.2.2")
		self.assertEqual(self.dns.resolve(8, "b"), "4.4.4.4")


if __name__ == "__main__":
	unittest.main()
