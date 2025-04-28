import re
from AttributeParser import AttributeParser

class Edge:
    def __init__(self, input_str):
        match = re.match(r'(\d+)\s*->\s*(\d+)\s*\[(.*)\]', input_str.strip(), re.DOTALL)
        if not match:
            raise ValueError(f"Invalid edge string: {input_str}")
        self.source = match.group(1)
        self.target = match.group(2)
        attr_str = match.group(3)
        self.attrs = AttributeParser.parse(attr_str)

    def __str__(self):
        return f"Edge(source={self.source}, target={self.target}, " + ", ".join(f"{k}={v}" for k, v in self.attrs.items()) + ")"