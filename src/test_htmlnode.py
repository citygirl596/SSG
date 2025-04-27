import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test_dict = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        print("==================================================")
        print("Checking for equality")
        print("==================================================")

        node = HTMLNode(tag="p", value="Oh dear what can the matter be", props=test_dict)
        node2 = HTMLNode(tag="p", value="Oh dear what can the matter be", props=test_dict)
        print(node)
        print(node2)
        print("============================")
        self.assertEqual(node, node2)

        node = HTMLNode(tag="a", value="Oh dear what can the matter be", props=test_dict)
        node2 = HTMLNode(tag="a", value="Oh dear what can the matter be", props=test_dict)
        print(node)
        print(node2)
        print("============================")
        self.assertEqual(node, node2)

        node = HTMLNode(tag="h1", value="Big heading")
        node2 = HTMLNode(tag="h1", value="Big heading")
        print(node)
        print(node2)
        print("============================")
        self.assertEqual(node, node2)


    def test_not_eq(self):
        test_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        print("==================================================")
        print("Checking that these are NOT equal")
        print("==================================================")

        node = HTMLNode(tag="p", value="Oh dear what can the matter be", props=test_dict)
        node2 = HTMLNode(tag="p", value="Oh dear what can the matter be")
        print(node)
        print(node2)
        print("============================")
        self.assertNotEqual(node, node2)

        node = HTMLNode(tag="a", value="Oh dear what can the matter be", props=test_dict)
        node2 = HTMLNode(tag="a", value="Oh dear what can the matter be")
        print(node)
        print(node2)
        print("============================")
        self.assertNotEqual(node, node2)

        node = HTMLNode(tag="h1", value="Big heading")
        node2 = HTMLNode(tag="h1", value="Bigger heading")
        print(node)
        print(node2)
        print("============================")
        self.assertNotEqual(node, node2)


    def testing_props_to_html_method(self):
        test_dict = {
        "href": "https://www.google.com",
        "target": "_blank",
        }

        expected_output = ' href="https://www.google.com" target="_blank"'
        print("==================================================")
        print("Testing the props_to_html method")
        print("==================================================")
        node = HTMLNode(tag="a", value="Oh dear what can the matter be", props=test_dict)
        return_value = node.props_to_html()

        print(f"Expected: {expected_output}")
        print(f"Actual  : {return_value}")

        self.assertEqual(return_value, expected_output)


if __name__ == "__main__":
    unittest.main()

