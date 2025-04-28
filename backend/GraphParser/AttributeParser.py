import re

class AttributeParser:
    @staticmethod
    def parse(attr_str):
        attrs = {}
        pairs = re.findall(r'(\w+)=("[^"]*"|\S+)', attr_str)
        for key, value in pairs:
            value = value.strip('"')
            if value.lower() in ["true", "false"]:
                value = value.lower() == "true"
            elif value.replace(".", "", 1).isdigit():
                value = float(value) if "." in value else int(value)
            elif "," in value:
                try:
                    value = list(map(float, value.split(',')))
                except:
                    value = value.split(",")
            attrs[key] = value
        return attrs