import re
from AttributeParser import AttributeParser

class Graph:
    def __init__(self, **kwargs):
        # Menambahkan atribut color
        self.bb = kwargs.get("bb")
        self.compound = kwargs.get("compound", False)
        self.fontname = kwargs.get("fontname", "")
        self.label = kwargs.get("label", "")
        self.lheight = kwargs.get("lheight", 0)
        self.lp = kwargs.get("lp")
        self.lwidth = kwargs.get("lwidth", 0)
        self.pack = kwargs.get("pack", False)
        self.rankdir = kwargs.get("rankdir", "TB")
        self.ranksep = kwargs.get("ranksep", 0)
        # Atribut color
        self.color = kwargs.get("color", None)

    def __str__(self):
        return f"Graph(bb={self.bb}, compound={self.compound}, fontname={self.fontname}, label={self.label}, lheight={self.lheight}, lp={self.lp}, lwidth={self.lwidth}, pack={self.pack}, rankdir={self.rankdir}, ranksep={self.ranksep}, color={self.color})"

    @classmethod
    def from_str(cls, input_str):
        start = input_str.find("[") + 1
        end = input_str.find("]")
        attr_str = input_str[start:end].strip()
        return cls(**AttributeParser.parse(attr_str))