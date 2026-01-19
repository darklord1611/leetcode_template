import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from integer_container_impl import IntegerContainerImpl


class Level1Tests(unittest.TestCase):
    """
    The test class below includes 10 tests for Level 1.

    All have the same score.
    You are not allowed to modify this file, but feel free to read the source code to better understand what is happening in every specific case.
    """

    failureException = Exception


    @classmethod
    def setUp(cls):
        cls.container = IntegerContainerImpl()

    @timeout(0.4)
    def test_level_1_case_01_add_two_numbers(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(100), 2)

    @timeout(0.4)
    def test_level_1_case_02_add_many_numbers(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(9), 2)
        self.assertEqual(self.container.add(8), 3)
        self.assertEqual(self.container.add(7), 4)
        self.assertEqual(self.container.add(6), 5)
        self.assertEqual(self.container.add(5), 6)
        self.assertEqual(self.container.add(4), 7)
        self.assertEqual(self.container.add(3), 8)
        self.assertEqual(self.container.add(2), 9)
        self.assertEqual(self.container.add(1), 10)

    @timeout(0.4)
    def test_level_1_case_03_delete_number(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(100), 2)
        self.assertTrue(self.container.delete(10))

    @timeout(0.4)
    def test_level_1_case_04_delete_nonexisting_number(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(100), 2)
        self.assertFalse(self.container.delete(20))
        self.assertTrue(self.container.delete(10))
        self.assertFalse(self.container.delete(10))

    @timeout(0.4)
    def test_level_1_case_05_add_and_delete_same_numbers(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(10), 2)
        self.assertEqual(self.container.add(10), 3)
        self.assertEqual(self.container.add(10), 4)
        self.assertEqual(self.container.add(10), 5)
        self.assertTrue(self.container.delete(10))
        self.assertTrue(self.container.delete(10))
        self.assertTrue(self.container.delete(10))
        self.assertTrue(self.container.delete(10))
        self.assertTrue(self.container.delete(10))
        self.assertFalse(self.container.delete(10))
        self.assertFalse(self.container.delete(10))

    @timeout(0.4)
    def test_level_1_case_06_add_delete_several_times(self):
        self.assertEqual(self.container.add(555), 1)
        self.assertTrue(self.container.delete(555))
        self.assertFalse(self.container.delete(555))
        self.assertEqual(self.container.add(555), 1)
        self.assertTrue(self.container.delete(555))
        self.assertFalse(self.container.delete(555))

    @timeout(0.4)
    def test_level_1_case_07_delete_in_random_order(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(20), 2)
        self.assertEqual(self.container.add(30), 3)
        self.assertEqual(self.container.add(40), 4)
        self.assertEqual(self.container.add(40), 5)
        self.assertTrue(self.container.delete(30))
        self.assertFalse(self.container.delete(30))
        self.assertTrue(self.container.delete(10))
        self.assertFalse(self.container.delete(10))
        self.assertTrue(self.container.delete(40))
        self.assertTrue(self.container.delete(40))
        self.assertFalse(self.container.delete(40))
        self.assertTrue(self.container.delete(20))
        self.assertFalse(self.container.delete(20))

    @timeout(0.4)
    def test_level_1_case_08_delete_before_add(self):
        self.assertFalse(self.container.delete(1))
        self.assertFalse(self.container.delete(2))
        self.assertFalse(self.container.delete(3))
        self.assertEqual(self.container.add(1), 1)
        self.assertEqual(self.container.add(2), 2)
        self.assertEqual(self.container.add(3), 3)
        self.assertTrue(self.container.delete(3))
        self.assertTrue(self.container.delete(2))
        self.assertTrue(self.container.delete(1))
        self.assertFalse(self.container.delete(3))
        self.assertFalse(self.container.delete(2))
        self.assertFalse(self.container.delete(1))

    @timeout(0.4)
    def test_level_1_case_09_mixed_operation_1(self):
        self.assertEqual(self.container.add(10), 1)
        self.assertEqual(self.container.add(15), 2)
        self.assertEqual(self.container.add(20), 3)
        self.assertEqual(self.container.add(10), 4)
        self.assertEqual(self.container.add(5), 5)
        self.assertTrue(self.container.delete(15))
        self.assertTrue(self.container.delete(20))
        self.assertFalse(self.container.delete(20))
        self.assertFalse(self.container.delete(0))
        self.assertEqual(self.container.add(7), 4)
        self.assertEqual(self.container.add(9), 5)
        self.assertTrue(self.container.delete(7))
        self.assertTrue(self.container.delete(10))
        self.assertTrue(self.container.delete(10))
        self.assertFalse(self.container.delete(10))
        self.assertFalse(self.container.delete(100))

    @timeout(0.4)
    def test_level_1_case_10_mixed_operation_2(self):
        self.assertFalse(self.container.delete(6))
        self.assertEqual(self.container.add(100), 1)
        self.assertFalse(self.container.delete(200))
        self.assertEqual(self.container.add(500), 2)
        self.assertFalse(self.container.delete(0))
        self.assertEqual(self.container.add(300), 3)
        self.assertFalse(self.container.delete(1000))
        self.assertEqual(self.container.add(400), 4)
        self.assertTrue(self.container.delete(300))
        self.assertTrue(self.container.delete(400))
        self.assertTrue(self.container.delete(100))
        self.assertTrue(self.container.delete(500))
        self.assertEqual(self.container.add(1000), 1)
        self.assertEqual(self.container.add(100), 2)
        self.assertEqual(self.container.add(10), 3)
        self.assertEqual(self.container.add(1), 4)
        self.assertTrue(self.container.delete(100))
        self.assertFalse(self.container.delete(500))
        self.assertFalse(self.container.delete(300))
        self.assertFalse(self.container.delete(400))
