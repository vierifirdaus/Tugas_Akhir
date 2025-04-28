import re
from AttributeParser import AttributeParser

class Node:
    def __init__(self, input_str):
        match = re.match(r'(\d+)\s*\[(.*)\]', input_str.strip(), re.DOTALL)
        if not match:
            raise ValueError(f"Invalid node string: {input_str}")
        self.name = match.group(1)
        attr_str = match.group(2)
        self.attrs = AttributeParser.parse(attr_str)

    def __str__(self):
        return f"Node(name={self.name}, " + ", ".join(f"{k}={v}" for k, v in self.attrs.items()) + ")"