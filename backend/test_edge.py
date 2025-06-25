from app.parsers import Edge
input_str = r"""
58 -> 60	[color=red,
				label="regex.match('(?:[A-Za-z0-9_]+\\s*\\[(?:[^\"[\\]]|\"[^\"]*\"|\\[.*?\\])*?\\];)',
    block, regex.DOTALL)",
				lp="1437.5,407.62",
				pos="e,1320.9,354.35 1389.1,459.96 1309.8,455.28 1239.5,447.25 1226.8,433.5 1211.1,416.6 1212.8,400.02 1226.8,381.75 1232,374.94 1276.4,\
364.1 1310,356.71"];
"""
res = Edge.Edge(input_str)
print(res.graphViz())