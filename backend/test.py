# from app.parsers import GraphParser

# # Pakai context manager untuk buka file, jadi aman otomatis close
# with open(r"C:\Users\ACER\OneDrive - Institut Teknologi Bandung\Tugas Akhir\Kode\Tugas_Akhir\backend\test.txt", "r") as f:
#     input_str = f.read()

# parser = GraphParser.GraphParser(input_str)
# # test print nama type dari subgraph 
# parser.print()
from app.parsers import GraphParser
dot_format = r"""
digraph cluster0cfg_fd0fb68f7ae542398e09847ab9b327b0_main {
	graph [bb="0,0,712,366.25",
		compound=True,
		fontname="DejaVu Sans Mono",
		label=cfg_fd0fb68f7ae542398e09847ab9b327b0_main,
		lheight=0.24,
		lp="356,12.625",
		lwidth=4.09,
		pack=False,
		rankdir=TB,
		ranksep=0.02
	];
	node [fontname="DejaVu Sans Mono",
		label="\N"
	];
	edge [fontname="DejaVu Sans Mono"];
	subgraph cluster_1 {
		graph [bb="8,203.75,78,255.75",
			color=purple,
			compound=true,
			fontname="DejaVu Sans Mono",
			label="",
			rankdir=TB,
			ranksep=0.02,
			shape=tab,
			style=filled
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		2	[color="#E552FF",
			height=0.5,
			label=main,
			pos="43,229.75",
			shape=tab,
			style=filled,
			width=0.75];
	}
	subgraph cluster_3 {
		graph [bb="62,118.5,132,170.5",
			color=purple,
			compound=true,
			fontname="DejaVu Sans Mono",
			label="",
			rankdir=TB,
			ranksep=0.02,
			shape=tab,
			style=filled
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		4	[color="#E552FF",
			height=0.5,
			label=range,
			pos="97,144.5",
			shape=tab,
			style=filled,
			width=0.75];
	}
	subgraph cluster_5 {
		graph [bb="217,33.25,287,85.25",
			color=purple,
			compound=true,
			fontname="DejaVu Sans Mono",
			label="",
			rankdir=TB,
			ranksep=0.02,
			shape=tab,
			style=filled
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		7	[color="#E552FF",
			height=0.5,
			label=print,
			pos="252,59.25",
			shape=tab,
			style=filled,
			width=0.75];
	}
	subgraph cluster_KEY {
		graph [bb="370,118.5,704,358.25",
			fontname="DejaVu Sans Mono",
			label=KEY,
			lheight=0.24,
			lp="537,345.62",
			lwidth=0.33
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		input	[fillcolor="#afeeee",
			height=0.5,
			pos="425,229.75",
			shape=parallelogram,
			style=filled,
			width=1.3142];
		call	[fillcolor="#E552FF",
			height=0.5,
			pos="425,144.5",
			shape=tab,
			style=filled,
			width=0.75];
		input -> call	[pos="e,425,162.73 425,211.5 425,200.67 425,186.45 425,173.98",
			style=invis];
		default	[fillcolor="#FFFB81",
			height=0.5,
			pos="545,144.5",
			shape=rectangle,
			style=filled,
			width=0.80556];
		if	[fillcolor="#FF6752",
			height=0.5,
			pos="420,307",
			shape=diamond,
			style=filled,
			width=0.75];
		if -> input	[pos="e,423.84,248.19 421.11,289.3 421.69,280.52 422.42,269.52 423.09,259.43",
			style=invis];
		for	[fillcolor="#FFBE52",
			height=0.5,
			pos="492,307",
			shape=hexagon,
			style=filled,
			width=0.75];
		return	[fillcolor="#98fb98",
			height=0.5,
			pos="545,229.75",
			shape=parallelogram,
			style=filled,
			width=1.5285];
		for -> return	[pos="e,532.77,248.11 504.29,288.55 510.78,279.33 518.88,267.83 526.15,257.52",
			style=invis];
		while	[fillcolor="#FFBE52",
			height=0.5,
			pos="575,307",
			shape=hexagon,
			style=filled,
			width=1.0687];
		return -> default	[pos="e,545,162.73 545,211.5 545,200.67 545,186.45 545,173.98",
			style=invis];
		try	[fillcolor=orange,
			height=0.5,
			pos="664,307",
			shape=Mdiamond,
			style=filled,
			width=0.89559];
		raise	[fillcolor="#98fb98",
			height=0.5,
			pos="657,229.75",
			shape=house,
			style=filled,
			width=1.0899];
		try -> raise	[pos="e,658.57,247.66 662.45,289.3 661.62,280.4 660.58,269.21 659.63,259",
			style=invis];
	}
	1	[fillcolor="#FFFB81",
		height=0.5,
		label="main()\l",
		pos="113,307",
		shape=rectangle,
		style="filled,solid",
		width=0.78472];
	1 -> 2	[label=calls,
		lp="101.48,272.38",
		pos="e,59.147,248.11 96.765,288.55 87.841,278.95 76.608,266.88 66.719,256.25",
		style=dashed];
	3	[fillcolor="#FFBE52",
		height=0.5,
		label="for i in range(5):\l",
		pos="184,229.75",
		shape=hexagon,
		style="filled,solid",
		width=2.6719];
	1 -> 3	[color=black,
		pos="e,167.62,248.11 129.47,288.55 138.52,278.95 149.91,266.88 159.94,256.25"];
	3 -> 4	[label=calls,
		lp="158.88,187.12",
		pos="e,112.89,162.62 163.06,211.27 157.35,206.35 151.24,200.93 145.75,195.75 137.35,187.83 128.47,178.86 120.63,170.72",
		style=dashed];
	5	[fillcolor="#FFFB81",
		height=0.5,
		label="print('This is a test for t...', i + 1)\l",
		pos="252,144.5",
		shape=rectangle,
		style="filled,solid",
		width=3.066];
	3 -> 5	[color=green,
		label="range(5)",
		lp="207.38,187.12",
		pos="e,196.67,162.9 178.08,211.65 175.6,201.28 174.54,188.22 180.75,178.5 182.77,175.34 185.18,172.48 187.86,169.89"];
	5 -> 3	[color=black,
		pos="e,221.03,211.33 250.4,162.73 248.7,173.15 245.21,186.21 238,195.75 235.64,198.87 232.9,201.76 229.92,204.42"];
	5 -> 7	[label=calls,
		lp="265.12,101.88",
		pos="e,252,77.477 252,126.25 252,115.42 252,101.2 252,88.728",
		style=dashed];
}

"""

parser = GraphParser.GraphParser(dot_format)
parser.print()
# # Print hasil secara rapi
# def print_dot_collection(dot_collection):
#     for name, dot_str in dot_collection.items():
#         print(f"\n==== {name} ====")
#         print(dot_str)
#         print("=" * 50)

# print_dot_collection(collection)

# method = parser.collectionMethod()

# for name, dot_str in method.items():
#     print(f"\n==== {name} ====")
#     print(dot_str)
#     print("=" * 50)