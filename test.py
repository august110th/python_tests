import unittest
from yandex import NewFolder, token

class FolderCreate(unittest.TestCase):

    def setUp(self):
        self.fc = NewFolder(token)

    def test_folder_create(self):
        self.assertEqual(self.fc.folder_create("new_folder"), 201)

    def test_folder_check(self):
        self.assertEqual(self.fc.folder_check("new_folder"), 200)

if __name__ == '__main__':
    unittest.main()