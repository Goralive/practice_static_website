import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This text is bold", "bold")
        node2 = TextNode("This text is bold", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This text is bold", "bold", "Some Url")
        node2 = TextNode("This text is bold", "bold")
        self.assertNotEqual(node, node2)
        self.assertEquals(node.url, "Some Url")


if __name__ == "__main__":
    unittest.main
