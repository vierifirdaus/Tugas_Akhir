from app.parsers import EdgeLabel

input_str = r"""
edge [fontname="DejaVu Sans Mono",label="p[]123123123"];
"""
node = EdgeLabel.EdgeLabel(input_str)
print(node)