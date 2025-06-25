import re
from .AttributeParser import AttributeParser

class Node:
    def __init__(self, input_str):
        self.name = None
        self.fillcolor = None
        self.height = None
        self.label = None
        self.pos = None
        self.shape = None
        self.style = None
        self.width = None
        self.color = None
        self.label = None

        # Improved regex to handle complex attributes
        input_str = input_str.strip()
        input_str = input_str.replace("\t"," ")
        input_str = input_str
        attrs = AttributeParser.parse(input_str)

        space_split = input_str.split(" ")
        self.name = space_split[0]
        self.fillcolor = attrs.get("fillcolor", None)
        self.height = attrs.get("height", None)
        self.label = attrs.get("label", None)
        self.pos = attrs.get("pos", None)
        self.shape = attrs.get("shape", None)
        self.style = attrs.get("style", None)
        self.width = attrs.get("width", None)
        self.color = attrs.get("color", None)
        self.label = attrs.get("label", None)


    def __str__(self):
        return f"Node(name={self.name}, fillcolor={self.fillcolor}, height={self.height}, label={self.label}, pos={self.pos}, shape={self.shape}, style={self.style}, width={self.width}, color={self.color})"

    def graphViz(self):
        attrs = []
        
        if self.fillcolor is not None:
            attrs.append(f'fillcolor="{self.fillcolor}"')
        if self.height is not None:
            attrs.append(f'height={self.height}')
        if self.label is not None:
            attrs.append(f'label="{self.label}"')
        if self.pos is not None:
            attrs.append(f'pos="{self.pos}"')
        if self.shape is not None:
            attrs.append(f'shape={self.shape}')
        if self.style is not None:
            attrs.append(f'style="{self.style}"')
        if self.width is not None:
            attrs.append(f'width={self.width}')
        if self.color is not None:
            attrs.append(f'color="{self.color}"')
        
        if attrs:
            return f'{self.name} [{", ".join(attrs)}]'
        return f'{self.name}'