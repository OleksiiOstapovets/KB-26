import unittest

from task2 import (
    weak_passwords_list,
    is_only_digits,
    is_only_lowercase_letters,
    is_weak_password,
    find_weak,
)


class TestWeakPasswords(unittest.TestCase):
    def test_weak_list_member(self):
        # pick a known weak password from the list
        self.assertIn("password", weak_passwords_list)
        self.assertTrue(is_weak_password("password"))

    def test_only_digits(self):
        self.assertTrue(is_only_digits("123456"))
        self.assertTrue(is_weak_password("123456"))
        self.assertFalse(is_only_digits("123a"))

    def test_only_lowercase_letters(self):
        self.assertTrue(is_only_lowercase_letters("abcdef"))
        self.assertTrue(is_weak_password("abcdef"))
        self.assertFalse(is_only_lowercase_letters("abcDef"))

    def test_mixed_password_not_weak_by_case_or_digits(self):
        # mixed-case and digits/punctuation should not be flagged by these simple rules
        self.assertFalse(is_only_digits("Abc123"))
        self.assertFalse(is_only_lowercase_letters("Abc123"))
        self.assertFalse(is_weak_password("Abc123"))

    def test_find_weak(self):
        samples = ["password", "goodPass1", "1234", "lowercase", "UPPER", "Ab1!"]
        found = find_weak(samples)
        # expected weak ones: 'password', '1234', 'lowercase'
        self.assertIn("password", found)
        self.assertIn("1234", found)
        self.assertIn("lowercase", found)
        self.assertNotIn("goodPass1", found)


if __name__ == "__main__":
    unittest.main()
