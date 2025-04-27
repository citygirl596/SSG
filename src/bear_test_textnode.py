import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        test_cases = [
            ("This is a text node", TextType.BOLD, None),
            ("This is an image node", TextType.IMAGE, None),
            ("This is a link node", TextType.LINK, "www.google.com")
        ]
        print("====================================")
        print("Now running self.assertEqual tests")
        print("====================================")

        for text, text_type, url in test_cases:

            with self.subTest(text=text, text_type=text_type, url=url):
                node1 = TextNode(text, text_type, url)
                node2 = TextNode(text, text_type, url)
                print(f"Testing node1: {node1} and node2: {node2}", end=" - ")
                try:
                    self.assertEqual(node1, node2)
                    print("PASSED")
                except AssertionError:
                    print("FAILED")
                    # Re-raise the exception to make the test fail
                    raise


    def test_not_eq(self):
        test_cases = [
            (TextNode("Text 1", TextType.BOLD), TextNode("Text 2", TextType.BOLD)),
            (TextNode("Same text", TextType.BOLD), TextNode("Same text", TextType.ITALIC)),
            (TextNode("URL text", TextType.LINK, "google.com"), TextNode("URL text", TextType.LINK, None)),
        ]
        print("====================================")
        print("Now running self.assertNotEqual tests")
        print("====================================")

        for node1, node2 in test_cases:
            print(f"Testing node1: {node1} and node2: {node2}", end=" - ")
            with self.subTest(node1=node1, node2=node2):
                try:
                    self.assertNotEqual(node1, node2)
                    print("PASSED")
                except AssertionError:
                    print("FAILED")
                    # Re-raise the exception to make the test fail
                    raise


if __name__ == "__main__":
    unittest.main(verbosity=2)

