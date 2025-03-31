import unittest
from PyPoetryDB.PoetryDB import API

class TestAPI(unittest.TestCase):
    def test_list_authors(self):
        api = API()
        authors = api.list_authors()
        self.assertIsInstance(authors, list)  # Verifica que sea una lista

if __name__ == "__main__":
    unittest.main()