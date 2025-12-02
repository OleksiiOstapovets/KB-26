import unittest
from task2 import is_only_digits,is_only_lowercase_letters,is_weak_password, is_special_symbol, is_too_short, from_weak_list
class TestWeakPasswords(unittest.TestCase):
    def test_only_digits(self):
        self.assertTrue(is_only_digits("1233456784560")) # Тести на перевірку, чи складається рядок лише з цифр
        self.assertFalse(is_only_digits("34567b4335aer")) 
        self.assertFalse(is_only_digits(";b433:5a/wgmm.mwl")) 
        
    def test_short(self):
        self.assertTrue(is_too_short("4567g")) # Перевірка, на довжину пароля (мінімум 12 символів)
        self.assertTrue(is_too_short("?nu/324hwrs"))
        self.assertFalse(is_too_short("4567654#u!].5"))
        self.assertFalse(is_too_short("$:fbjowrijb24367].5"))

    def test_only_lowercase_letter(self):
        self.assertFalse(is_only_lowercase_letters("23#46/:ye3;4")) # Перевірка, чи парл містить тільки малі букви
        self.assertFalse(is_only_lowercase_letters("81gb3#fhdgn46/:;4"))
        self.assertFalse(is_only_lowercase_letters("dfbdfnsbL666EDC"))
        self.assertTrue(is_only_lowercase_letters("wndmfkbkdjsvnkenbdkvnskvjnb"))
        
    def test_weak_list(self):
        self.assertTrue(from_weak_list("admin")) # Чи належить пароль до списку слабких паролів
        self.assertTrue(from_weak_list("qwerty"))
        self.assertTrue(from_weak_list("P@ssw0rd"))
        self.assertFalse(from_weak_list("password12345678910"))
        self.assertFalse(from_weak_list(".gfas23"))
        self.assertFalse(from_weak_list("#xbgfm)(*&54)"))
    
    def test_special_symbol(self):
        self.assertTrue(is_special_symbol("egvdbsd4rgwjtemnsb."))# Чи містить спеціальні символи
        self.assertTrue(is_special_symbol("asfvd;bsdsfn4rgwjtemn$sb"))
        self.assertFalse(is_special_symbol("12423657486707879867456345324"))
        self.assertFalse(is_special_symbol("1vsfnsfbfsnedndeg2345vdbsd"))

    def test_weak_password(self):
        self.assertEqual('This password is too short!',is_weak_password("4fnbx/jhmyt")) # Тест головної функції
        self.assertEqual('This password is too weak. It is too popular!',is_weak_password("admin123"))
        self.assertEqual('This password is too weak. It consist only of digits!',is_weak_password("1234567897656432"))
        self.assertEqual('This password is too weak. It consist only of lowercase letters!',is_weak_password("sdgfghdgjfhkgjlhmn"))
        self.assertEqual('This password is good, but you can make it more complicated by adding a special symbol!',is_weak_password("Tr54by2hnv5q"))
        self.assertEqual('This password is good, but you can make it more complicated by adding a special symbol!',is_weak_password("Dgb6nawemobs"))
        self.assertEqual('This password is good enough',is_weak_password("Td5cg/y65bggm"))

if __name__ == "__main__":
    unittest.main()
