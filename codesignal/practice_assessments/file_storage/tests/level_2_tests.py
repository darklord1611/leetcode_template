import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from file_storage_impl import FileStorageImpl


class Level2Tests(unittest.TestCase):
    """
    Level 2 tests for File Storage - Search and Query Operations

    Tests cover: FILE_SEARCH with prefix matching and size sorting
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh FileStorage instance for each test."""
        self.storage = FileStorageImpl()

    @timeout(0.4)
    def test_level_2_case_01_search_by_prefix(self):
        """Test searching files by prefix, sorted by size descending."""
        self.storage.file_upload("Foo.txt", "100kb")
        self.storage.file_upload("Bar.csv", "200kb")
        self.storage.file_upload("Baz.pdf", "300kb")
        result = self.storage.file_search("Ba")
        self.assertEqual(result, "found [Baz.pdf, Bar.csv]")

    @timeout(0.4)
    def test_level_2_case_02_search_single_match(self):
        """Test searching with a single matching file."""
        self.storage.file_upload("Foo.txt", "100kb")
        self.storage.file_upload("Bar.csv", "200kb")
        result = self.storage.file_search("Foo")
        self.assertEqual(result, "found [Foo.txt]")

    @timeout(0.4)
    def test_level_2_case_03_search_no_matches(self):
        """Test searching with no matching files."""
        self.storage.file_upload("Foo.txt", "100kb")
        self.storage.file_upload("Bar.csv", "200kb")
        result = self.storage.file_search("Xyz")
        self.assertEqual(result, "found []")

    @timeout(0.4)
    def test_level_2_case_04_search_all_files(self):
        """Test searching with empty prefix matches all files."""
        self.storage.file_upload("Small.txt", "50kb")
        self.storage.file_upload("Medium.txt", "100kb")
        self.storage.file_upload("Large.txt", "200kb")
        result = self.storage.file_search("")
        self.assertEqual(result, "found [Large.txt, Medium.txt, Small.txt]")

    @timeout(0.4)
    def test_level_2_case_05_search_size_ordering(self):
        """Test that search results are ordered by size (descending)."""
        self.storage.file_upload("File1.txt", "300kb")
        self.storage.file_upload("File2.txt", "100kb")
        self.storage.file_upload("File3.txt", "200kb")
        result = self.storage.file_search("File")
        self.assertEqual(result, "found [File1.txt, File3.txt, File2.txt]")

    @timeout(0.4)
    def test_level_2_case_06_search_with_copies(self):
        """Test searching includes copied files."""
        self.storage.file_upload("Original.txt", "150kb")
        self.storage.file_copy("Original.txt", "Copy.txt")
        result = self.storage.file_search("C")
        self.assertEqual(result, "found [Copy.txt]")

    @timeout(0.4)
    def test_level_2_case_07_search_case_sensitive(self):
        """Test that search is case-sensitive."""
        self.storage.file_upload("apple.txt", "100kb")
        self.storage.file_upload("Apple.txt", "200kb")
        result = self.storage.file_search("a")
        self.assertEqual(result, "found [apple.txt]")

    @timeout(0.4)
    def test_level_2_case_08_search_multiple_prefixes(self):
        """Test searching with different prefixes."""
        self.storage.file_upload("Alpha.txt", "100kb")
        self.storage.file_upload("Beta.txt", "200kb")
        self.storage.file_upload("Gamma.txt", "300kb")
        self.assertEqual(self.storage.file_search("A"), "found [Alpha.txt]")
        self.assertEqual(self.storage.file_search("B"), "found [Beta.txt]")
        self.assertEqual(self.storage.file_search("G"), "found [Gamma.txt]")

    @timeout(0.4)
    def test_level_2_case_09_search_same_size_files(self):
        """Test searching with files of the same size."""
        self.storage.file_upload("File1.txt", "100kb")
        self.storage.file_upload("File2.txt", "100kb")
        self.storage.file_upload("File3.txt", "100kb")
        result = self.storage.file_search("File")
        # Files with same size should maintain some consistent order
        self.assertIn("File1.txt", result)
        self.assertIn("File2.txt", result)
        self.assertIn("File3.txt", result)

    @timeout(0.4)
    def test_level_2_case_10_search_after_operations(self):
        """Test searching after various operations."""
        self.storage.file_upload("Data1.csv", "500kb")
        self.storage.file_upload("Data2.csv", "300kb")
        self.storage.file_copy("Data1.csv", "Data3.csv")
        result = self.storage.file_search("Data")
        self.assertEqual(result, "found [Data1.csv, Data3.csv, Data2.csv]")


if __name__ == '__main__':
    unittest.main()
