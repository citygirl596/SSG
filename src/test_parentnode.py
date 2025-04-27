import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        print("==================================================")
        print("Testing the parent_to_html method")
        print("==================================================")

        # Parent with one child
        child_node = LeafNode("span", "child")
        parentnode = ParentNode("div", [child_node])
        actual = parentnode.to_html()
        expected = "<div><span>child</span></div>"
        print(f"Actual:   {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

        # Parent with grandchildren
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        actual = parent_node.to_html()
        expected = "<div><span><b>grandchild</b></span></div>"
        print(f"Actual:   {actual}")
        print(f"Expected: {expected}")
        print("=====================")
        self.assertEqual(actual, expected)

    def test_parent_with_multiple_children(self):
        parent = ParentNode(
            "ul",
            [
                LeafNode("li", "Item 1"),
                LeafNode("li", "Item 2"),
                LeafNode("li", "Item 3")
            ]
        )
        self.assertEqual(parent.to_html(), "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>")

    def test_parent_with_properties(self):
        parent = ParentNode(
            "div",
            [LeafNode("p", "Hello")],
            {"class": "container", "id": "main"}
        )
        self.assertEqual(parent.to_html(), '<div class="container" id="main"><p>Hello</p></div>')

    def test_multiple_nesting_levels(self):
        innermost = LeafNode("span", "Text")
        inner = ParentNode("div", [innermost], {"class": "inner"})
        middle = ParentNode("section", [inner])
        outer = ParentNode("article", [middle], {"id": "content"})

        self.assertEqual(
            outer.to_html(),
            '<article id="content"><section><div class="inner"><span>Text</span></div></section></article>'
        )

    def test_mixed_children_types(self):
        children = [
            LeafNode(None, "Plain text"),
            ParentNode("p", [LeafNode("em", "Emphasized")]),
            LeafNode("br", ""),  # Empty string as value
            LeafNode("span", "More text")
        ]

        parent = ParentNode("div", children)

        actual = parent.to_html()
        expected = "<div>Plain text<p><em>Emphasized</em></p><br></br><span>More text</span></div>"

        print(f"Actual output: {repr(actual)}")
        print(f"Expected output: {repr(expected)}")

        # This should clarify which is which
        self.assertEqual(
            actual,  # What your code produces
            expected  # What you expect it to produce
        )

