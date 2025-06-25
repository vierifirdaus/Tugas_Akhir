import re
from .AttributeParser import AttributeParser

class EdgeLabel:
    def __init__(self,input_str):
        self.fontname = None
        self.label = None
        self.color = None
        attrs = AttributeParser.parse(input_str.strip())
        self.fontname = attrs.get("fontname", "DejaVu Sans Mono")
        self.label = attrs.get("label", None)
        if self.label is not None:
            self.label = self.label.replace('"', "'")
        self.color = attrs.get("color", None)

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
            return f'edge [{", ".join(attrs)}]'
        else :
            return ""
# # Example usage
# input = r"""edge [fontname="DejaVu Sans Mono", color="#E552FF"]"""
# edgeLabel = EdgeLabel(input)
# # node_label.addAttribute("color", "red")
# print(edgeLabel.graphViz())  # Output: NodeLabel(fontname=DejaVu Sans Mono, label=\N)
