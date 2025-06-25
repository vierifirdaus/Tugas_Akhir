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
107 -> 108	[label=calls,
				lp="3292.7,1976.1",
				pos="e,3280.5,1951.6 3212.2,3428 3224.5,3162.6 3271.5,2146.1 3279.9,1962.9",
				style=dashed];
"""

if __name__ == "__main__":
    parsed_attrs = AttributeParser.parse(input_str)
    print(parsed_attrs)