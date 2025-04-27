### The code below uses parameters to run the test scripts as sub-tests.  This means that if a sub-test fails the
# rest of the tests will still run.


import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        test_cases = [
            ("This is a text node", TextType.BOLD, None),
            ("This is an image node", TextType.IMAGE, None),
            ("This is a link node", TextType.LINK, "www.google.com"),
        ]

        for text, text_type, url in test_cases:
            with self.subTest(text=text, text_type=text_type, url=url):
                node1 = TextNode(text, text_type, url)
                node2 = TextNode(text, text_type, url)
                self.assertEqual(node1, node2)

    def test_not_eq(self):
        test_cases = [
            # Different text
            (TextNode("Text 1", TextType.BOLD), TextNode("Text 2", TextType.BOLD)),
            # Different type
            (TextNode("Same text", TextType.BOLD), TextNode("Same text", TextType.ITALIC)),
            # Different URL
            (TextNode("URL text", TextType.LINK, "google.com"), TextNode("URL text", TextType.LINK, None)),
        ]

        for node1, node2 in test_cases:
            with self.subTest(node1=node1, node2=node2):
                self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()