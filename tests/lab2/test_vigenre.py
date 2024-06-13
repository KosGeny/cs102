import unittest

from src.lab2.vigenre import *


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere('hello', 'a'), 'hello')
        self.assertEqual(encrypt_vigenere('HELLO', 'A'), 'HELLO')
        self.assertEqual(encrypt_vigenere('abc', 'D'), 'def')
        self.assertEqual(encrypt_vigenere("ABC", "Bb"), 'BCD')
        self.assertEqual(encrypt_vigenere('xyz2-3', 'ITMO'), 'frl2-3')
        self.assertEqual(encrypt_vigenere('52', 'SPB'), '52')
        self.assertEqual(encrypt_vigenere('', 'kot'), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_vigenere('hello', 'a'), 'hello')
        self.assertEqual(decrypt_vigenere('HELLO', 'A'), 'HELLO')
        self.assertEqual(decrypt_vigenere('def', 'D'), 'abc')
        self.assertEqual(decrypt_vigenere("BCD", "Bb"), 'ABC')
        self.assertEqual(decrypt_vigenere('frl2-3', 'ITMO'), 'xyz2-3')
        self.assertEqual(decrypt_vigenere('52', 'SPB'), '52')
        self.assertEqual(decrypt_vigenere('', 'kot'), '')

if __name__ == '__main__':
    unittest.main()