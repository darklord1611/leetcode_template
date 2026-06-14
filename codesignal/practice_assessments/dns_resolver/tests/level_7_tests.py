import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from dns_resolver_impl import DnsResolverImpl
from timeout_decorator import timeout


class Level7Tests(unittest.TestCase):
	"""
	Level 7 tests for DNS Resolver - Weighted Load Balancing & Analytics

	Tests cover: ADD_RECORD_WITH_WEIGHT (smooth weighted round-robin),
	GET_RESOLUTION_STATS, TOP_DOMAINS.
	"""

	failureException = Exception

	def setUp(self):
		self.dns = DnsResolverImpl()

	@timeout(0.4)
	def test_level_7_case_01_add_record_with_weight_returns_true(self):
		self.assertEqual(self.dns.add_record_with_weight(1, "d", "1.1.1.1", 2), "true")

	@timeout(0.4)
	def test_level_7_case_02_weighted_round_robin_2_1(self):
		self.dns.add_record_with_weight(1, "d", "1.1.1.1", 2)
		self.dns.add_record_with_weight(2, "d", "2.2.2.2", 1)
		seq = [self.dns.resolve(3 + i, "d") for i in range(3)]
		self.assertEqual(seq, ["1.1.1.1", "2.2.2.2", "1.1.1.1"])

	@timeout(0.4)
	def test_level_7_case_03_weighted_round_robin_5_1(self):
		self.dns.add_record_with_weight(1, "d", "a", 5)
		self.dns.add_record_with_weight(2, "d", "b", 1)
		seq = [self.dns.resolve(3 + i, "d") for i in range(6)]
		self.assertEqual(seq, ["a", "a", "a", "b", "a", "a"])

	@timeout(0.4)
	def test_level_7_case_04_default_weight_is_one(self):
		self.dns.add_record_with_weight(1, "d", "1.1.1.1", 2)
		self.dns.add_record(2, "d", "2.2.2.2")
		seq = [self.dns.resolve(3 + i, "d") for i in range(3)]
		self.assertEqual(seq, ["1.1.1.1", "2.2.2.2", "1.1.1.1"])

	@timeout(0.4)
	def test_level_7_case_05_resolution_stats(self):
		self.dns.add_record_with_weight(1, "d", "1.1.1.1", 2)
		self.dns.add_record_with_weight(2, "d", "2.2.2.2", 1)
		for i in range(3):
			self.dns.resolve(3 + i, "d")
		self.assertEqual(self.dns.get_resolution_stats(10, "d"), "1.1.1.1:2,2.2.2.2:1")

	@timeout(0.4)
	def test_level_7_case_06_resolution_stats_never_resolved(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.assertEqual(self.dns.get_resolution_stats(2, "d"), "")

	@timeout(0.4)
	def test_level_7_case_07_top_domains(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "e", "2.2.2.2")
		self.dns.resolve(3, "d")
		self.dns.resolve(4, "d")
		self.dns.resolve(5, "d")
		self.dns.resolve(6, "e")
		self.assertEqual(self.dns.top_domains(7, 2), "d,e")

	@timeout(0.4)
	def test_level_7_case_08_top_domains_limit(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.dns.add_record(2, "e", "2.2.2.2")
		self.dns.resolve(3, "d")
		self.dns.resolve(4, "d")
		self.dns.resolve(5, "e")
		self.assertEqual(self.dns.top_domains(6, 1), "d")

	@timeout(0.4)
	def test_level_7_case_09_top_domains_tie_lexicographic(self):
		self.dns.add_record(1, "e", "2.2.2.2")
		self.dns.add_record(2, "d", "1.1.1.1")
		self.dns.resolve(3, "e")
		self.dns.resolve(4, "d")
		self.assertEqual(self.dns.top_domains(5, 2), "d,e")

	@timeout(0.4)
	def test_level_7_case_10_top_domains_none(self):
		self.dns.add_record(1, "d", "1.1.1.1")
		self.assertEqual(self.dns.top_domains(2, 3), "")


if __name__ == "__main__":
	unittest.main()
