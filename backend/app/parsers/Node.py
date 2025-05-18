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

        match = re.match(r'^\s*([a-zA-Z_]\w*|\d+)\s*\[(.*)\]', input_str.strip(), re.DOTALL)
        if not match:
            raise ValueError(f"Invalid node string: {input_str}")
        
        self.name = match.group(1)

        attr_str = match.group(2)
        attrs = AttributeParser.parse(attr_str)

        self.fillcolor = attrs.get("fillcolor")
        self.height = attrs.get("height")
        self.label = attrs.get("label")
        self.pos = attrs.get("pos")
        self.shape = attrs.get("shape")
        self.style = attrs.get("style")
        self.width = attrs.get("width")

    def __str__(self):
        return f"Node(name={self.name}, fillcolor={self.fillcolor}, height={self.height}, label={self.label}, pos={self.pos}, shape={self.shape}, style={self.style}, width={self.width})"
    def graphViz(self):
        attrs = []
        
        # Add attributes only if they are set
        if self.fillcolor is not None:
            attrs.append(f'fillcolor="{self.fillcolor}"')
        if self.height is not None:
            attrs.append(f'height={self.height}')
        if self.label is not None:
            resLabel = ""
            lenResLabel = len(self.label)
            if(type(self.label) == str) :
                attrs.append(f'label="{self.label}"')
            else:
                for i in range(lenResLabel):
                    if i==0 :
                        resLabel += str(self.label[i])
                    else :
                        resLabel += " " + str(self.label[i])
                attrs.append(f'label="{resLabel}"')
        if self.pos is not None:
            strPos = ""
            lenStrPos = len(self.pos)
            for i in range(lenStrPos):
                if i==0 :
                    strPos += str(self.pos[i])
                else :
                    strPos += "," + str(self.pos[i])
            attrs.append(f'pos="{strPos}"')
        if self.shape is not None:
            attrs.append(f'shape={self.shape}')
        if self.style is not None:
            strStyle = ""
            lenStrStyle = len(self.style)
            if(type(self.style) == str) :
                attrs.append(f'style="{self.style}"')
            else:
                for i in range(lenStrStyle):
                    if i==0 :
                        strStyle += str(self.style[i])
                    else :
                        strStyle += "," + str(self.style[i])
                attrs.append(f'style="{strStyle}"')
        if self.width is not None:
            attrs.append(f'width={self.width}')
        
        # Format as node declaration
        if attrs:
            return f'{self.name} [{", ".join(attrs)}]'
        return f'{self.name}'
# input = r"""1	[fillcolor="#FFBE52",
# 		height=0.5,
# 		pos="111,283",
# 		shape=hexagon,
# 		style="filled",
#         label="print('Hello, World!')\l",
# 		width=2.8406];"""
# node = Node(input)
# print(node.graphViz())