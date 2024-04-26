import unittest

from src.lab2.caesar import *


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar('hello'), 'khoor')
        self.assertEqual(encrypt_caesar('ITMO'), 'LWPR')
        self.assertEqual(encrypt_caesar('xyz'), 'abc')
        self.assertEqual(encrypt_caesar('xyz2-3'), 'abc2-3')
        self.assertEqual(encrypt_caesar('52'), '52')
        self.assertEqual(encrypt_caesar(''), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar('khoor'), 'hello')
        self.assertEqual(decrypt_caesar('LWPR'), 'ITMO')
        self.assertEqual(decrypt_caesar('abc'), 'xyz')
        self.assertEqual(decrypt_caesar('abc2-3'), 'xyz2-3')
        self.assertEqual(decrypt_caesar('52'), '52')
        self.assertEqual(decrypt_caesar(''), '')

if __name__ == '__main__':
    unittest.main()