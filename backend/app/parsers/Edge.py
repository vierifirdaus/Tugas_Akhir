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

        edge_pattern = r'(?:[A-Za-z0-9_]+\s*->\s*[A-Za-z0-9_]+\s*\[(?:[^"[\]]|"[^"]*"|\[.*?\])*?\](?:\s*;)?)' # Edges
        match = re.match(edge_pattern, processed_str, re.DOTALL)
        
        if not match:
            raise ValueError(f"Invalid edge string: {input_str}")
        space_split = processed_str.split(" ") 
        self.source = space_split[0]  # The source node
        self.target = space_split[2]  # The target node

        attrs = AttributeParser.parse(processed_str)
        self.pos = attrs.get("pos")
        self.style = attrs.get("style")
        self.color = attrs.get("color")
        self.label = attrs.get("label")
        if self.label is not None:
            temp_label = ""
            if isinstance(self.label, list):
                for i in self.label :
                    if i == "\l":
                        temp_label += "\\l"
                    else:
                        temp_label += i 
                self.label = temp_label.replace('"', "'")
            else : 
                self.label = self.label.replace('"', "'")
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