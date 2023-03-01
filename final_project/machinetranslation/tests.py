import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest, TestCase):
     def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)

class TestFrenchToEnglish(unittest, TestCase):
     def test1(self):
        self.assertEqual(english_to_french('Bonjour'), 'Hello')
        self.assertNotEqual(english_to_french('Bonjour'), 'Bonjour')
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)