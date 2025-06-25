from app.parsers import NodeLabel

input_str = r"""
node [fontname="DejaVu Sans Mono"];
"""

res = NodeLabel.NodeLabel(input_str)
print(res.graphViz())