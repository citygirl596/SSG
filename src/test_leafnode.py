import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        print("==================================================")
        print("Testing the leaf_to_html method")
        print("==================================================")
        # Paragraph tag
        node = LeafNode("p", "Hello, world!")
        actual = node.to_html()
        expected = "<p>Hello, world!</p>"
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # Div tag
        node = LeafNode("div", "This is a div")
        actual = node.to_html()
        expected = "<div>This is a div</div>"
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # Span tag
        node = LeafNode("span", "Inline text")
        actual = node.to_html()
        expected = "<span>Inline text</span>"
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # h1 tag
        node = LeafNode("h1", "Main Heading")
        actual = node.to_html()
        expected = "<h1>Main Heading</h1>"
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # self closing tag img
        node = LeafNode("img", "Image description", {"src": "image.jpg", "alt": "A sample image"})
        actual = node.to_html()
        expected = '<img src="image.jpg" alt="A sample image">Image description</img>'
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # tag with a property - a
        node = LeafNode("a", "Visit our site", {"href": "https://example.com", "target": "_blank"})
        actual = node.to_html()
        expected = '<a href="https://example.com" target="_blank">Visit our site</a>'
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # tag with a property - button
        node = LeafNode("button", "Click me", {"type": "submit", "class": "btn-primary"})
        actual = node.to_html()
        expected = '<button type="submit" class="btn-primary">Click me</button>'
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # plain text
        node = LeafNode(None, "Just plain text")
        actual = node.to_html()
        expected = "Just plain text"
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # pre
        node = LeafNode("pre", "  Formatted  text  ", {"class": "code"})
        actual = node.to_html()
        expected = '<pre class="code">  Formatted  text  </pre>'
        print(f"Actual: {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

    def test_eq(self):
        test_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        print("==================================================")
        print("Checking for equality")
        print("==================================================")

        node = LeafNode(tag="p", value="Oh dear what can the matter be", props=test_dict)
        node2 = LeafNode(tag="p", value="Oh dear what can the matter be", props=test_dict)
        print(node)
        print(node2)
        print("============================")
        self.assertEqual(node, node2)

    def test_leaf_node_raises_value_error_when_value_is_none(self):
        print("==================================================")
        print("Testing ValueError when value is None")
        print("==================================================")

        node = LeafNode("p", None)

        # This is the correct way to test for exceptions
        with self.assertRaises(ValueError):
            node.to_html()

        print("ValueError was correctly raised as expected")
        print("=====================")

