import re
from .AttributeParser import AttributeParser

class Edge:
    def __init__(self, input_str):
        self.source = None
        self.target = None
        self.direction = None  
        self.pos = None
        self.style = None
        self.color = None
        self.label = None
        self.lp = None
        self.direction = "->"  
        processed_str = ' '.join(input_str.strip().split())
        temp_str = processed_str.replace("\t"," ")
        space_split = temp_str.split("->") 
        self.source = space_split[0]  
        for item in space_split[1].split(" ") :
            if item not in ['',None] :
                self.target = item 
                break

        attrs = AttributeParser.parse(processed_str)
        self.pos = attrs.get("pos")
        self.style = attrs.get("style")
        self.color = attrs.get("color")
        self.label = attrs.get("label")
        if self.label is not None:
            temp_label = ""
            if isinstance(self.label, list):
                for i in self.label :
                    temp_label+=i
                self.label = temp_label.replace('"', "'")
            else : 
                self.label = self.label.replace('"', "'")
        self.lp = attrs.get("lp")

    def __str__(self):
        return f"Edge(source={self.source}, target={self.target}, pos={self.pos}, style={self.style}, color={self.color}, label={self.label}, lp={self.lp})"
    
    def graphViz(self):
        attrs = []
        if self.pos is not None:
            attrs.append(f'pos="{self.pos}"')
        if self.style is not None:
            attrs.append(f'style="{self.style}"')
        if self.color is not None:
            attrs.append(f'color="{self.color}"')
        if self.label is not None:
            attrs.append(f'label="{self.label}"')
        if self.lp is not None:
            attrs.append(f'lp="{self.lp}"')
        return f"{self.source} {self.direction} {self.target} [{', '.join(attrs)}]"
# input_str = r"""
# input -> call	[pos="e,323,138.73 323,187.5 323,176.67 323,162.45 323,149.98",
# 			style=invis];"""
# try:
#     edge = Edge(input_str)
#     print(edge)  
# except ValueError as e:
#     print(f"Error: {e}")