class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return_string = ""
        for key, value in self.props.items():
            formatted_string = f' {key}="{value}"'
            return_string += formatted_string
        return return_string

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value\
               and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
