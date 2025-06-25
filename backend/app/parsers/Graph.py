import re
from .AttributeParser import AttributeParser

class Graph:
    def __init__(self, input_str):
        self.bb = None
        self.compound = None
        self.fontname = None
        self.label = None
        self.lheight = None
        self.lp = None
        self.lwidth = None
        self.pack = None
        self.rankdir = None
        self.ranksep = None
        self.color = None
        self.style = None
        self.shape = None

        attrs = AttributeParser.parse(input_str.strip())


        self.bb = attrs.get("bb")
        self.compound = attrs.get("compound")
        self.fontname = attrs.get("fontname")
        self.label = attrs.get("label")
        self.lheight = attrs.get("lheight")
        self.lp = attrs.get("lp")
        self.lwidth = attrs.get("lwidth")
        self.pack = attrs.get("pack")
        self.rankdir = attrs.get("rankdir")
        self.ranksep = attrs.get("ranksep")
        self.color = attrs.get("color")
        self.style = attrs.get("style")
        self.shape = attrs.get("shape")
        if self.label is not None :
            if(len(self.label)>1) : 
                if(self.label[0:3] == 'cfg') : 
                    self.label = 'Main'
        if self.label is not None:
            self.label = self.label.replace('"', "'")

    def __str__(self):
        return f"Graph(bb={self.bb}, compound={self.compound}, fontname={self.fontname}, label={self.label}, lheight={self.lheight}, lp={self.lp}, lwidth={self.lwidth}, pack={self.pack}, rankdir={self.rankdir}, ranksep={self.ranksep}, color={self.color}, style={self.style}, shape={self.shape})"
    def graphViz(self):
        attrs = []
        
        if self.bb is not None:
            attrs.append(f'bb="{self.bb}"')
        if self.compound is not None:
            attrs.append(f'compound={str(self.compound).lower()}')
        if self.fontname is not None:
            attrs.append(f'fontname="{self.fontname}"')
        if self.label is not None:
            attrs.append(f'label="{self.label}"')
        if self.lheight is not None:
            attrs.append(f'lheight={self.lheight}')
        if self.lp is not None:
            attrs.append(f'lp="{self.lp}"')
        if self.lwidth is not None:
            attrs.append(f'lwidth={self.lwidth}')
        if self.pack is not None:
            attrs.append(f'pack={str(self.pack).lower()}')
        if self.rankdir is not None:
            attrs.append(f'rankdir={self.rankdir}')
        if self.ranksep is not None:
            attrs.append(f'ranksep={self.ranksep}')
        if self.color is not None:
            attrs.append(f'color="{self.color}"')
        if self.style is not None:
            attrs.append(f'style="{self.style}"')
        if self.shape is not None:
            attrs.append(f'shape={self.shape}')
        if attrs:
            return f'graph [{", ".join(attrs)}]'
        return ''
    