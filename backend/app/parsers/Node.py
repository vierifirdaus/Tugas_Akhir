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

        # Improved regex to handle complex attributes
        match = re.match(r'^\s*([a-zA-Z_]\w*|\d+)\s*\[(.*)\]', input_str.strip(), re.DOTALL)
        if not match:
            raise ValueError(f"Invalid node string: {input_str}")
        
        self.name = match.group(1)
        attr_str = match.group(2)
        
        # Handle the label separately first
        label_match = re.search(r'label="(.*?)"(?=(?:\s*[,\]]))', attr_str, re.DOTALL)
        if label_match:
            self.label = label_match.group(1)
            # Remove the label part from attr_str to prevent double parsing
            attr_str = attr_str[:label_match.start()] + attr_str[label_match.end():]
        
        # Parse remaining attributes
        attrs = AttributeParser.parse(attr_str)

        self.fillcolor = attrs.get("fillcolor")
        self.height = attrs.get("height")
        # Only set label if not already set from the special handling
        if self.label is None:
            self.label = attrs.get("label")
        self.pos = attrs.get("pos")
        self.shape = attrs.get("shape")
        self.style = attrs.get("style")
        self.width = attrs.get("width")

    def __str__(self):
        return f"Node(name={self.name}, fillcolor={self.fillcolor}, height={self.height}, label={self.label}, pos={self.pos}, shape={self.shape}, style={self.style}, width={self.width})"

    def graphViz(self):
        attrs = []
        
        if self.fillcolor is not None:
            attrs.append(f'fillcolor="{self.fillcolor}"')
        if self.height is not None:
            attrs.append(f'height={self.height}')
        if self.label is not None:
            # Preserve the original label formatting including \l and quotes
            label = self.label
            attrs.append(f'label="{label}"')
        if self.pos is not None:
            if isinstance(self.pos, (list, tuple)):
                strPos = ",".join(map(str, self.pos))
            else:
                strPos = str(self.pos)
            attrs.append(f'pos="{strPos}"')
        if self.shape is not None:
            attrs.append(f'shape={self.shape}')
        if self.style is not None:
            if isinstance(self.style, (list, tuple)):
                strStyle = ",".join(map(str, self.style))
            else:
                strStyle = str(self.style)
            attrs.append(f'style="{strStyle}"')
        if self.width is not None:
            attrs.append(f'width={self.width}')
        
        if attrs:
            return f'{self.name} [{", ".join(attrs)}]'
        return f'{self.name}'
# input = r"""9 [fillcolor="#FFFB81", height=1.0694, label="\"\"\"Metode khusus untuk ...\"\"\"\linterest = self.balance * self.interest_rate\lself.balance += interest\lprint(f'Interest of {interes...')\l", pos="2373.6,367.5", shape=rectangle, style="filled,solid", width=3.7639]; """
# node = Node(input)
# print(node.graphViz())