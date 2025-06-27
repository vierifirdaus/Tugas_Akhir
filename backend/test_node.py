from app.parsers import Node

input_str = r"""
8	[fillcolor="#FF6752",
			height=0.5,
			label="if char == '\"' and (i == 0 or file...'\\'):\l",
			pos="1019.5,1298.2",
			shape=diamond,
			style="filled,solid",
			width=6.8478];
"""

res = Node.Node(input_str)
print(res.graphViz())