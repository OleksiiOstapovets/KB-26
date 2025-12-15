import unittest

from task3 import (AES,AESModeOfOperationCTR,AESModeOfOperationCBC)

class TestAESCore(unittest.TestCase):

    def test_encrypt_decrypt_block(self):
        key = b"this_key_16_demo"
        aes = AES(key)

        block = b"\x00" * 16
        encrypted = aes.encrypt(block)
        decrypted = aes.decrypt(encrypted)

        self.assertEqual(block, bytes(decrypted)) # Чи зашифрований та розшифрований співпадає з оригіналом

    def test_different_keys_produce_different_ciphertext(self):
        block = b"\x01" * 16

        aes1 = AES(b"this_key_16_demo")
        aes2 = AES(b"this_key_16_test")

        c1 = aes1.encrypt(block)
        c2 = aes2.encrypt(block)

        self.assertNotEqual(c1, c2)

    def test_same_key_same_plaintext_same_ciphertext(self):
        key = b"this_key_16_demo"
        block = b"ABCDEFGHIJKLMNOP"

        aes1 = AES(key)
        aes2 = AES(key)

        self.assertEqual(
            aes1.encrypt(block),
            aes2.encrypt(block)
        )


class TestAESCTRMode(unittest.TestCase):

    def test_ctr_encrypt_decrypt(self):
        key = b"this_key_16_demo"
        plaintext = b"Hello World!!!"

        aes = AESModeOfOperationCTR(key)
        ciphertext = aes.encrypt(plaintext)

        aes_dec = AESModeOfOperationCTR(key)
        decrypted = aes_dec.decrypt(ciphertext)

        self.assertEqual(plaintext, decrypted)

    def test_ctr_accepts_any_length(self):
        key = b"this_key_16_demo"

        data = b"A" * 37  # НЕ кратно 16
        aes = AESModeOfOperationCTR(key)

        encrypted = aes.encrypt(data)

        self.assertEqual(len(encrypted), len(data))


class TestAESCBCMode(unittest.TestCase):
    """Тести режиму CBC"""

    def test_cbc_requires_block_alignment(self):
        key = b"this_key_16_demo"
        aes = AESModeOfOperationCBC(key)

        with self.assertRaises(ValueError):
            aes.encrypt(b"Not 16 bytes")


if __name__ == "__main__":
    unittest.main()
