import re
from .AttributeParser import AttributeParser

class NodeLabel:
    def __init__(self,input_str):
        self.fontname = None
        self.label = None
        self.color = None
        start = input_str.find("[") + 1
        end = input_str.find("]")
        attr_str = input_str[start:end].strip()
        attrs = AttributeParser.parse(attr_str)
        self.fontname = attrs.get("fontname", "DejaVu Sans Mono")
        self.label = attrs.get("label", None)
        # saya ingin mengganti pada label " menjadi '
        if self.label is not None:
            self.label = self.label.replace('"', "'")

    def __str__(self):
        return f"NodeLabel(fontname={self.fontname}, label={self.label}, color={self.color})"
    def addAttribute(self, key, value):
        setattr(self, key, value)
    def graphViz(self):
        attrs = []

        if self.fontname is not None:
            attrs.append(f'fontname="{self.fontname}"')
        if self.label is not None:
            attrs.append(f'label="{self.label}"')
        if self.color is not None:
            attrs.append(f'color="{self.color}"')
        
        if attrs :
            return f'node [{", ".join(attrs)}]'
        return ""
# # Example usage
# input = r"""node [fontname="DejaVu Sans Mono" style="rounded,filled"]"""
# node_label = NodeLabel(input)
# # node_label.addAttribute("color", "red")
# print(node_label.graphViz())  # Output: NodeLabel(fontname=DejaVu Sans Mono, label=\N)
