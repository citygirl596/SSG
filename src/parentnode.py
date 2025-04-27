from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")

        if self.children is None:
            raise ValueError("All parent nodes must have children")

        attributes = ""
        if self.props:
            for key, value in self.props.items():
                attributes += f' {key}="{value}"'

        # Process children and collect their HTML
        children_html = ""
        for child in self.children:
            children_html += child.to_html()  # Call to_html on each child

        # Return the complete HTML with children nested inside
        return f"<{self.tag}{attributes}>{children_html}</{self.tag}>"

