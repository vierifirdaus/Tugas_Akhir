from app.parsers import Graph

input_str = r"""
graph [bb="0,0,7473.2,4992.2",
		compound=True,
		fontname="DejaVu Sans Mono",
		label=123asdjlajlsfkjasldjldj1qiow,
		lheight=0.24,
		lp="3736.6,12.625",
		lwidth=3.66,
		pack=False,
		rankdir=TB,
		ranksep=0.02
	];
"""

res = Graph.Graph(input_str)
print(res.graphViz())