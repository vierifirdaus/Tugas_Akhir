import re

class AttributeParser:
    @staticmethod
    def parse(attr_str):
        attrs = {}
        # First extract the content between brackets if present
        bracket_match = re.search(r'\[(.*)\]', attr_str)
        if bracket_match:
            attr_str = bracket_match.group(1)
        
        pairs = re.findall(r'(\w+)\s*=\s*("[^"]*"|\S+)', attr_str)
        
        for key, value in pairs:
            # Remove surrounding quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            
            # Handle boolean values
            if value.lower() in ["true", "false"]:
                value = value.lower() == "true"
            # Handle numeric values
            elif re.match(r'^-?\d+\.?\d*$', value):
                value = float(value) if "." in value else int(value)
            # Handle comma-separated values
            elif "," in value:
                parts = value.split(",")
                # Remove empty last element if exists
                if parts and parts[-1] == "":
                    parts = parts[:-1]
                # Convert to list or single value
                if len(parts) > 1:
                    try:
                        value = list(map(float, parts))
                    except ValueError:
                        value = parts
                else:
                    value = parts[0] if parts else ""
            
            attrs[key] = value
        
        return attrs

input_str = r"""graph [bb="0,0,100,100", compound=true, fontname="DejaVu Sans Mono", label="Graph Label", lheight=0.5, lp="10,20!", lwidth=1.5, pack=true, rankdir=LR, ranksep=0.5, color="red"]"""

if __name__ == "__main__":
    parsed_attrs = AttributeParser.parse(input_str)
    print(parsed_attrs)