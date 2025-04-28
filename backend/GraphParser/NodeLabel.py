import re
from AttributeParser import AttributeParser

class NodeLabel:
    def __init__(self, fontname="", label="\\N"):
        self.fontname = fontname
        self.label = label

    def __str__(self):
        return f"NodeLabel(fontname={self.fontname}, label={self.label})"

    @classmethod
    def from_str(cls, input_str):
        match = re.search(r'\[(.*?)\]', input_str, re.DOTALL)
        attrs = {}
        if match:
            content = match.group(1)
            for pair in re.split(r',\s*', content):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    attrs[k.strip()] = v.strip().strip('"')
        return cls(**attrs)