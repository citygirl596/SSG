from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        attributes = ""

        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value

        if self.props:
            for key, value in self.props.items():
                attributes += f' {key}="{value}"'

        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
