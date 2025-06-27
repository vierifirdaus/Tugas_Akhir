import re

class AttributeParser:
    @staticmethod
    def parse(attr_str):
        attrs = {}
        bracket_match = re.search(r'\[(.*)\]', attr_str, re.DOTALL)
        if bracket_match:
            attr_str = bracket_match.group(1)
        pairs = re.finditer(r'(\w+)\s*=\s*(?:"(.*?)(?<!\\)"|"""(.*?)"""|([^,\s]+))', attr_str, re.DOTALL)
        for match in pairs:
            name = match.group(1)
            value = match.group(2) or match.group(3) or match.group(4)
            attrs[name] = value
        
        return attrs

input_str = r"""
8	[fillcolor="#FF6752",
			height=0.5,
			label="if char == '\"' and (i == 0 or file...'\\'):\l",
			pos="1019.5,1298.2",
			shape=diamond,
			style="filled,solid",
			width=6.8478];
"""

if __name__ == "__main__":
    parsed_attrs = AttributeParser.parse(input_str)
    print(parsed_attrs)