"""Utilities to identify weak passwords.

Provides a `weak_passwords_list` (common weak passwords) and helpers to
detect passwords that are weak because they are in the list, contain only
digits, or contain only lowercase letters.

Functions:
  - is_only_digits(s)
  - is_only_lowercase_letters(s)
  - is_weak_password(pw)
  - find_weak(passwords)
"""

from typing import Iterable, List
weak_passwords_list: List[str] = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "monkey",
    "letmein",
    "dragon",
    "111111",
    "baseball",
]
def is_only_digits(s: str) -> bool:
    """Return True if the string consists only of digits (and non-empty)."""
    return isinstance(s, str) and s.isdigit() and len(s) > 0
def is_only_lowercase_letters(s: str) -> bool:
    """Return True if the string consists only of lowercase letters (and non-empty)."""
    return isinstance(s, str) and s.isalpha() and s.islower() and len(s) > 0
def is_weak_password(pw: str) -> bool:
    """Return True if `pw` is considered weak.
    A password is weak when any of the following is true:
      - exactly matches an entry in `weak_passwords_list` (case-sensitive)
      - contains only digits
      - contains only lowercase letters
    Non-string inputs will be converted to str before checking.
    """
    if not isinstance(pw, str):
        pw = str(pw)
    if pw in weak_passwords_list:
        return True
    if is_only_digits(pw):
        return True
    if is_only_lowercase_letters(pw):
        return True
    return False
def find_weak(passwords: Iterable[str]) -> List[str]:
    """Return a list of passwords from the iterable that are weak."""
    return [pw for pw in passwords if is_weak_password(pw)]
if __name__ == "__main__":
    # Simple demo when run directly
    sample = ["password", "hunter2", "1234", "abcdef", "Abcdef1!"]
    print("Weak passwords from sample:", find_weak(sample))
