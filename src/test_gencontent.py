import unittest

from gencontent import extract_title


class TestGenerateContent(unittest.TestCase):

    def test_extract_title_positive(self):
        markdown = "Bobby\n# Hello"
        actual = extract_title(markdown)
        self.assertEqual(actual, "Hello")

    def test_extract_double_h1(self):
        markdown = "Bobby\nHello\nworlds"
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)

        self.assertTrue('No title found' in str(context.exception))
