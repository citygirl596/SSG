from textnode import TextNode, TextType

def main():
    plain = TextNode("oh how plain this is", TextType.NORMAL)
    print(plain)

    link = TextNode("This is some anchor text", TextType.LINK, "google.com")
    print(link)

    image = TextNode("This is some anchor text", TextType.IMAGE, "google.com")
    print(image)

    # Testing the __eq__ method
    node1 = TextNode("same text", TextType.BOLD)
    node2 = TextNode("same text", TextType.BOLD)
    node3 = TextNode("different text", TextType.BOLD)

    print(f"node1 == node2: {node1 == node2}")  # Should be True
    print(f"node1 == node3: {node1 == node3}")  # Should be False

    # Testing with URL
    link1 = TextNode("anchor", TextType.LINK, "example.com")
    link2 = TextNode("anchor", TextType.LINK, "example.com")
    link3 = TextNode("anchor", TextType.LINK, "different.com")

    print(f"link1 == link2: {link1 == link2}")  # Should be True
    print(f"link1 == link3: {link1 == link3}")  # Should be False


if __name__ == "__main__":
        main()

