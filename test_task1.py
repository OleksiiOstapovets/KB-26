import unittest
import string
from task1 import Creating_password, Difficulty
class Test_Difficulty(unittest.TestCase):
	def test_return_difficulty(self): #Перевірка типу значення
		self.assertIsInstance(Difficulty("easy"), str)
		self.assertIsInstance(Difficulty("medium"), str)
		self.assertIsInstance(Difficulty("hard"), str)

	def test_length_default(self): #Довжина пароля завжди 12 символів
		self.assertEqual(len(Creating_password("easy")), 12)
		self.assertEqual(len(Creating_password("medium")), 12)
		self.assertEqual(len(Creating_password("hard")), 12)

	def test_easy(self):
		pw = Creating_password("easy") #Перевірка символів для легкого рівня
		for ch in pw:
			self.assertTrue(ch.islower() or ch.isdigit(),f"char {ch!r} is not allowed in easy")

	def test_medium(self): #Перевірка символів для середнього рівня
		pw = Creating_password("medium")
		for ch in pw:
			self.assertTrue(ch.isalpha() or ch.isdigit(),f"char {ch!r} is not allowed in medium")

	def test_hard(self): #Перевірка символів для складного рівня
		pw = Creating_password("hard")
		allowed = set(string.ascii_letters + string.digits + string.punctuation)
		for ch in pw:
			self.assertIn(ch, allowed, f"char {ch!r} is not allowed in hard")
			
if __name__ == "__main__":
	unittest.main()