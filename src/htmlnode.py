class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value for html")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag was provided")
        if self.children is None:
            raise ValueError("No children was provided")
        html = ""
        for child in self.children:
            html += f"{child.to_html()}"
        return f"<{self.tag}>{html}</{self.tag}>"
