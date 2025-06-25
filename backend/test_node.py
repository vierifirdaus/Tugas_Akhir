from app.parsers import Node

input_str = r"""
1	[fillcolor="#FFFB81",
		height=5.6042,
		label="import re\lclass AttributeParser:\l\l    @staticmethod\l    def parse(attr_str):\l        attrs = {}\l        bracket_match = re.search('\\[(\
.*)\\]', attr_str, re.DOTALL)\l        if bracket_match:\l            attr_str = bracket_match.group(1)\l        pairs = re.finditer(\l            '(\\w+)\\s*=\\s*(?:\"(\
.*?)(?<!\\\\)\"|\"\"\"(.*?)\"\"\"|([^,\\s]+))',\l            attr_str, re.DOTALL)\l        for match in pairs:\l            name = match.group(\
1)\l            value = match.group(2) or match.group(3) or match.group(4)\l            attrs[name] = value\l        return attrs\linput_\
str = \"\"\"\l107 -> 108	[label=calls,\l				lp=\"3292.7,1976.1\",\l				pos=\"e,3280.5,1951.6 3212...\",\l				style=dashed];\l"\"\"\l",
		pos="226.62,773.25",
		shape=rectangle,
		style="filled,solid",
		width=6.2951];
"""

res = Node.Node(input_str)
print(res.graphViz())