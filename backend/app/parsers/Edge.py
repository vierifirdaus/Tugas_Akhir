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

        processed_str = ' '.join(input_str.strip().split())

        edge_pattern = r'^\s*([a-zA-Z_]\w*|\d+)\s*(->|--)\s*([a-zA-Z_]\w*|\d+)(?:\s*\[(.*?)\])?\s*;?\s*$'
        match = re.match(edge_pattern, processed_str, re.DOTALL)
        
        if not match:
            raise ValueError(f"Invalid edge string: {input_str}")
                
        self.source = match.group(1)
        self.direction = match.group(2)  # Store the direction
        self.target = match.group(3)

        if match.group(4):
            attrs = AttributeParser.parse(match.group(4))
            self.pos = attrs.get("pos")
            self.style = attrs.get("style")
            self.color = attrs.get("color")
            self.label = attrs.get("label")
            self.lp = attrs.get("lp")

    def __str__(self):
        return f"Edge(source={self.source}, target={self.target}, pos={self.pos}, style={self.style}, color={self.color}, label={self.label}, lp={self.lp})"
    
    def graphViz(self):
        attrs = []
        if self.pos is not None:
            strPos = ""
            lenStrPos = len(self.pos)
            for i in range(lenStrPos):
                if i == 0:
                    strPos += str(self.pos[i])
                else:
                    strPos += "," + str(self.pos[i])
            attrs.append(f'pos="{strPos}"')
        if self.style is not None:
            strStyle = ""
            lenStrStyle = len(self.style)
            if isinstance(self.style, str):
                attrs.append(f'style="{self.style}"')
            else:
                for i in range(lenStrStyle):
                    if i == 0:
                        strStyle += str(self.style[i])
                    else:
                        strStyle += "," + str(self.style[i])
                attrs.append(f'style="{strStyle}"')
        if self.color is not None:
            attrs.append(f'color="{self.color}"')
        if self.label is not None:
            attrs.append(f'label="{self.label}"')
        if self.lp is not None:
            strLp = ""
            lenStrLp = len(self.lp)
            for i in range(lenStrLp):
                if i == 0:
                    strLp += str(self.lp[i])
                else:
                    strLp += "," + str(self.lp[i])
            attrs.append(f'lp="{strLp}"')
        
        return f"{self.source} {self.direction} {self.target} [{', '.join(attrs)}]"
# input_str = r"""
# input -> call	[pos="e,323,138.73 323,187.5 323,176.67 323,162.45 323,149.98",
# 			style=invis];"""
# try:
#     edge = Edge(input_str)
#     print(edge)  
# except ValueError as e:
#     print(f"Error: {e}")