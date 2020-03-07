from path import Path
from unittest import TestCase
from PathHolder import PathHolder


class TestPathHolder(TestCase):
    def test_one_script_one_verification(self):
        path_holder = PathHolder(self.get_path("one script one verification"))
        self.assertEqual(len(path_holder.script_names), 1)
        self.assertEqual(len(path_holder.verification_script_names), 1)

    def test_two_script_one_verification(self):
        path_holder = PathHolder(self.get_path("two script one verification"))
        self.assertEqual(len(path_holder.script_names), 2)
        self.assertEqual(len(path_holder.verification_script_names), 1)

    def get_path(self, path):
        return Path("./unit test files/"+path)

if __name__ == '__main__':
    unittest.main()