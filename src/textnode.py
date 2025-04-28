# TODO next step is to update the tests on images and perhaps links as well to cover off some edge cases suggested
# TODO by Boots.

# Testing with slight updates to see if the commit does in fact reset my streak!

# A thoughtful point! For most cases, what you’re testing is sufficient. But as your program grows, you might consider these possible scenarios:
#
# Different alt texts: Try varied alt text, including empty strings, to see how your function handles them.
# Invalid/missing URLs: What if the url parameter is None, an empty string, or has unexpected characters?
# Long or special characters: What if the alt or url contains special or Unicode characters? Does your code handle them without breaking?
# Extra arguments: What if someone constructs a TextNode with additional or unexpected properties? Does your function only use the ones it’s supposed to?
# Why might it be important to consider unusual or edge-case data, even if your initial input data is always “normal”?



from enum import Enum

from leafnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        print("Text Node is TEXT")
        return_node = LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        print("Text Node is BOLD")
        return_node = LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        print("Text Node is ITALIC")
        return_node = LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        print("Text Node is CODE")
        return_node = LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        print("Text Node is LINK")
        # return_node = LeafNode("a", text_node.text, text_node.url)
        return_node = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        print("Text Node is IMAGE")
        return_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Text Node is not a valid text node type")

    print(f"Result is {return_node}")
    return return_node


def main():
    list_of_nodes = [
        TextNode("oh how plain this is", TextType.TEXT),
        TextNode("same text", TextType.BOLD),
        TextNode("same text", TextType.ITALIC),
        TextNode("same text", TextType.CODE),
        TextNode("This is some link anchor text", TextType.LINK, "google.com"),
        TextNode("This is some image anchor text", TextType.IMAGE, "google.com")
    ]

    for each_node in list_of_nodes:
        processed_node = text_node_to_html_node(each_node)


if __name__ == "__main__":
    main()

    # # Testing the __eq__ method
    # node1 = TextNode("same text", TextType.BOLD)
    # node2 = TextNode("same text", TextType.BOLD)
    # node3 = TextNode("different text", TextType.BOLD)
    #
    # print(f"node1 == node2: {node1 == node2}")  # Should be True
    # print(f"node1 == node3: {node1 == node3}")  # Should be False
    #
    # # Testing with URL
    # link1 = TextNode("anchor", TextType.LINK, "example.com")
    # link2 = TextNode("anchor", TextType.LINK, "example.com")
    # link3 = TextNode("anchor", TextType.LINK, "different.com")
    #
    # print(f"link1 == link2: {link1 == link2}")  # Should be True
    # print(f"link1 == link3: {link1 == link3}")  # Should be False
