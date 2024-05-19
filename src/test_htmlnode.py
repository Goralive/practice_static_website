import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        html_node = HTMLNode()
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_props_to_html(self):
        html_node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        actual = html_node.props_to_html()
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(expected, actual)
        self.assertIsNone(html_node.children)
        self.assertIsNone(html_node.tag)
        self.assertIsNone(html_node.value)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_self_prop_none(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            None,
        )

        self.assertEqual("", node.props_to_html())



if __name__ == "__main__":
    unittest.main
