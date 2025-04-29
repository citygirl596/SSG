import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.IMAGE, "GOOGLE.com")
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

        node = TextNode("This is some anchor text", TextType.IMAGE, "google.com")
        node2 = TextNode("This is some anchor text", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_tags(self):
        list_of_nodes = [
            (TextNode("oh how plain this is", TextType.TEXT), None),
            (TextNode("same text", TextType.BOLD), "b"),
            (TextNode("same text", TextType.ITALIC), "i"),
            (TextNode("same text", TextType.CODE), "code"),
            (TextNode("This is some link anchor text", TextType.LINK, "google.com"), "a"),
            (TextNode("This is some image anchor text", TextType.IMAGE, "google.com"), "img")
        ]

        for node, expected_tag in list_of_nodes:
            with self.subTest(text = node.text, text_type=node.text_type):
                processed_node = text_node_to_html_node(node)
                self.assertEqual(processed_node.tag, expected_tag)


    def test_values(self):
        list_of_nodes = [
            (TextNode("oh how plain this is", TextType.TEXT), "oh how plain this is"),
            (TextNode("same text", TextType.BOLD), "same text"),
            (TextNode("same text", TextType.ITALIC), "same text"),
            (TextNode("same text", TextType.CODE), "same text"),
            (TextNode("This is some link anchor text", TextType.LINK, "google.com"), "This is some link anchor text"),
            (TextNode("This is some image anchor text", TextType.IMAGE, "google.com"), "")
        ]

        for node, expected_value in list_of_nodes:
            with self.subTest(text = node.text, text_type=node.text_type):
                processed_node = text_node_to_html_node(node)
                self.assertEqual(processed_node.value, expected_value)

    def test_links(self):
        node = TextNode("This is some link anchor text", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is some link anchor text")
        self.assertEqual(html_node.props, {"href": "google.com"})

    def test_link_url_is_none(self):
        node = TextNode("This is some link anchor text", TextType.LINK, None)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is some link anchor text")
        self.assertEqual(html_node.props, {"href": None})

    def test_link_with_special_chars(self):
        url = "https://example.com/search?q=test&lang=en#section"
        node = TextNode("Search results", TextType.LINK, url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Search results")
        self.assertEqual(html_node.props, {"href": url})

    def test_link_with_unicode(self):
        url = "https://例子.测试"  # example.test in Chinese characters
        node = TextNode("Unicode URL", TextType.LINK, url)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Unicode URL")
        self.assertEqual(html_node.props, {"href": url})

    def test_images(self):
        node = TextNode("This is some image anchor text", TextType.IMAGE, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "google.com", "alt": "This is some image anchor text"})

    def test_image_alt_text(self):
        node = TextNode("", TextType.IMAGE, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "google.com", "alt": ""})


if __name__ == "__main__":
    unittest.main()

