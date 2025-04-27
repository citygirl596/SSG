import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        test_cases = [
            ("This is a text node", TextType.BOLD, None),
            ("This is an image node", TextType.IMAGE, None),
            ("This is a link node", TextType.LINK, "www.google.com")
        ]

        for text, text_type, url in test_cases:
            with self.subTest(f"{text}, {text_type}, {url}"):
                node1 = TextNode(text, text_type, url)
                node2 = TextNode(text, text_type, url)
                self.assertEqual(node1, node2)

    def test_not_eq(self):
        test_cases = [
            (TextNode("Text 1", TextType.BOLD), TextNode("Text 2", TextType.BOLD), "different text"),
            (TextNode("Same text", TextType.BOLD), TextNode("Same text", TextType.ITALIC), "different type"),
            (TextNode("URL text", TextType.LINK, "google.com"), TextNode("URL text", TextType.LINK, None),
             "different URL")
        ]

        for node1, node2, description in test_cases:
            with self.subTest(description):
                self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    # Create a test suite manually
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTextNode)
    # Run with explicit verbosity
    unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == "__main__":
#     unittest.main(verbosity=2)