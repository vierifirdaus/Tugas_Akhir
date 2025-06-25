from app.parsers import GraphParser

input_str = r"""
digraph cluster0cfg_d6b0d77699ea4e1cb0e9de87ed6e5990 {
	graph [bb="0,0,7892.2,6350.8",
		compound=True,
		fontname="DejaVu Sans Mono",
		label=cfg_d6b0d77699ea4e1cb0e9de87ed6e5990,
		lheight=0.24,
		lp="3946.1,12.625",
		lwidth=3.69,
		pack=False,
		rankdir=TB,
		ranksep=0.02
	];
	node [fontname="DejaVu Sans Mono",
		label="\N"
	];
	edge [fontname="DejaVu Sans Mono"];
	subgraph cluster0GraphParser {
		graph [bb="796.25,33.25,7542.2,4632",
			compound=True,
			fontname="DejaVu Sans Mono",
			label=GraphParser,
			lheight=0.24,
			lp="4169.2,4619.4",
			lwidth=1.05,
			pack=False,
			rankdir=TB,
			ranksep=0.02
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		subgraph cluster0__init__ {
			graph [bb="804.25,2489.2,1000.2,4598.8",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=__init__,
				lheight=0.24,
				lp="902.25,4586.1",
				lwidth=0.67,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_5 {
				graph [bb="848.25,2497.2,956.25,2549.2",
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
				6	[color="#E552FF",
					height=0.5,
					label="self.from_str",
					pos="902.25,2523.2",
					shape=tab,
					style=filled,
					width=1.2847];
			}
			5	[fillcolor="#FFFB81",
				height=2.7465,
				label="self.name = None\lself.graph = None\lself.nodeLabel = None\lself.edgeLabel = None\lself.subGraph = []\lself.node = []\lself.edge = []\lself.type = \
None\lself.parent = parent\lself.typeCode = typesCode\lself.from_str(input_str)\l",
				pos="902.25,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=2.4931];
			5 -> 6	[label=calls,
				lp="915.38,2565.9",
				pos="e,902.25,2541.6 902.25,4367.4 902.25,4005.5 902.25,2757.9 902.25,2552.9",
				style=dashed];
		}
		subgraph cluster0from_str {
			graph [bb="1008.2,41.25,2338.2,4521.1",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=from_str,
				lheight=0.24,
				lp="1673.2,4508.5",
				lwidth=0.73,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_9 {
				graph [bb="1018.2,2408.8,1132.2,2549.2",
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
				10	[color="#E552FF",
					height=0.5,
					label="regex.match",
					pos="1075.2,2523.2",
					shape=tab,
					style=filled,
					width=1.2951];
				11	[color="#E552FF",
					height=0.5,
					label="input_str.strip",
					pos="1075.2,2434.8",
					shape=tab,
					style=filled,
					width=1.3472];
				10 -> 11	[color=black,
					pos="e,1075.2,2453.1 1075.2,2505.2 1075.2,2493.5 1075.2,2477.8 1075.2,2464.3"];
			}
			subgraph cluster_13 {
				graph [bb="1413.2,2319.6,1645.2,2371.6",
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
				16	[color="#E552FF",
					height=0.5,
					label="header_match.group",
					pos="1493.2,2345.6",
					shape=tab,
					style=filled,
					width=2.0035];
				17	[color="#E552FF",
					height=0.5,
					label="re.sub",
					pos="1610.2,2345.6",
					shape=tab,
					style=filled,
					width=0.75347];
			}
			subgraph cluster_14 {
				graph [bb="1148.2,2026.8,1374.2,2078.8",
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
				21	[color="#E552FF",
					height=0.5,
					label="input_str.find",
					pos="1319.2,2052.8",
					shape=tab,
					style=filled,
					width=1.2951];
				22	[color="#E552FF",
					height=0.5,
					label="input_str.rfind",
					pos="1205.2,2052.8",
					shape=tab,
					style=filled,
					width=1.3681];
			}
			subgraph cluster_25 {
				graph [bb="1381.2,1166,1604.2,1218",
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
				27	[color="#E552FF",
					height=0.5,
					label="input_str.strip",
					pos="1547.2,1192",
					shape=tab,
					style=filled,
					width=1.3472];
				28	[color="#E552FF",
					height=0.5,
					label="regex.findall",
					pos="1435.2,1192",
					shape=tab,
					style=filled,
					width=1.2639];
			}
			subgraph cluster_30 {
				graph [bb="1277.2,987.75,1465.2,1039.8",
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
				32	[color="#E552FF",
					height=0.5,
					label="block.strip",
					pos="1418.2,1013.8",
					shape=tab,
					style=filled,
					width=1.0868];
				33	[color="#E552FF",
					height=0.5,
					label="block.split",
					pos="1323.2,1013.8",
					shape=tab,
					style=filled,
					width=1.0556];
			}
			subgraph cluster_34 {
				graph [bb="1373.2,902.5,1443.2,954.5",
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
				35	[color="#E552FF",
					height=0.5,
					label=len,
					pos="1408.2,928.5",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_37 {
				graph [bb="1607.2,654.75,1735.2,706.75",
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
				40	[color="#E552FF",
					height=0.5,
					label="block.startswith",
					pos="1671.2,680.75",
					shape=tab,
					style=filled,
					width=1.5451];
			}
			subgraph cluster_41 {
				graph [bb="1931.2,569.5,2001.2,621.5",
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
				78	[color="#E552FF",
					height=0.5,
					label="Graph",
					pos="1966.2,595.5",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_43 {
				graph [bb="1357.2,569.5,1485.2,621.5",
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
				44	[color="#E552FF",
					height=0.5,
					label="block.startswith",
					pos="1421.2,595.5",
					shape=tab,
					style=filled,
					width=1.5451];
			}
			subgraph cluster_45 {
				graph [bb="1048.2,484.25,1144.2,536.25",
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
				77	[color="#E552FF",
					height=0.5,
					label=NodeLabel,
					pos="1096.2,510.25",
					shape=tab,
					style=filled,
					width=1.1076];
			}
			subgraph cluster_47 {
				graph [bb="1152.2,484.25,1280.2,536.25",
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
				48	[color="#E552FF",
					height=0.5,
					label="block.startswith",
					pos="1216.2,510.25",
					shape=tab,
					style=filled,
					width=1.5451];
			}
			subgraph cluster_49 {
				graph [bb="2130.2,399,2224.2,451",
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
				76	[color="#E552FF",
					height=0.5,
					label=EdgeLabel,
					pos="2177.2,425",
					shape=tab,
					style=filled,
					width=1.0868];
			}
			subgraph cluster_52 {
				graph [bb="1048.2,313.75,1156.2,365.75",
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
				70	[color="#E552FF",
					height=0.5,
					label=GraphParser,
					pos="1102.2,339.75",
					shape=tab,
					style=filled,
					width=1.2743];
			}
			subgraph cluster_73 {
				graph [bb="1294.2,126.75,1458.2,178.75",
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
				75	[color="#E552FF",
					height=0.5,
					label="self.subGraph.append",
					pos="1376.2,152.75",
					shape=tab,
					style=filled,
					width=2.0451];
			}
			subgraph cluster_60 {
				graph [bb="2198.2,126.75,2268.2,178.75",
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
				61	[color="#E552FF",
					height=0.5,
					label=print,
					pos="2233.2,152.75",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_58 {
				graph [bb="1828.2,49.25,1964.2,178.75",
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
				62	[color="#E552FF",
					height=0.5,
					label="self.node.append",
					pos="1896.2,152.75",
					shape=tab,
					style=filled,
					width=1.6597];
				63	[color="#E552FF",
					height=0.5,
					label="Node",
					pos="1896.2,75.25",
					shape=tab,
					style=filled,
					width=0.75];
				62 -> 63	[color=black,
					pos="e,1896.2,93.576 1896.2,134.62 1896.2,125.8 1896.2,114.82 1896.2,104.76"];
			}
			subgraph cluster_66 {
				graph [bb="2089.2,1166,2159.2,1218",
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
				67	[color="#E552FF",
					height=0.5,
					label=print,
					pos="2124.2,1192",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_64 {
				graph [bb="1016.2,126.75,1152.2,280.5",
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
				68	[color="#E552FF",
					height=0.5,
					label="self.edge.append",
					pos="1084.2,254.5",
					shape=tab,
					style=filled,
					width=1.6597];
				69	[color="#E552FF",
					height=0.5,
					label="Edge",
					pos="1084.2,152.75",
					shape=tab,
					style=filled,
					width=0.75];
				68 -> 69	[color=black,
					pos="e,1084.2,170.93 1084.2,236.12 1084.2,221.32 1084.2,199.75 1084.2,182.4"];
			}
			subgraph cluster_79 {
				graph [bb="1955.2,902.5,2083.2,954.5",
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
				81	[color="#E552FF",
					height=0.5,
					label="sub.assign_type",
					pos="2019.2,928.5",
					shape=tab,
					style=filled,
					width=1.566];
			}
			subgraph cluster_80 {
				graph [bb="1819.2,902.5,1947.2,954.5",
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
				82	[color="#E552FF",
					height=0.5,
					label="self.assign_type",
					pos="1883.2,928.5",
					shape=tab,
					style=filled,
					width=1.5451];
			}
			9	[fillcolor="#FFFB81",
				height=0.59028,
				label="header_match = regex.match('(subgraph|digraph)?\...', input_str\l    .strip())\l",
				pos="1240.2,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=5.7326];
			9 -> 10	[label=calls,
				lp="1092.1,2565.9",
				pos="e,1076.7,2541.5 1238.5,4445.1 1222.2,4253.5 1096.8,2777.7 1077.7,2552.9",
				style=dashed];
			12	[fillcolor="#FF6752",
				height=0.5,
				label="if header_match:\l",
				pos="1261.2,2523.2",
				shape=diamond,
				style="filled,solid",
				width=3.355];
			9 -> 12	[color=black,
				pos="e,1261.1,2541.5 1240.5,4445.1 1242.5,4253.5 1258.5,2777.7 1260.9,2552.9"];
			13	[fillcolor="#FFFB81",
				height=0.59028,
				label="raw_name = header_match.group(2) or 'Unnamed'\lself.name = re.sub('^cluster\\d*_?', '', raw_name)\l",
				pos="1487.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=4.6285];
			12 -> 13	[color=green,
				label=header_match,
				lp="1455.7,2472.6",
				pos="e,1433.8,2456.4 1294.4,2509.7 1315.7,2501.6 1344.1,2490.9 1369.2,2481.2 1386.7,2474.6 1405.7,2467.3 1423.2,2460.5"];
			15	[fillcolor="#FFFB81",
				height=0.5,
				label="self.name = 'Unnamed'\l",
				pos="1222.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=2.2014];
			12 -> 15	[color=red,
				label="(not header_match)",
				lp="1303.2,2472.6",
				pos="e,1230.1,2453.1 1253.9,2506 1248.5,2494 1241,2477.3 1234.7,2463.3"];
			13 -> 16	[label=calls,
				lp="1503.7,2392.1",
				pos="e,1492.1,2363.9 1488.7,2413.1 1489.5,2401.7 1490.4,2387.5 1491.3,2375.1",
				style=dashed];
			13 -> 17	[label=calls,
				lp="1575.8,2392.1",
				pos="e,1589.2,2364 1519.5,2413.1 1536.1,2402.2 1556.5,2388.5 1574.2,2375.5 1576.2,2374 1578.3,2372.5 1580.3,2370.9",
				style=dashed];
			18	[fillcolor="#FF6752",
				height=0.5,
				label="if self.name == '_init__':\l",
				pos="1236.2,2345.6",
				shape=diamond,
				style="filled,solid",
				width=4.6364];
			13 -> 18	[color=black,
				pos="e,1274.6,2359.9 1427.8,2413.1 1384.3,2398 1326.2,2377.8 1285.4,2363.7"];
			19	[fillcolor="#FFFB81",
				height=0.5,
				label="self.name = '__init__'\l",
				pos="1319.2,2256.5",
				shape=rectangle,
				style="filled,solid",
				width=2.0556];
			18 -> 19	[color=green,
				label="self.name == '_init__'",
				lp="1355.1,2299.1",
				pos="e,1302.8,2274.7 1251.1,2329 1263.3,2316.3 1280.7,2298 1294.9,2283"];
			14	[fillcolor="#FFFB81",
				height=0.59028,
				label="start = input_str.find('{')\lend = input_str.rfind('}')\l",
				pos="1319.2,2163.2",
				shape=rectangle,
				style="filled,solid",
				width=2.2743];
			18 -> 14	[color=red,
				label="(self.name != '_init__')",
				lp="1166.5,2256.5",
				pos="e,1237.1,2175.2 1176.1,2333.7 1146.9,2325 1114.4,2309.6 1096.8,2282.5 1082.2,2260.1 1080.5,2243.6 1096.8,2222.5 1113,2201.5 1172.4,\
2186.6 1225.8,2177.1"];
			19 -> 14	[color=black,
				pos="e,1319.2,2184.9 1319.2,2238.3 1319.2,2226.5 1319.2,2210.3 1319.2,2196.2"];
			14 -> 21	[label=calls,
				lp="1332.4,2104",
				pos="e,1319.2,2071.1 1319.2,2141.6 1319.2,2124.8 1319.2,2101.1 1319.2,2082.5",
				style=dashed];
			14 -> 22	[label=calls,
				lp="1288.9,2104",
				pos="e,1223.5,2071.1 1297.5,2141.6 1278.8,2123.7 1251.6,2097.9 1231.6,2078.8",
				style=dashed];
			23	[fillcolor="#FF6752",
				height=0.5,
				label="if start == -1 or end == -1:\l",
				pos="1790.2,2052.8",
				shape=diamond,
				style="filled,solid",
				width=5.2564];
			14 -> 23	[color=black,
				pos="e,1736.7,2066.1 1401.6,2143.3 1493.7,2122.1 1641.1,2088.1 1725.4,2068.7"];
			"14_input"	[fillcolor="#afeeee",
				height=0.5,
				label="input_str.rfind",
				pos="1512.2,2256.5",
				shape=parallelogram,
				style="filled,solid",
				width=2.8141];
			"14_input" -> 14	[pos="e,1357.2,2184.9 1470.1,2238.1 1439.8,2224.5 1399.1,2205.4 1367.5,2190"];
			"14_input" -> 14	[pos="e,1368.7,2184.9 1480.9,2238.1 1453.4,2224.4 1412.7,2205 1378.9,2189.6"];
			24	[fillcolor="#98fb98",
				height=0.5,
				label="return\l",
				pos="1950.2,1622.4",
				shape=parallelogram,
				style="filled,solid",
				width=1.5285];
			23 -> 24	[color=green,
				label="start == -1 or end == -1",
				lp="1957.5,2010.1",
				pos="e,1952,1640.7 1828.2,2037.9 1848.6,2028.5 1872.3,2014 1886.2,1993.5 1960.2,1884.9 1957.4,1718 1952.8,1651.8"];
			25	[fillcolor="#FFFB81",
				height=10.309,
				label="content = input_str[start:].strip()\lfull_pattern = \"\"\"\l        (?x)\l        # ===== Main Matching Logic: Match one of four DOT \
statement types =====\l        (?:\l            # OPTION 4: A subgraph definition (e.g., \"subgraph cluster_0 {...\")\l            # \
This uses recursion on the main pattern to parse inner statements.\l            subgraph \\s+ \\w+ \\s*\l            \\{\l                (?: (?\
R) | \\s+ )* # Recursively match statements inside the subgraph\l            \\}\l        |\l            # OPTION 1: An edge statement (\
e.g., \"node1 -> node2 [labe...\")\l            (?:[A-Za-z0-9_]+\\s*->\\s*[A-Za-z0-9_]+\\s*\\[(?:[^\"[\\]]+|\"(?:\\\\\"|[^\"])*\"|\\[(?:[^[\\]]+|\"(?:\\\\\"|[^\"])*\")*\\])*\\][^;]*;?) ;\l\l        | # \
OR\l\l            # OPTION 2: A node definition (e.g., \"node1 [shape=box];\")\l            # Note: A node ID not followed by '->' \
is a node statement.\l            (?:[A-Za-z0-9_]+\\s*\\[(?:[^\"[\\]]|\"[^\"]*\"|\\[.*?\\])*?\\];)\l\l        | # OR\l\l            # \
OPTION 3: Default attributes (e.g., \"graph [rankdir=LR];\")\l            (?:graph|node|edge) \\s* (?&attributes) \\s* ;\l        )\l\l        # ===== \
Sub-pattern Definitions =====\l        (?(DEFINE)\l            # Definition for a valid quoted string, handles escaped quotes \\\"\l            (?<\
quoted_string>\l                \" (?: \\\\\" | [^\"] )* \"\l            )\l\l            # Definition for a block of attributes (e.g., \"[\
label=\"foo\", color=blue]\")\l            (?<attributes>\l                \\[\l                (?: [^\\]\"]+ | (?&quoted_string) )* # \
Match any content inside, including quoted strings\l                \\]\l            )\l        )\l        \"\"\"\lblocks = regex.findall(\
full_pattern, content, regex.VERBOSE)\l",
				pos="1483.2,1622.4",
				shape=rectangle,
				style="filled,solid",
				width=10.951];
			23 -> 25	[color=red,
				label="(not (start == -1 or end == -1))",
				lp="1758,2010.1",
				pos="e,1630.6,1993.9 1703.9,2042.6 1686.9,2037.6 1670.2,2030.1 1656.8,2018.8 1650.4,2013.4 1644.4,2007.9 1638.5,2002"];
			25 -> 27	[label=calls,
				lp="1554.9,1234.6",
				pos="e,1544.7,1210.2 1538.6,1250.8 1540.3,1239.7 1541.7,1229.8 1543,1221.5",
				style=dashed];
			25 -> 28	[label=calls,
				lp="1453.4,1234.6",
				pos="e,1437.2,1210.2 1441.7,1250.8 1440.5,1239.7 1439.4,1229.8 1438.4,1221.5",
				style=dashed];
			29	[fillcolor="#FFBE52",
				height=0.5,
				label="for block in blocks:\l",
				pos="1943.2,1192",
				shape=hexagon,
				style="filled,solid",
				width=2.9587];
			25 -> 29	[color=black,
				pos="e,1924.5,1210.4 1877.8,1253.9 1892.9,1239.9 1906,1227.7 1916.4,1218"];
			"25_input"	[fillcolor="#afeeee",
				height=0.5,
				label="input_str.strip",
				pos="1483.2,2052.8",
				shape=parallelogram,
				style="filled,solid",
				width=2.7712];
			"25_input" -> 25	[pos="e,1483.2,1993.8 1483.2,2034.4 1483.2,2026.8 1483.2,2016.8 1483.2,2005"];
			30	[fillcolor="#FFFB81",
				height=0.82986,
				label="block = block.strip()\lspace_split = block.split(' ')\ledge_check = False\l",
				pos="1502.2,1102.9",
				shape=rectangle,
				style="filled,solid",
				width=2.5451];
			29 -> 30	[color=green,
				label=blocks,
				lp="1794,1149.4",
				pos="e,1594.1,1122 1877.2,1178 1805.3,1163.7 1689.1,1140.8 1605.2,1124.2"];
			31	[fillcolor="#FFBE52",
				height=0.5,
				label="for sub in self.subGraph:\l",
				pos="1943.2,1102.9",
				shape=hexagon,
				style="filled,solid",
				width=3.7181];
			29 -> 31	[color=green,
				pos="e,1943.2,1121.4 1943.2,1173.8 1943.2,1162 1943.2,1146.2 1943.2,1132.6"];
			30 -> 32	[label=calls,
				lp="1478.4,1056.4",
				pos="e,1435.1,1032.2 1474.3,1072.9 1464.1,1062.3 1452.8,1050.5 1442.9,1040.3",
				style=dashed];
			30 -> 33	[label=calls,
				lp="1433.1,1056.4",
				pos="e,1355.8,1032.2 1436.1,1072.6 1430.7,1070 1425.2,1067.5 1420,1065 1397.6,1054.3 1392.3,1051.2 1370.2,1039.8 1368.8,1039 1367.3,1038.2 \
1365.8,1037.4",
				style=dashed];
			34	[fillcolor="#FF6752",
				height=0.5,
				label="if len(space_split) > 1:\l",
				pos="1629.2,1013.8",
				shape=diamond,
				style="filled,solid",
				width=4.2851];
			30 -> 34	[color=black,
				pos="e,1607.6,1029.6 1544.9,1072.6 1562.3,1060.7 1582.1,1047.1 1598.1,1036.1"];
			34 -> 35	[label=calls,
				lp="1507.2,971.12",
				pos="e,1427.5,946.84 1574.3,1001.8 1535.1,992.56 1482.1,977.23 1439.2,954.5 1438.5,954.1 1437.7,953.68 1437,953.24",
				style=dashed];
			36	[fillcolor="#FF6752",
				height=0.5,
				label="if space_split[1] == '->':\l",
				pos="1621.2,928.5",
				shape=diamond,
				style="filled,solid",
				width=4.6778];
			34 -> 36	[color=green,
				label="len(space_split) > 1",
				lp="1687.1,971.12",
				pos="e,1622.9,946.73 1627.6,995.5 1626.6,984.67 1625.2,970.45 1624,957.98"];
			37	[fillcolor="#FF6752",
				height=0.5,
				label="if block.startswith('graph'):\l",
				pos="1651.2,766",
				shape=diamond,
				style="filled,solid",
				width=4.9671];
			34 -> 37	[color=red,
				label="(len(space_split) <= 1)",
				lp="1873.1,877.88",
				pos="e,1731.5,776.36 1717.2,1005.6 1749,997.94 1781.3,983.08 1798.2,954.5 1803.3,946.01 1802,823.87 1797.2,817.25 1784,798.95 1763.7,\
787.25 1742.3,779.79"];
			38	[fillcolor="#FFFB81",
				height=0.5,
				label="edge_check = True\l",
				pos="1525.2,835.25",
				shape=rectangle,
				style="filled,solid",
				width=1.8785];
			36 -> 38	[color=green,
				label="space_split[1] == '->'",
				lp="1575,877.88",
				pos="e,1511.2,853.6 1552.2,917.43 1534.5,911.39 1517.5,901.78 1506.8,886.5 1502,879.71 1502.8,871.53 1505.9,863.77"];
			36 -> 37	[color=red,
				label="(space_split[1] != '->')",
				lp="1723.1,835.25",
				pos="e,1652.3,784.01 1631.9,911.43 1636.2,904.13 1640.8,895.2 1643.2,886.5 1651.9,856.24 1653.1,819.97 1652.7,795.38"];
			38 -> 37	[color=black,
				pos="e,1623.7,781.68 1558,816.76 1575.1,807.65 1596,796.47 1613.7,787.02"];
			37 -> 40	[label=calls,
				lp="1676.2,723.38",
				pos="e,1667.1,699.14 1655.3,748.15 1657.9,737.24 1661.4,722.76 1664.4,710.1",
				style=dashed];
			41	[fillcolor="#FFFB81",
				height=0.5,
				label="self.graph = Graph(block)\l",
				pos="1966.2,680.75",
				shape=rectangle,
				style="filled,solid",
				width=2.4097];
			37 -> 41	[color=green,
				label="block.startswith('graph')",
				lp="1910.5,723.38",
				pos="e,1900.1,699.23 1699.1,752.36 1749.6,739.02 1829.9,717.8 1889.3,702.1"];
			43	[fillcolor="#FF6752",
				height=0.5,
				label="if block.startswith('node'):\l",
				pos="1424.2,680.75",
				shape=diamond,
				style="filled,solid",
				width=4.8224];
			37 -> 43	[color=red,
				label="(not block.startswith('graph'))",
				lp="1564.5,723.38",
				pos="e,1435.8,697.92 1552.3,757.49 1525.7,752.61 1497.7,744.72 1473.8,732 1462.1,725.82 1451.5,715.95 1443.1,706.6"];
			41 -> 29	[color=black,
				pos="e,2012.6,1178.9 2035.1,699.12 2066.2,711.53 2096.2,732.04 2096.2,765 2096.2,1103.9 2096.2,1103.9 2096.2,1103.9 2096.2,1141.7 2060.5,\
1163.3 2023.5,1175.6"];
			41 -> 78	[label=calls,
				lp="1979.4,638.12",
				pos="e,1966.2,613.73 1966.2,662.5 1966.2,651.67 1966.2,637.45 1966.2,624.98",
				style=dashed];
			43 -> 44	[label=calls,
				lp="1436.1,638.12",
				pos="e,1421.9,613.73 1423.6,662.5 1423.2,651.67 1422.7,637.45 1422.3,624.98",
				style=dashed];
			45	[fillcolor="#FFFB81",
				height=0.5,
				label="self.nodeLabel = NodeLabel(block)\l",
				pos="1231.2,595.5",
				shape=rectangle,
				style="filled,solid",
				width=3.1597];
			43 -> 45	[color=green,
				label="block.startswith('node')",
				lp="1347.4,638.12",
				pos="e,1242.7,613.96 1342.3,670.76 1319.9,665.88 1296.4,658.35 1276.5,646.75 1266.3,640.77 1257.1,631.7 1249.7,622.9"];
			47	[fillcolor="#FF6752",
				height=0.5,
				label="if block.startswith('edge'):\l",
				pos="1668.2,595.5",
				shape=diamond,
				style="filled,solid",
				width=4.8224];
			43 -> 47	[color=red,
				label="(not block.startswith('node'))",
				lp="1656.2,638.12",
				pos="e,1629.1,609.84 1463.5,666.37 1505.5,652.02 1572.4,629.19 1618.3,613.55"];
			45 -> 29	[color=black,
				pos="e,1856.7,1184.8 1231.2,613.72 1231.2,630.55 1231.2,656.91 1231.2,679.75 1231.2,1103.9 1231.2,1103.9 1231.2,1103.9 1231.2,1134.4 \
1650.1,1169.4 1845.3,1184"];
			45 -> 77	[label=calls,
				lp="1189,552.88",
				pos="e,1124.5,528.68 1202.9,577.05 1183,564.73 1156,548.08 1134.1,534.62",
				style=dashed];
			47 -> 48	[label=calls,
				lp="1447.7,552.88",
				pos="e,1254.2,528.7 1597.2,584.4 1488.4,568.88 1291.5,540.5 1276.2,536.25 1272.5,535.21 1268.7,533.99 1264.8,532.66",
				style=dashed];
			49	[fillcolor="#FFFB81",
				height=0.5,
				label="self.edgeLabel = EdgeLabel(block)\l",
				pos="2177.2,510.25",
				shape=rectangle,
				style="filled,solid",
				width=3.1389];
			47 -> 49	[color=green,
				label="block.startswith('edge')",
				lp="2073.7,552.88",
				pos="e,2095,528.72 1741.5,584.64 1819.5,573.88 1946.4,555.59 2055.2,536.25 2064.5,534.61 2074.1,532.8 2083.8,530.93"];
			51	[fillcolor="#FF6752",
				height=0.5,
				label="if block.startswith('subgraph') or block.startswit...'digraph'):\l",
				pos="1668.2,510.25",
				shape=diamond,
				style="filled,solid",
				width=10.506];
			47 -> 51	[color=red,
				label="(not block.startswith('edge'))",
				lp="1756.4,552.88",
				pos="e,1668.2,528.48 1668.2,577.25 1668.2,566.42 1668.2,552.2 1668.2,539.73"];
			49 -> 29	[color=black,
				pos="e,2008.3,1177.5 2170.3,528.47 2164.1,545.09 2156.2,571.1 2156.2,594.5 2156.2,1103.9 2156.2,1103.9 2156.2,1103.9 2156.2,1134.4 2080.3,\
1159.5 2019.2,1174.8"];
			49 -> 76	[label=calls,
				lp="2190.4,467.62",
				pos="e,2177.2,443.23 2177.2,492 2177.2,481.17 2177.2,466.95 2177.2,454.48",
				style=dashed];
			52	[fillcolor="#FFFB81",
				height=0.5,
				label="sub_parser = GraphParser(block, parent=self, typesCode=self.typeCode)\l",
				pos="1345.2,425",
				shape=rectangle,
				style="filled,solid",
				width=6.4306];
			51 -> 52	[color=green,
				label="block.startswith('subgraph') or block.startswith('digraph')",
				lp="1515.6,467.62",
				pos="e,1338.4,443.44 1481.6,500.66 1414.5,495.63 1352.5,487.89 1342,476.25 1336.7,470.41 1335.6,462.46 1336.3,454.61"];
			54	[fillcolor="#FF6752",
				height=0.5,
				label="if edge_check:\l",
				pos="1715.2,425",
				shape=diamond,
				style="filled,solid",
				width=2.921];
			51 -> 54	[color=red,
				label="(not (block.startswith('subgraph') or block.startswith('digraph')))",
				lp="1897.7,467.62",
				pos="e,1709.2,442.32 1682,492.66 1685.9,487.56 1690,481.83 1693.2,476.25 1697.6,468.88 1701.6,460.5 1704.9,452.73"];
			52 -> 70	[label=calls,
				lp="1233.3,382.38",
				pos="e,1135.2,358.23 1277.3,406.55 1239.9,396.18 1192.9,381.91 1152.2,365.75 1150.1,364.88 1147.8,363.95 1145.6,362.99",
				style=dashed];
			71	[fillcolor="#FF6752",
				height=0.5,
				label="if sub_parser.name == 'KEY':\l",
				pos="1780.2,339.75",
				shape=diamond,
				style="filled,solid",
				width=5.4218];
			52 -> 71	[color=black,
				pos="e,1749.2,355.28 1523.6,406.52 1582.1,400.41 1635.7,394.27 1649.2,391 1680.1,383.54 1713.5,370.64 1738.9,359.78"];
			72	[fillcolor="#FFFB81",
				height=0.5,
				label="continue\l",
				pos="1642.2,254.5",
				shape=rectangle,
				style="filled,solid",
				width=0.94097];
			71 -> 72	[color=green,
				label="sub_parser.name == 'KEY'",
				lp="1805.4,297.12",
				pos="e,1670.9,272.76 1755.3,323.67 1734.5,311.13 1704.5,293.06 1680.7,278.68"];
			73	[fillcolor="#FFFB81",
				height=0.5,
				label="self.subGraph.append(sub_parser)\l",
				pos="1376.2,254.5",
				shape=rectangle,
				style="filled,solid",
				width=3.1285];
			71 -> 73	[color=red,
				label="(sub_parser.name != 'KEY')",
				lp="1611.2,297.12",
				pos="e,1421.2,272.98 1698.4,328.86 1630.9,320.59 1543.8,309.54 1527.2,305.75 1495,298.36 1459.9,286.89 1431.7,276.78"];
			72 -> 29	[color=black,
				pos="e,2010.8,1178.3 1667.7,272.99 1673.3,276.03 1679.3,278.77 1685.2,280.5 1729.2,293.28 1845.5,285.6 1891.2,288.5 2019,296.6 2051.4,\
296.11 2178.2,313.75 2237,321.91 2309.2,279.48 2309.2,338.75 2309.2,1103.9 2309.2,1103.9 2309.2,1103.9 2309.2,1118.5 2129.5,1155.4 \
2021.9,1176.2"];
			73 -> 29	[color=black,
				pos="e,1859.3,1183.9 1263.3,272.02 1170.1,286.17 1051.9,305.52 1044.2,313.75 1023.7,335.86 1037.2,351.16 1037.2,381.38 1037.2,1103.9 \
1037.2,1103.9 1037.2,1103.9 1037.2,1189.3 1142.8,1120.1 1227.2,1132.8 1303.7,1144.2 1322.3,1150.9 1399.2,1158 1491.8,1166.5 1515.4,\
1160.8 1608.2,1166 1689.2,1170.6 1780.9,1177.5 1848,1183"];
			73 -> 75	[label=calls,
				lp="1389.4,211.88",
				pos="e,1376.2,170.93 1376.2,236.12 1376.2,221.32 1376.2,199.75 1376.2,182.4",
				style=dashed];
			57	[fillcolor="#FFFB81",
				height=0.5,
				label="",
				pos="2142.2,339.75",
				shape=rectangle,
				style="filled,solid",
				width=0.75];
			54 -> 57	[color=red,
				label="(not edge_check)",
				lp="2020.6,382.38",
				pos="e,2114.8,346.11 1763,414.69 1848.3,398.07 2025.2,363.57 2103.5,348.3"];
			64	[fillcolor=orange,
				height=0.5,
				label="self.edge.append(Edge(block))\l",
				pos="1366.2,339.75",
				shape=Mdiamond,
				style="filled,solid",
				width=5.5665];
			54 -> 64	[color=green,
				label=edge_check,
				lp="1608.4,382.38",
				pos="e,1419.5,353.45 1672.8,413.88 1612.4,399.46 1501,372.9 1430.5,356.07"];
			58	[fillcolor=orange,
				height=0.5,
				label="self.node.append(Node(block))\l",
				pos="1896.2,254.5",
				shape=Mdiamond,
				style="filled,solid",
				width=5.6078];
			57 -> 58	[color=black,
				pos="e,1937.1,269.33 2115,329.52 2074.8,315.92 1998.8,290.22 1947.9,272.98"];
			59	[fillcolor="#FFFB81",
				height=0.5,
				label="",
				pos="2117.2,152.75",
				shape=rectangle,
				style="filled,solid",
				width=0.75];
			58 -> 59	[color=black,
				pos="e,2090,166.07 1928.4,239 1968.5,220.9 2036.9,190.01 2079.5,170.8"];
			58 -> 62	[label=calls,
				lp="1909.4,211.88",
				pos="e,1896.2,170.93 1896.2,236.12 1896.2,221.32 1896.2,199.75 1896.2,182.4",
				style=dashed];
			60	[fillcolor="#FFFB81",
				height=0.5,
				label="print(f'[!] Tidak dikenali d...')\l",
				pos="2233.2,254.5",
				shape=rectangle,
				style="filled,solid",
				width=2.6806];
			60 -> 61	[label=calls,
				lp="2246.4,211.88",
				pos="e,2233.2,170.93 2233.2,236.12 2233.2,221.32 2233.2,199.75 2233.2,182.4",
				style=dashed];
			60 -> 59	[color=black,
				pos="e,2137.2,170.93 2213,236.12 2194.4,220.1 2166.6,196.16 2145.7,178.21"];
			59 -> 29	[color=black,
				pos="e,2010.3,1178.3 2112.9,171.07 2107.1,198.14 2100.8,250.49 2128.2,280.5 2184.9,342.5 2253.7,255.61 2314.2,313.75 2336.5,335.06 2329.2,\
350.59 2329.2,381.38 2329.2,1103.9 2329.2,1103.9 2329.2,1103.9 2329.2,1131.5 2300.2,1123.3 2274.2,1132.8 2194.1,1161.9 2169.7,1154 \
2085.2,1166 2064.6,1169 2042.2,1172.6 2021.6,1176.3"];
			64 -> 29	[color=black,
				pos="e,1860.7,1183.4 1268,349.38 1217,357.07 1155.1,371.58 1105.2,399 1062,422.78 1017.2,417.3 1017.2,466.62 1017.2,1103.9 1017.2,1103.9 \
1017.2,1103.9 1017.2,1128.8 1012.5,1142.8 1032.2,1158 1044.9,1167.8 1592.3,1165.3 1608.2,1166 1689.8,1169.6 1782.2,1176.7 1849.3,\
1182.5"];
			64 -> 68	[label=calls,
				lp="1244.6,297.12",
				pos="e,1127,272.97 1312.5,326.15 1268,315.32 1203.5,298.62 1148.2,280.5 1144.8,279.37 1141.3,278.15 1137.7,276.88",
				style=dashed];
			66	[fillcolor="#FFFB81",
				height=0.5,
				label="print(f'Failed to parse edge...')\l",
				pos="2124.2,1622.4",
				shape=rectangle,
				style="filled,solid",
				width=2.8056];
			66 -> 29	[color=black,
				pos="e,1971.7,1210.4 2122.7,1604 2117.1,1548.3 2093.4,1370.5 2014.2,1251.2 2005.5,1238.1 1993,1226.5 1980.8,1217.1"];
			66 -> 67	[label=calls,
				lp="2137.4,1234.6",
				pos="e,2124.2,1210.1 2124.2,1604.1 2124.2,1538.2 2124.2,1303.4 2124.2,1221.4",
				style=dashed];
			79	[fillcolor="#FFFB81",
				height=0.5,
				label="sub.assign_type()\l",
				pos="2015.2,1013.8",
				shape=rectangle,
				style="filled,solid",
				width=1.7118];
			31 -> 79	[color=green,
				label="self.subGraph",
				lp="2029.5,1056.4",
				pos="e,2001.7,1032.1 1958.4,1084.7 1963.8,1078.6 1969.8,1071.5 1975.2,1065 1981.6,1057.3 1988.4,1048.9 1994.6,1041.1"];
			80	[fillcolor="#FFFB81",
				height=0.5,
				label="self.assign_type()\l",
				pos="1874.2,1013.8",
				shape=rectangle,
				style="filled,solid",
				width=1.691];
			31 -> 80	[color=green,
				pos="e,1888.1,1032.2 1929.6,1084.7 1919.8,1072.2 1906.3,1055.2 1895.1,1041"];
			79 -> 31	[color=black,
				pos="e,1951.8,1084.8 1992.2,1032.1 1986.7,1036.9 1981,1042.2 1976.2,1047.8 1969.2,1056 1962.6,1066 1957.3,1075.1"];
			79 -> 81	[label=calls,
				lp="2030.7,971.12",
				pos="e,2018.4,946.73 2016.1,995.5 2016.6,984.67 2017.3,970.45 2017.9,957.98",
				style=dashed];
			80 -> 82	[label=calls,
				lp="1892.7,971.12",
				pos="e,1881.4,946.73 1876.1,995.5 1877.3,984.67 1878.8,970.45 1880.2,957.98",
				style=dashed];
			15 -> 14	[color=black,
				pos="e,1237.1,2170.9 1163.9,2416.4 1120.1,2402.7 1066.6,2384.6 1060.2,2375.5 1020.8,2319.4 1050.2,2283.7 1081.2,2222.5 1088,2209.2 1090.2,\
2204.4 1103.2,2197.2 1124.3,2185.7 1177.6,2177.4 1225.9,2172.1"];
		}
		subgraph cluster0assign_type {
			graph [bb="2346.2,1596.4,3331.2,4517.9",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=assign_type,
				lheight=0.24,
				lp="2838.8,4505.2",
				lwidth=0.99,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_96 {
				graph [bb="2485.2,2137.2,2559.2,2189.2",
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
				98	[color="#E552FF",
					height=0.5,
					label=getattr,
					pos="2522.2,2163.2",
					shape=tab,
					style=filled,
					width=0.79514];
			}
			85	[fillcolor="#FF6752",
				height=0.5,
				label="if self.parent is None:\l",
				pos="2526.2,4466.6",
				shape=diamond,
				style="filled,solid",
				width=4.0371];
			86	[fillcolor="#FFFB81",
				height=0.5,
				label="self.type = 'dot'\l",
				pos="2441.2,2523.2",
				shape=rectangle,
				style="filled,solid",
				width=1.5451];
			85 -> 86	[color=green,
				label="self.parent is None",
				lp="2499.8,2565.9",
				pos="e,2442,2541.7 2525.5,4448.2 2517.7,4270.2 2452.4,2778.8 2442.5,2552.9"];
			87	[fillcolor="#FF6752",
				height=0.5,
				label="if self.typeCode is not None:\l",
				pos="2701.2,2523.2",
				shape=diamond,
				style="filled,solid",
				width=5.1738];
			85 -> 87	[color=red,
				label="(self.parent is not None)",
				lp="2771.9,2565.9",
				pos="e,2699.7,2541.4 2527.8,4448.5 2543.7,4271.8 2678.3,2779 2698.7,2552.9"];
			88	[fillcolor="#98fb98",
				height=0.5,
				label="return\l",
				pos="2441.2,2434.8",
				shape=parallelogram,
				style="filled,solid",
				width=1.5285];
			86 -> 88	[color=black,
				pos="e,2441.2,2453.1 2441.2,2505.2 2441.2,2493.5 2441.2,2477.8 2441.2,2464.3"];
			90	[fillcolor="#FF6752",
				height=0.5,
				label="if self.name in self.typeCode['function']:\l",
				pos="3068.2,2434.8",
				shape=diamond,
				style="filled,solid",
				width=7.0959];
			87 -> 90	[color=green,
				label="self.typeCode is not None",
				lp="3016.3,2472.6",
				pos="e,3011.2,2449.2 2753.8,2509.9 2818.6,2494.6 2928.9,2468.6 3000.2,2451.8"];
			91	[fillcolor="#FF6752",
				height=0.5,
				label="if self.subGraph:\l",
				pos="2729.2,2345.6",
				shape=diamond,
				style="filled,solid",
				width=3.169];
			87 -> 91	[color=red,
				label="(self.typeCode is None)",
				lp="2733.8,2434.8",
				pos="e,2706.9,2360.4 2688.5,2506.1 2672.4,2483.8 2648.7,2442.5 2663.2,2408.8 2670.5,2392.1 2684.6,2377.8 2697.9,2367.2"];
			92	[fillcolor="#FFFB81",
				height=0.5,
				label="self.type = 'function'\l",
				pos="3143.2,2345.6",
				shape=rectangle,
				style="filled,solid",
				width=1.9514];
			90 -> 92	[color=green,
				label="self.name in self.typeCode['function']",
				lp="3223.1,2392.1",
				pos="e,3128.1,2363.8 3082.1,2417.4 3090.4,2407.6 3101.3,2394.8 3111,2383.5 3114.1,2379.9 3117.4,2376.1 3120.7,2372.3"];
			90 -> 91	[color=red,
				label="(self.name not in self.typeCode['function'])",
				lp="2963.9,2392.1",
				pos="e,2750.9,2360.5 2948.8,2424.7 2911.6,2419.8 2870.8,2412.3 2834.5,2400.8 2808.4,2392.4 2780.9,2378.1 2760.5,2366.3"];
			94	[fillcolor="#98fb98",
				height=0.5,
				label="return\l",
				pos="3188.2,2256.5",
				shape=parallelogram,
				style="filled,solid",
				width=1.5285];
			92 -> 94	[color=black,
				pos="e,3179.2,2275 3152.1,2327.4 3158.4,2315.3 3166.9,2298.9 3174.1,2285"];
			96	[fillcolor="#FF6752",
				height=0.5,
				label="if getattr(self.parent, 'parent', None) == None:\l",
				pos="2660.2,2256.5",
				shape=diamond,
				style="filled,solid",
				width=8.4186];
			91 -> 96	[color=green,
				label="self.subGraph",
				lp="2739.8,2299.1",
				pos="e,2673.3,2274 2717.2,2329.4 2707.1,2316.6 2692.3,2297.9 2680.3,2282.8"];
			97	[fillcolor="#FF6752",
				height=0.5,
				label="if getattr(getattr(self.parent, 'parent', None), 'parent', None\l",
				pos="2946.2,2163.2",
				shape=diamond,
				style="filled,solid",
				width=10.485];
			91 -> 97	[color=red,
				label="(not self.subGraph)",
				lp="3061.1,2256.5",
				pos="e,2978.8,2180.2 2787.3,2336.3 2850.4,2326.2 2945.7,2307.4 2972.2,2282.5 3000.8,2255.7 3012.5,2231.9 2994.2,2197.2 2992.4,2193.7 \
2990,2190.5 2987.3,2187.6"];
			96 -> 98	[label=calls,
				lp="2669.6,2205.9",
				pos="e,2541.4,2181.5 2660.8,2238.2 2660.2,2224.9 2657,2207.2 2645.2,2197.2 2629.9,2184.3 2574,2196.5 2555.2,2189.2 2553.9,2188.7 2552.5,\
2188.1 2551.2,2187.5",
				style=dashed];
			99	[fillcolor="#FFFB81",
				height=0.5,
				label="self.type = 'class'\l",
				pos="2415.2,2163.2",
				shape=rectangle,
				style="filled,solid",
				width=1.6806];
			96 -> 99	[color=green,
				label="getattr(self.parent, 'parent', None) == None",
				lp="2505.1,2205.9",
				pos="e,2383.3,2181.7 2477.7,2248.9 2428.7,2243.1 2384.8,2232.7 2369,2214.5 2361.6,2206 2366.1,2196.9 2374.6,2188.8"];
			96 -> 97	[color=red,
				label="(getattr(self.parent, 'parent', None) != None)",
				lp="2855.9,2205.9",
				pos="e,2817.9,2175.6 2671.8,2238.8 2682.1,2225.2 2698.5,2206.9 2717.5,2197.2 2734.2,2188.8 2769.1,2182.1 2806.7,2177.1"];
			101	[fillcolor="#98fb98",
				height=0.5,
				label="return\l",
				pos="2410.2,2052.8",
				shape=parallelogram,
				style="filled,solid",
				width=1.5285];
			99 -> 101	[color=black,
				pos="e,2411.1,2071.1 2414.4,2144.8 2413.7,2128.1 2412.5,2102.4 2411.6,2082.6"];
			103	[fillcolor="#FFFB81",
				height=0.5,
				label="self.type = 'method'\l",
				pos="2552.2,2052.8",
				shape=rectangle,
				style="filled,solid",
				width=1.9201];
			97 -> 103	[color=red,
				label="getattr(getattr(self.parent, 'parent', None), 'parent', None
    ) == None and getattr(self.parent, 'name', None) != 'main'",
				lp="2647.4,2104",
				pos="e,2497.3,2071.2 2818.6,2150.9 2744.2,2144.4 2648.4,2136.1 2563.2,2129.2 2551.4,2128.3 2464.6,2130 2456.5,2121.2 2446.1,2110 2447.6,\
2099.2 2456.5,2086.8 2457.7,2085.1 2470.6,2080.3 2486.5,2074.9"];
			104	[fillcolor="#FFFB81",
				height=0.5,
				label="self.type = None\l",
				pos="2842.2,2052.8",
				shape=rectangle,
				style="filled,solid",
				width=1.6285];
			97 -> 104	[color=red,
				label="(not (getattr(getattr(self.parent, 'parent', None), 'parent', None) == None and
    getattr(self.parent, 'name', None) != 'main'))",
				lp="3094.9,2104",
				pos="e,2841.1,2071.1 2890.4,2147.4 2876.8,2141.4 2863.7,2132.9 2854.5,2121.2 2845.9,2110.3 2842.6,2095.4 2841.6,2082.4"];
			105	[fillcolor="#98fb98",
				height=0.5,
				label="return\l",
				pos="2552.2,1622.4",
				shape=parallelogram,
				style="filled,solid",
				width=1.5285];
			103 -> 105	[color=black,
				pos="e,2552.2,1640.4 2552.2,2034.4 2552.2,1968.6 2552.2,1733.7 2552.2,1651.8"];
		}
		subgraph cluster0print {
			graph [bb="3339.2,1588.4,3995.2,4564.2",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=print,
				lheight=0.24,
				lp="3667.2,4551.6",
				lwidth=0.39,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_109 {
				graph [bb="3347.2,2497.2,3777.2,2549.2",
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
				110	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3670.2,2523.2",
					shape=tab,
					style=filled,
					width=0.75];
				111	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3742.2,2523.2",
					shape=tab,
					style=filled,
					width=0.75];
				112	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3382.2,2523.2",
					shape=tab,
					style=filled,
					width=0.75];
				113	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3454.2,2523.2",
					shape=tab,
					style=filled,
					width=0.75];
				114	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3526.2,2523.2",
					shape=tab,
					style=filled,
					width=0.75];
				115	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3598.2,2523.2",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_117 {
				graph [bb="3607.2,2319.6,3677.2,2371.6",
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
				119	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3642.2,2345.6",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_118 {
				graph [bb="3897.2,2319.6,3967.2,2371.6",
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
				120	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3932.2,2345.6",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_122 {
				graph [bb="3571.2,2137.2,3641.2,2189.2",
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
				124	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3606.2,2163.2",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_123 {
				graph [bb="3917.2,2137.2,3987.2,2189.2",
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
				125	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3952.2,2163.2",
					shape=tab,
					style=filled,
					width=0.75];
			}
			subgraph cluster_127 {
				graph [bb="3706.2,1596.4,3856.2,1648.4",
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
				129	[color="#E552FF",
					height=0.5,
					label=print,
					pos="3741.2,1622.4",
					shape=tab,
					style=filled,
					width=0.75];
				130	[color="#E552FF",
					height=0.5,
					label="sg.print",
					pos="3817.2,1622.4",
					shape=tab,
					style=filled,
					width=0.85764];
			}
			109	[fillcolor="#FFFB81",
				height=1.7882,
				label="indent_str = '   ' * indent\lprint(f'{indent_str}Graph Na...')\lprint(f'{indent_str}Type    ...')\lprint(f'{indent_str}Graph   ...')\lprint(\
f'{indent_str}Node Lab...')\lprint(f'{indent_str}Edge Lab...')\lprint(f'{indent_str}Nodes   ...')\l",
				pos="3598.2,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=2.9201];
			109 -> 110	[label=calls,
				lp="3682.1,2565.9",
				pos="e,3669.6,2541.7 3600.6,4401.9 3612,4093.8 3661.3,2765.7 3669.2,2553",
				style=dashed];
			109 -> 111	[label=calls,
				lp="3752.8,2565.9",
				pos="e,3741,2541.7 3603,4401.9 3625.8,4093.8 3724.3,2765.7 3740.1,2553",
				style=dashed];
			109 -> 112	[label=calls,
				lp="3400.3,2565.9",
				pos="e,3384.2,2541.7 3591.2,4401.9 3556.9,4093.8 3409.1,2765.7 3385.5,2553",
				style=dashed];
			109 -> 113	[label=calls,
				lp="3470.7,2565.9",
				pos="e,3455.5,2541.7 3593.5,4401.9 3570.7,4093.8 3472.2,2765.7 3456.4,2553",
				style=dashed];
			109 -> 114	[label=calls,
				lp="3541,2565.9",
				pos="e,3526.9,2541.7 3595.9,4401.9 3584.5,4093.8 3535.2,2765.7 3527.3,2553",
				style=dashed];
			109 -> 115	[label=calls,
				lp="3611.4,2565.9",
				pos="e,3598.2,2541.7 3598.2,4401.9 3598.2,4093.8 3598.2,2765.7 3598.2,2553",
				style=dashed];
			116	[fillcolor="#FFBE52",
				height=0.5,
				label="for n in self.node:\l",
				pos="3887.2,2523.2",
				shape=hexagon,
				style="filled,solid",
				width=2.79];
			109 -> 116	[color=black,
				pos="e,3884.7,2541.7 3607.7,4401.9 3653.6,4093.8 3851.3,2765.7 3883,2553"];
			117	[fillcolor="#FFFB81",
				height=0.5,
				label="print(f'{indent_str}  -', n)\l",
				pos="3682.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=2.3576];
			116 -> 117	[color=green,
				label="self.node",
				lp="3743.2,2472.6",
				pos="e,3690.5,2452.8 3837.6,2504.8 3820,2499.1 3799.9,2493.3 3781.2,2489.2 3752.8,2483.1 3741.4,2495.9 3716.2,2481.2 3708.3,2476.7 3701.7,\
2469.4 3696.4,2462"];
			118	[fillcolor="#FFFB81",
				height=0.5,
				label="print(f'{indent_str}Edges   ...')\l",
				pos="3886.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=2.8056];
			116 -> 118	[color=green,
				pos="e,3886.5,2453.1 3887.1,2505.2 3886.9,2493.5 3886.7,2477.8 3886.6,2464.3"];
			117 -> 116	[color=black,
				pos="e,3857.2,2504.9 3744.1,2453.1 3754.3,2456.4 3764.7,2460.1 3774.2,2464 3799.2,2474.2 3826,2487.9 3847.3,2499.4"];
			117 -> 119	[label=calls,
				lp="3680.1,2392.1",
				pos="e,3650.3,2364.1 3674.3,2416.5 3668.8,2404.6 3661.4,2388.3 3655.1,2374.5",
				style=dashed];
			118 -> 120	[label=calls,
				lp="3925.1,2392.1",
				pos="e,3923,2364.1 3895.3,2416.5 3901.7,2404.4 3910.4,2388 3917.7,2374.1",
				style=dashed];
			121	[fillcolor="#FFBE52",
				height=0.5,
				label="for e in self.edge:\l",
				pos="3787.2,2345.6",
				shape=hexagon,
				style="filled,solid",
				width=2.79];
			118 -> 121	[color=black,
				pos="e,3807.1,2364.1 3866.7,2416.5 3852.1,2403.7 3832.1,2386.1 3815.7,2371.7"];
			122	[fillcolor="#FFFB81",
				height=0.5,
				label="print(f'{indent_str}  -', e)\l",
				pos="3640.2,2256.5",
				shape=rectangle,
				style="filled,solid",
				width=2.3576];
			121 -> 122	[color=green,
				label="self.edge",
				lp="3704.2,2299.1",
				pos="e,3649.2,2274.6 3725.5,2331.2 3708.9,2325.7 3691.5,2318.1 3677.2,2307.8 3668.7,2301.5 3661.3,2292.7 3655.4,2284.2"];
			123	[fillcolor="#FFFB81",
				height=0.5,
				label="print(f'{indent_str}Subgraph...')\l",
				pos="3848.2,2256.5",
				shape=rectangle,
				style="filled,solid",
				width=2.9201];
			121 -> 123	[color=green,
				pos="e,3836,2275 3799.3,2327.4 3807.9,2315.1 3819.7,2298.2 3829.6,2284.2"];
			122 -> 121	[color=black,
				pos="e,3774.1,2327.2 3704,2275 3714.9,2279.2 3725.7,2284.4 3735.2,2290.5 3746.9,2298 3757.9,2308.6 3766.7,2318.4"];
			122 -> 124	[label=calls,
				lp="3637.4,2205.9",
				pos="e,3612.7,2181.6 3633.9,2238.3 3629,2225.4 3622.3,2207.4 3616.7,2192.4",
				style=dashed];
			123 -> 125	[label=calls,
				lp="3925.7,2205.9",
				pos="e,3932.4,2181.6 3867.8,2238.3 3883.7,2224.4 3906.3,2204.6 3924.1,2188.9",
				style=dashed];
			126	[fillcolor="#FFBE52",
				height=0.5,
				label="for sg in self.subGraph:\l",
				pos="3779.2,2163.2",
				shape=hexagon,
				style="filled,solid",
				width=3.5494];
			123 -> 126	[color=black,
				pos="e,3792.4,2181.6 3835.3,2238.3 3825.1,2224.9 3810.8,2206 3799.2,2190.7"];
			127	[fillcolor="#FFFB81",
				height=0.59028,
				label="print(f'{indent_str}  - Subg...')\lsg.print(indent=indent + 1)\l",
				pos="3779.2,2052.8",
				shape=rectangle,
				style="filled,solid",
				width=2.7951];
			126 -> 127	[color=green,
				label="self.subGraph",
				lp="3773.4,2104",
				pos="e,3742,2074.5 3751.8,2144.9 3744.1,2138.5 3736.7,2130.5 3732.5,2121.2 3726.2,2107.3 3725.4,2100.4 3732.5,2086.8 3733.2,2085.5 3733.9,\
2084.2 3734.7,2083"];
			127 -> 126	[color=black,
				pos="e,3801.4,2144.9 3809.6,2074.5 3813.1,2078.1 3816.2,2082.2 3818.2,2086.8 3824.7,2100.7 3823.9,2107 3818.2,2121.2 3816.1,2126.7 3812.8,\
2131.8 3809,2136.5"];
			127 -> 129	[label=calls,
				lp="3775.1,2010.1",
				pos="e,3739.6,1640.7 3766.7,2031 3764.8,2027.1 3763.1,2022.9 3762,2018.8 3725.5,1885.5 3733.5,1717.8 3738.7,1651.8",
				style=dashed];
			127 -> 130	[label=calls,
				lp="3803.1,2010.1",
				pos="e,3817.2,1640.9 3785.5,2031.3 3786.6,2027.2 3787.5,2022.8 3788.2,2018.8 3811.5,1883 3816.1,1717.9 3817,1652.3",
				style=dashed];
		}
		subgraph cluster0collectionSubGraph {
			graph [bb="4003.2,2222.5,4609.2,4517.9",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=collectionSubGraph,
				lheight=0.24,
				lp="4306.2,4505.2",
				lwidth=1.61,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_138 {
				graph [bb="4349.2,2230.5,4495.2,2282.5",
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
				140	[color="#E552FF",
					height=0.5,
					label="subgraph.graphViz",
					pos="4422.2,2256.5",
					shape=tab,
					style=filled,
					width=1.7951];
			}
			133	[fillcolor="#FFFB81",
				height=0.5,
				label="res = {}\l",
				pos="4283.2,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=0.94097];
			134	[fillcolor="#FFBE52",
				height=0.5,
				label="for subgraph in self.subGraph:\l",
				pos="4283.2,2523.2",
				shape=hexagon,
				style="filled,solid",
				width=4.5112];
			133 -> 134	[color=black,
				pos="e,4283.2,2541.7 4283.2,4448.2 4283.2,4270.3 4283.2,2780.3 4283.2,2553.2"];
			135	[fillcolor="#FF6752",
				height=0.5,
				label="if subgraph.name == 'KEY':\l",
				pos="4394.2,2434.8",
				shape=diamond,
				style="filled,solid",
				width=5.1944];
			134 -> 135	[color=green,
				label="self.subGraph",
				lp="4396.1,2472.6",
				pos="e,4374.3,2451.3 4305.4,2505 4322.7,2491.5 4346.6,2472.8 4365.4,2458.3"];
			136	[fillcolor="#98fb98",
				height=0.5,
				label="return res\l",
				pos="4110.2,2434.8",
				shape=parallelogram,
				style="filled,solid",
				width=2.1927];
			134 -> 136	[color=green,
				pos="e,4145.1,2453.2 4248.7,2505 4221.8,2491.5 4184.2,2472.7 4155,2458.1"];
			137	[fillcolor="#FFFB81",
				height=0.5,
				label="continue\l",
				pos="4147.2,2345.6",
				shape=rectangle,
				style="filled,solid",
				width=0.94097];
			135 -> 137	[color=green,
				label="subgraph.name == 'KEY'",
				lp="4323.6,2392.1",
				pos="e,4173.9,2364 4326.3,2422.8 4300.7,2417.6 4271.5,2410.4 4246,2400.8 4224.5,2392.6 4201.9,2380.6 4183.8,2369.9"];
			138	[fillcolor="#FFFB81",
				height=0.5,
				label="res[subgraph.name] = subgraph.graphViz()\l",
				pos="4422.2,2345.6",
				shape=rectangle,
				style="filled,solid",
				width=3.941];
			135 -> 138	[color=red,
				label="(subgraph.name != 'KEY')",
				lp="4489.8,2392.1",
				pos="e,4416.7,2364 4399.6,2417 4403.5,2405.1 4408.7,2388.8 4413.2,2374.9"];
			137 -> 134	[color=black,
				pos="e,4181.3,2509.3 4112.9,2353.2 4083.2,2361 4041.9,2377 4022.2,2408.8 4011.2,2426.6 4009.4,2439.4 4022.2,2456 4041,2480.1 4108.6,2496.9 \
4170.3,2507.5"];
			138 -> 134	[color=black,
				pos="e,4398.4,2512.3 4534.8,2364.1 4548.4,2369.1 4561.6,2375.4 4573.2,2383.5 4600.4,2402.4 4611,2430.2 4590.2,2456 4567.2,2484.5 4483.8,\
2501.3 4409.7,2510.9"];
			138 -> 140	[label=calls,
				lp="4435.4,2299.1",
				pos="e,4422.2,2275 4422.2,2327.4 4422.2,2315.7 4422.2,2299.9 4422.2,2286.2",
				style=dashed];
		}
		subgraph cluster0collectionMethod {
			graph [bb="4617.2,894.5,5601.2,4521.1",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=collectionMethod,
				lheight=0.24,
				lp="5109.2,4508.5",
				lwidth=1.42,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_146 {
				graph [bb="4628.2,2319.6,4774.2,2371.6",
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
				148	[color="#E552FF",
					height=0.5,
					label="className.append",
					pos="4701.2,2345.6",
					shape=tab,
					style=filled,
					width=1.816];
			}
			subgraph cluster_159 {
				graph [bb="5174.2,987.75,5534.2,1039.8",
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
				161	[color="#E552FF",
					height=0.5,
					label="graphviz.Source.pipe.decode",
					pos="5278.2,1013.8",
					shape=tab,
					style=filled,
					width=2.6701];
				162	[color="#E552FF",
					height=0.5,
					label="method_arr.append",
					pos="5459.2,1013.8",
					shape=tab,
					style=filled,
					width=1.8681];
			}
			subgraph cluster_163 {
				graph [bb="4900.2,987.75,5000.2,1039.8",
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
				165	[color="#E552FF",
					height=0.5,
					label="res.append",
					pos="4950.2,1013.8",
					shape=tab,
					style=filled,
					width=1.1701];
			}
			subgraph cluster_155 {
				graph [bb="4647.2,902.5,4841.2,954.5",
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
				166	[color="#E552FF",
					height=0.5,
					label="subgraph.collectionMethod",
					pos="4744.2,928.5",
					shape=tab,
					style=filled,
					width=2.4826];
			}
			144	[fillcolor="#FFFB81",
				height=0.59028,
				label="res = []\lclassName = []\l",
				pos="4898.2,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=1.5451];
			145	[fillcolor="#FFBE52",
				height=0.5,
				label="for classItem in self.typeCode['class']:\l",
				pos="4898.2,2523.2",
				shape=hexagon,
				style="filled,solid",
				width=5.5744];
			144 -> 145	[color=black,
				pos="e,4898.2,2541.5 4898.2,4445.1 4898.2,4253.5 4898.2,2777.7 4898.2,2552.9"];
			146	[fillcolor="#FFFB81",
				height=0.5,
				label="className.append(classItem['classname'])\l",
				pos="4765.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=3.8889];
			145 -> 146	[color=green,
				label="self.typeCode['class']",
				lp="4825.9,2472.6",
				pos="e,4759.2,2452.8 4792.5,2505.7 4780.9,2499.8 4770.4,2491.8 4762.5,2481.2 4758.9,2476.4 4757.7,2470.3 4757.8,2464.3"];
			147	[fillcolor="#FFFB81",
				height=0.5,
				label="classMethod = {}\l",
				pos="4985.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=1.7118];
			145 -> 147	[color=green,
				pos="e,4967.8,2453.1 4915.4,2505.2 4928.1,2492.6 4945.5,2475.2 4959.8,2461"];
			146 -> 145	[color=black,
				pos="e,4901.7,2504.9 4874,2453.2 4882.8,2456.3 4889.6,2459.8 4893.2,2464 4900.2,2472 4902.4,2483.2 4902.4,2493.6"];
			146 -> 148	[label=calls,
				lp="4754,2392.1",
				pos="e,4714.1,2364.1 4752.6,2416.5 4743.5,2404.2 4731.2,2387.4 4720.8,2373.3",
				style=dashed];
			149	[fillcolor="#FFBE52",
				height=0.5,
				label="for classItem in self.typeCode['class']:\l",
				pos="4985.2,2345.6",
				shape=hexagon,
				style="filled,solid",
				width=5.5744];
			147 -> 149	[color=black,
				pos="e,4985.2,2364.1 4985.2,2416.5 4985.2,2404.8 4985.2,2389 4985.2,2375.4"];
			150	[fillcolor="#FFFB81",
				height=0.5,
				label="classMethod[classItem['classname']] = classItem['method']\l",
				pos="4815.2,2256.5",
				shape=rectangle,
				style="filled,solid",
				width=5.2847];
			149 -> 150	[color=green,
				label="self.typeCode['class']",
				lp="4885.9,2299.1",
				pos="e,4813.2,2274.9 4874.3,2329.1 4850.9,2323.6 4830.7,2316.6 4822.5,2307.8 4817.2,2302 4814.7,2294.2 4813.7,2286.4"];
			151	[fillcolor="#FFBE52",
				height=0.5,
				label="for subgraph in self.subGraph:\l",
				pos="5186.2,2256.5",
				shape=hexagon,
				style="filled,solid",
				width=4.5112];
			149 -> 151	[color=green,
				pos="e,5146.1,2274.9 5025.4,2327.2 5057.2,2313.4 5101.7,2294.1 5135.9,2279.3"];
			150 -> 149	[color=black,
				pos="e,4979.2,2327.2 4925.2,2275 4935.2,2279.1 4944.7,2284.2 4953.2,2290.5 4962.3,2297.2 4969.3,2307.3 4974.4,2317"];
			152	[fillcolor="#FF6752",
				height=0.5,
				label="if subgraph.name in className:\l",
				pos="5186.2,2163.2",
				shape=diamond,
				style="filled,solid",
				width=5.8765];
			151 -> 152	[color=green,
				label="self.subGraph",
				lp="5227.1,2205.9",
				pos="e,5186.2,2181.6 5186.2,2238.3 5186.2,2225.5 5186.2,2207.8 5186.2,2192.9"];
			153	[fillcolor="#98fb98",
				height=0.5,
				label="return res\l",
				pos="4878.2,2163.2",
				shape=parallelogram,
				style="filled,solid",
				width=2.1927];
			151 -> 153	[color=green,
				pos="e,4937.1,2181.7 5127.2,2238 5076.1,2222.9 5002,2200.9 4947.9,2184.9"];
			154	[fillcolor="#FFFB81",
				height=0.5,
				label="method_arr = []\l",
				pos="5186.2,2052.8",
				shape=rectangle,
				style="filled,solid",
				width=1.6389];
			152 -> 154	[color=green,
				label="subgraph.name in className",
				lp="5276.2,2104",
				pos="e,5186.2,2071.1 5186.2,2144.8 5186.2,2128.1 5186.2,2102.4 5186.2,2082.6"];
			155	[fillcolor="#FFFB81",
				height=0.5,
				label="res += subgraph.collectionMethod()\l",
				pos="4744.2,1013.8",
				shape=rectangle,
				style="filled,solid",
				width=3.3056];
			152 -> 155	[color=red,
				label="(subgraph.name not in className)",
				lp="4758,1234.6",
				pos="e,4709.8,1032.2 5162.9,2146.8 5123.5,2119.8 5043.1,2060.4 4993.2,1993.5 4774.3,1699.6 4728.6,1601.4 4650.8,1243.2 4631.9,1156.5 \
4632.2,1113.9 4691.2,1047.8 4694,1044.6 4697.2,1041.7 4700.6,1038.9"];
			156	[fillcolor="#FFBE52",
				height=0.5,
				label="for method in subgraph.subGraph:\l",
				pos="5186.2,1622.4",
				shape=hexagon,
				style="filled,solid",
				width=5.1187];
			154 -> 156	[color=black,
				pos="e,5186.2,1640.4 5186.2,2034.4 5186.2,1968.6 5186.2,1733.7 5186.2,1651.8"];
			157	[fillcolor="#FF6752",
				height=0.5,
				label="if method.name in classMethod[subgraph.name]:\l",
				pos="5233.2,1192",
				shape=diamond,
				style="filled,solid",
				width=8.7699];
			156 -> 157	[color=green,
				label="subgraph.subGraph",
				lp="5411.9,1234.6",
				pos="e,5306.7,1206.3 5196.8,1604.1 5228.1,1552.1 5319.6,1391.1 5350.2,1243.2 5351.8,1235.7 5354.9,1232.1 5350.2,1226 5345.3,1219.5 5332.7,\
1213.9 5317.6,1209.3"];
			158	[fillcolor="#FF6752",
				height=0.5,
				label="if method_arr:\l",
				pos="4795.2,1192",
				shape=diamond,
				style="filled,solid",
				width=2.9003];
			156 -> 158	[color=green,
				pos="e,4829.9,1204.5 5176.5,1603.9 5141.9,1543.8 5019.7,1342.1 4869.2,1226 4860.6,1219.3 4850.3,1213.6 4840.3,1209"];
			157 -> 156	[color=red,
				label="(method.name not in classMethod[subgraph.name])",
				lp="5190.5,1234.6",
				pos="e,5168.1,1603.9 5093.4,1202.5 5064.7,1207.4 5040.3,1214.8 5030.8,1226 4932,1342.1 5094,1528.4 5160.1,1595.9"];
			159	[fillcolor="#FFFB81",
				height=0.82986,
				label="svg_str = graphviz.Source(method.graphViz(), format='svg').pipe().decode(\l    'utf-8')\lmethod_arr.append({method.name: svg_str})\l",
				pos="5352.2,1102.9",
				shape=rectangle,
				style="filled,solid",
				width=6.7014];
			157 -> 159	[color=green,
				label="method.name in classMethod[subgraph.name]",
				lp="5420.8,1149.4",
				pos="e,5289.1,1133.2 5245.3,1174.6 5253.7,1164 5265.6,1150.4 5278.2,1140.8 5278.8,1140.3 5279.3,1139.9 5279.9,1139.5"];
			159 -> 156	[color=black,
				pos="e,5211.2,1604 5554.1,1133.2 5557.9,1135.5 5561,1138 5563.2,1140.8 5585.4,1167.1 5572.1,1186.5 5558.2,1218 5481.4,1392.8 5296.9,1541.1 \
5220.4,1597.3"];
			159 -> 161	[label=calls,
				lp="5332.8,1056.4",
				pos="e,5293.1,1032.2 5327.6,1072.9 5318.9,1062.6 5309.1,1051 5300.5,1041",
				style=dashed];
			159 -> 162	[label=calls,
				lp="5431.6,1056.4",
				pos="e,5437.9,1032.1 5388.2,1072.6 5401.5,1061.8 5416.4,1049.7 5429.1,1039.3",
				style=dashed];
			163	[fillcolor="#FFFB81",
				height=0.5,
				label="res.append({subgraph.name: method_arr})\l",
				pos="4950.2,1102.9",
				shape=rectangle,
				style="filled,solid",
				width=3.9618];
			158 -> 163	[color=green,
				label=method_arr,
				lp="4918,1149.4",
				pos="e,4919.3,1121.3 4818.8,1177.8 4842.8,1164.3 4880.5,1143.1 4909.4,1126.8"];
			158 -> 155	[color=red,
				label="(not method_arr)",
				lp="4745,1102.9",
				pos="e,4722.1,1032.2 4756.6,1180.2 4733.4,1171.4 4705.7,1156.6 4691.8,1132.8 4678.3,1109.8 4682.2,1097.8 4691.8,1073 4696.5,1060.7 4705.1,\
1049.4 4714,1040.1"];
			163 -> 165	[label=calls,
				lp="4963.4,1056.4",
				pos="e,4950.2,1032.2 4950.2,1084.7 4950.2,1072.9 4950.2,1057.1 4950.2,1043.5",
				style=dashed];
			163 -> 155	[color=black,
				pos="e,4785.4,1032.1 4909.1,1084.5 4876.5,1070.7 4830.9,1051.4 4795.9,1036.6"];
			155 -> 151	[color=black,
				pos="e,5102.4,2238.7 4689.1,1032.2 4658.3,1045.6 4626.2,1067.9 4626.2,1101.9 4626.2,2164.2 4626.2,2164.2 4626.2,2164.2 4626.2,2238 4717.3,\
2178.3 4790.2,2189.2 4889.8,2204.2 4915,2205.6 5014.2,2222.5 5039.3,2226.8 5066.4,2231.8 5091.4,2236.6"];
			155 -> 166	[label=calls,
				lp="4757.4,971.12",
				pos="e,4744.2,946.73 4744.2,995.5 4744.2,984.67 4744.2,970.45 4744.2,957.98",
				style=dashed];
		}
		subgraph cluster0collectionFunction {
			graph [bb="5609.2,2129.2,6349.2,4517.9",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=collectionFunction,
				lheight=0.24,
				lp="5979.2,4505.2",
				lwidth=1.51,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_174 {
				graph [bb="5690.2,2230.5,6000.2,2282.5",
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
				176	[color="#E552FF",
					height=0.5,
					label="graphviz.Source.pipe.decode",
					pos="5896.2,2256.5",
					shape=tab,
					style=filled,
					width=2.6701];
				177	[color="#E552FF",
					height=0.5,
					label="res.append",
					pos="5740.2,2256.5",
					shape=tab,
					style=filled,
					width=1.1701];
			}
			subgraph cluster_175 {
				graph [bb="6044.2,2137.2,6246.2,2189.2",
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
				178	[color="#E552FF",
					height=0.5,
					label="subgraph.collectionFunction",
					pos="6145.2,2163.2",
					shape=tab,
					style=filled,
					width=2.5764];
			}
			170	[fillcolor="#FFFB81",
				height=0.5,
				label="res = []\l",
				pos="6179.2,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=0.89931];
			171	[fillcolor="#FFBE52",
				height=0.5,
				label="for subgraph in self.subGraph:\l",
				pos="6179.2,2523.2",
				shape=hexagon,
				style="filled,solid",
				width=4.5112];
			170 -> 171	[color=black,
				pos="e,6179.2,2541.7 6179.2,4448.2 6179.2,4270.3 6179.2,2780.3 6179.2,2553.2"];
			172	[fillcolor="#FF6752",
				height=0.5,
				label="if subgraph.type == 'function':\l",
				pos="5911.2,2434.8",
				shape=diamond,
				style="filled,solid",
				width=5.6491];
			171 -> 172	[color=green,
				label="self.subGraph",
				lp="6086.1,2472.6",
				pos="e,5953.6,2449.4 6125.3,2504.8 6078.5,2489.7 6011,2468 5964.4,2452.9"];
			173	[fillcolor="#98fb98",
				height=0.5,
				label="return res\l",
				pos="6211.2,2434.8",
				shape=parallelogram,
				style="filled,solid",
				width=2.1927];
			171 -> 173	[color=green,
				pos="e,6204.8,2453.1 6185.6,2505.2 6189.9,2493.4 6195.8,2477.5 6200.9,2463.9"];
			174	[fillcolor="#FFFB81",
				height=0.82986,
				label="svg_str = graphviz.Source(subgraph.graphViz(), format='svg').pipe().decode(\l    'utf-8')\lres.append({subgraph.name: svg_str})\l",
				pos="5863.2,2345.6",
				shape=rectangle,
				style="filled,solid",
				width=6.8368];
			172 -> 174	[color=green,
				label="subgraph.type == 'function'",
				lp="5978.8,2392.1",
				pos="e,5879.4,2376 5902.2,2417.4 5897.3,2408.5 5891,2397 5884.9,2386"];
			175	[fillcolor="#FFFB81",
				height=0.5,
				label="res += subgraph.collectionFunction()\l",
				pos="6145.2,2256.5",
				shape=rectangle,
				style="filled,solid",
				width=3.3993];
			172 -> 175	[color=red,
				label="(subgraph.type != 'function')",
				lp="6229.9,2345.6",
				pos="e,6145.7,2274.6 5983.5,2422.7 6036.3,2412.9 6101.4,2397 6118.2,2375.5 6138.4,2349.8 6144,2311.8 6145.3,2285.9"];
			174 -> 176	[label=calls,
				lp="5896.8,2299.1",
				pos="e,5889.6,2275 5874.2,2315.6 5877.9,2305.9 5882,2295.2 5885.6,2285.6",
				style=dashed];
			174 -> 177	[label=calls,
				lp="5822.2,2299.1",
				pos="e,5764.8,2274.9 5822,2315.4 5806.4,2304.3 5788.9,2291.9 5774.1,2281.4",
				style=dashed];
			174 -> 175	[color=black,
				pos="e,6088.6,2275 5957.9,2315.4 5997.2,2303.2 6041.9,2289.4 6077.8,2278.3"];
			175 -> 171	[color=black,
				pos="e,6230.1,2504.8 6266.1,2274.9 6288.1,2283.7 6308.4,2296.6 6322.2,2315.8 6359.3,2366.9 6338.6,2406.6 6299.2,2456 6284,2475.1 6261.7,\
2489.6 6240.4,2500"];
			175 -> 178	[label=calls,
				lp="6158.4,2205.9",
				pos="e,6145.2,2181.6 6145.2,2238.3 6145.2,2225.5 6145.2,2207.8 6145.2,2192.9",
				style=dashed];
		}
		subgraph cluster0graphViz {
			graph [bb="6357.2,41.25,7126.2,4521.1",
				compound=True,
				fontname="DejaVu Sans Mono",
				label=graphViz,
				lheight=0.24,
				lp="6741.8,4508.5",
				lwidth=0.73,
				pack=False,
				rankdir=TB,
				ranksep=0.02
			];
			node [fontname="DejaVu Sans Mono"];
			edge [fontname="DejaVu Sans Mono"];
			subgraph cluster_194 {
				graph [bb="6554.2,987.75,6662.2,1039.8",
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
				195	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6608.2,1013.8",
					shape=tab,
					style=filled,
					width=1.2847];
			}
			subgraph cluster_196 {
				graph [bb="6521.2,740,6669.2,861.25",
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
				198	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6609.2,835.25",
					shape=tab,
					style=filled,
					width=1.2847];
				199	[color="#E552FF",
					height=0.5,
					label="self.graph.graphViz",
					pos="6595.2,766",
					shape=tab,
					style=filled,
					width=1.8368];
				198 -> 199	[color=black,
					pos="e,6598.9,784.49 6605.6,816.93 6604.3,810.47 6602.7,802.95 6601.2,795.74"];
			}
			subgraph cluster_200 {
				graph [bb="6906.2,569.5,7082.2,706.75",
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
				202	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6994.2,680.75",
					shape=tab,
					style=filled,
					width=1.2847];
				203	[color="#E552FF",
					height=0.5,
					label="self.nodeLabel.graphViz",
					pos="6994.2,595.5",
					shape=tab,
					style=filled,
					width=2.2118];
				202 -> 203	[color=black,
					pos="e,6994.2,613.73 6994.2,662.5 6994.2,651.67 6994.2,637.45 6994.2,624.98"];
			}
			subgraph cluster_204 {
				graph [bb="6422.2,399,6598.2,536.25",
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
				206	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6535.2,510.25",
					shape=tab,
					style=filled,
					width=1.2847];
				207	[color="#E552FF",
					height=0.5,
					label="self.edgeLabel.graphViz",
					pos="6510.2,425",
					shape=tab,
					style=filled,
					width=2.2118];
				206 -> 207	[color=black,
					pos="e,6514.3,443.32 6528.6,491.89 6526.8,486.87 6524.8,481.37 6523.2,476.25 6521.1,469.22 6519,461.56 6517.1,454.38"];
			}
			subgraph cluster_208 {
				graph [bb="6972.2,228.5,7118.2,365.75",
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
				210	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="7036.2,339.75",
					shape=tab,
					style=filled,
					width=1.2847];
				211	[color="#E552FF",
					height=0.5,
					label="subgraph.graphViz",
					pos="7045.2,254.5",
					shape=tab,
					style=filled,
					width=1.7951];
				210 -> 211	[color=black,
					pos="e,7043.4,272.73 7038.1,321.5 7039.3,310.67 7040.8,296.45 7042.2,283.98"];
			}
			subgraph cluster_212 {
				graph [bb="6844.2,126.75,6964.2,280.5",
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
				214	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6902.2,254.5",
					shape=tab,
					style=filled,
					width=1.2847];
				215	[color="#E552FF",
					height=0.5,
					label="node.graphViz",
					pos="6904.2,152.75",
					shape=tab,
					style=filled,
					width=1.4306];
				214 -> 215	[color=black,
					pos="e,6903.9,170.93 6902.6,236.12 6902.9,221.32 6903.3,199.75 6903.7,182.4"];
			}
			subgraph cluster_216 {
				graph [bb="6663.2,49.25,6783.2,178.75",
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
				218	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6720.2,152.75",
					shape=tab,
					style=filled,
					width=1.2847];
				219	[color="#E552FF",
					height=0.5,
					label="edge.graphViz",
					pos="6723.2,75.25",
					shape=tab,
					style=filled,
					width=1.4306];
				218 -> 219	[color=black,
					pos="e,6722.6,93.576 6720.9,134.62 6721.3,125.8 6721.7,114.82 6722.1,104.76"];
			}
			subgraph cluster_217 {
				graph [bb="6547.2,126.75,6655.2,178.75",
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
				220	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6601.2,152.75",
					shape=tab,
					style=filled,
					width=1.2847];
			}
			subgraph cluster_186 {
				graph [bb="6680.2,2319.6,6788.2,2371.6",
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
				187	[color="#E552FF",
					height=0.5,
					label="lines.append",
					pos="6734.2,2345.6",
					shape=tab,
					style=filled,
					width=1.2847];
			}
			182	[fillcolor="#FFFB81",
				height=0.59028,
				label="indent_str = '  ' * indent\llines = []\l",
				pos="6604.2,4466.6",
				shape=rectangle,
				style="filled,solid",
				width=2.2951];
			183	[fillcolor="#FF6752",
				height=0.5,
				label="if self.name:\l",
				pos="6604.2,2523.2",
				shape=diamond,
				style="filled,solid",
				width=2.5283];
			182 -> 183	[color=black,
				pos="e,6604.2,2541.5 6604.2,4445.1 6604.2,4253.5 6604.2,2777.7 6604.2,2552.9"];
			184	[fillcolor="#FFFB81",
				height=0.5,
				label="is_digraph = False\l",
				pos="6532.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=1.7743];
			183 -> 184	[color=green,
				label="self.name",
				lp="6597.5,2472.6",
				pos="e,6546.8,2453.2 6592,2507.6 6581.7,2495.1 6566.5,2476.9 6554.1,2462"];
			186	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str}digraph ...')\l",
				pos="6740.2,2434.8",
				shape=rectangle,
				style="filled,solid",
				width=3.4931];
			183 -> 186	[color=red,
				label="(not self.name)",
				lp="6738.9,2472.6",
				pos="e,6712.9,2453.1 6625.2,2508.9 6646,2495.7 6678.3,2475.2 6703.4,2459.2"];
			188	[fillcolor="#FF6752",
				height=0.5,
				label="if 'cfg' in self.name:\l",
				pos="6532.2,2345.6",
				shape=diamond,
				style="filled,solid",
				width=3.7477];
			184 -> 188	[color=black,
				pos="e,6532.2,2364.1 6532.2,2416.5 6532.2,2404.8 6532.2,2389 6532.2,2375.4"];
			189	[fillcolor="#FFFB81",
				height=0.59028,
				label="is_digraph = True\lself.name = 'MainCode'\l",
				pos="6668.2,2256.5",
				shape=rectangle,
				style="filled,solid",
				width=2.2118];
			188 -> 189	[color=green,
				label="'cfg' in self.name",
				lp="6667.8,2299.1",
				pos="e,6636.1,2278.1 6554.7,2330.2 6574.2,2317.7 6602.9,2299.3 6626.6,2284.2"];
			190	[fillcolor="#FF6752",
				height=0.5,
				label="if self.parent is None:\l",
				pos="6570.2,2163.2",
				shape=diamond,
				style="filled,solid",
				width=4.0371];
			188 -> 190	[color=red,
				label="('cfg' not in self.name)",
				lp="6510.6,2256.5",
				pos="e,6514.9,2174.8 6499.3,2331.6 6478.8,2321.5 6454,2305.4 6442,2282.5 6429.6,2258.9 6427.6,2244.9 6442,2222.5 6456,2200.7 6480.3,2187 \
6504.1,2178.4"];
			189 -> 190	[color=black,
				pos="e,6586.6,2179.5 6646,2234.8 6630.8,2220.6 6610.5,2201.8 6594.8,2187.1"];
			191	[fillcolor="#FFFB81",
				height=0.5,
				label="is_digraph = True\l",
				pos="6672.2,2052.8",
				shape=rectangle,
				style="filled,solid",
				width=1.7326];
			190 -> 191	[color=green,
				label="self.parent is None",
				lp="6695.9,2104",
				pos="e,6656,2071.1 6584.9,2146.7 6601.4,2129.1 6628.7,2100.1 6648.3,2079.2"];
			192	[fillcolor="#FF6752",
				height=0.5,
				label="if indent == 0:\l",
				pos="6558.2,1622.4",
				shape=diamond,
				style="filled,solid",
				width=2.983];
			190 -> 192	[color=red,
				label="(self.parent is not None)",
				lp="6527.4,2052.8",
				pos="e,6547.5,1638.8 6537,2148.9 6509,2135.7 6470.9,2112.5 6453.5,2078.8 6375.9,1927.8 6495.1,1719.4 6541.3,1648.3"];
			191 -> 192	[color=black,
				pos="e,6562.7,1640 6667.6,2034.4 6650.1,1968.4 6587.2,1732.2 6565.6,1651"];
			193	[fillcolor="#FFFB81",
				height=0.5,
				label="is_digraph = True\l",
				pos="6672.2,1192",
				shape=rectangle,
				style="filled,solid",
				width=1.7326];
			192 -> 193	[color=green,
				label="indent == 0",
				lp="6700,1234.6",
				pos="e,6667.7,1210.2 6562.6,1604.8 6579.9,1540.1 6643,1303.1 6664.8,1221.1"];
			194	[fillcolor="#FFFB81",
				height=0.59028,
				label="graph_type = 'digraph' if is_digraph else ...'subgraph'\llines.append(f'{indent_str}{graph_t...')\l",
				pos="6608.2,1102.9",
				shape=rectangle,
				style="filled,solid",
				width=4.7743];
			192 -> 194	[color=red,
				label="(indent != 0)",
				lp="6561.5,1192",
				pos="e,6563.6,1124.6 6551.2,1605.3 6525.5,1543.9 6442.5,1320.5 6521.8,1166 6529,1151.8 6541.2,1140.2 6554.1,1130.9"];
			193 -> 194	[color=black,
				pos="e,6623.3,1124.4 6659.6,1173.8 6651.1,1162.3 6639.8,1146.8 6629.9,1133.3"];
			194 -> 195	[label=calls,
				lp="6621.4,1056.4",
				pos="e,6608.2,1032 6608.2,1081.2 6608.2,1069.9 6608.2,1055.6 6608.2,1043.2",
				style=dashed];
			185	[fillcolor="#FF6752",
				height=0.5,
				label="if self.graph:\l",
				pos="6782.2,1013.8",
				shape=diamond,
				style="filled,solid",
				width=2.549];
			194 -> 185	[color=black,
				pos="e,6757.2,1027.3 6649.5,1081.2 6679.2,1066.4 6718.8,1046.5 6747,1032.4"];
			196	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str} {self.g...')\l",
				pos="6638.2,928.5",
				shape=rectangle,
				style="filled,solid",
				width=3.3889];
			185 -> 196	[color=green,
				label="self.graph",
				lp="6752.8,971.12",
				pos="e,6668.3,946.9 6759.8,999.74 6737.9,987.13 6704.4,967.73 6678,952.51"];
			197	[fillcolor="#FF6752",
				height=0.5,
				label="if self.nodeLabel:\l",
				pos="6796.2,835.25",
				shape=diamond,
				style="filled,solid",
				width=3.293];
			185 -> 197	[color=red,
				label="(not self.graph)",
				lp="6839.7,928.5",
				pos="e,6795.3,853.5 6784.5,995.98 6785.1,990.78 6785.7,985.04 6786.2,979.75 6790,939.94 6793,893.79 6794.7,864.81"];
			196 -> 198	[label=calls,
				lp="6637.7,877.88",
				pos="e,6614.8,853.65 6632.8,910.34 6628.7,897.42 6623,879.43 6618.2,864.42",
				style=dashed];
			196 -> 197	[color=black,
				pos="e,6772.5,849.99 6668.3,910.12 6695.3,894.56 6734.8,871.76 6762.7,855.61"];
			200	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str}  {self....')\l",
				pos="6994.2,766",
				shape=rectangle,
				style="filled,solid",
				width=3.3472];
			197 -> 200	[color=green,
				label="self.nodeLabel",
				lp="6961.9,800.62",
				pos="e,6942.8,784.48 6831.6,822.23 6859.6,812.75 6899.1,799.3 6932.3,788.05"];
			201	[fillcolor="#FF6752",
				height=0.5,
				label="if self.edgeLabel:\l",
				pos="6747.2,680.75",
				shape=diamond,
				style="filled,solid",
				width=3.293];
			197 -> 201	[color=red,
				label="(not self.nodeLabel)",
				lp="6804.9,766",
				pos="e,6742.7,698.47 6775.1,820.2 6763.7,811.33 6750.7,798.76 6744.5,784 6734.5,760.37 6736.7,730.85 6740.4,709.61"];
			200 -> 202	[label=calls,
				lp="7007.4,723.38",
				pos="e,6994.2,698.98 6994.2,747.75 6994.2,736.92 6994.2,722.7 6994.2,710.23",
				style=dashed];
			200 -> 201	[color=black,
				pos="e,6783,693.8 6942.5,747.55 6898.6,732.75 6836.2,711.73 6793.8,697.45"];
			204	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str}  {self....')\l",
				pos="6614.2,595.5",
				shape=rectangle,
				style="filled,solid",
				width=3.3472];
			201 -> 204	[color=green,
				label="self.edgeLabel",
				lp="6723.1,638.12",
				pos="e,6634.8,613.89 6717.8,666.83 6705.8,661.17 6691.9,654.14 6680,646.75 6667.6,639.07 6654.7,629.57 6643.6,620.91"];
			205	[fillcolor="#FFBE52",
				height=0.5,
				label="for subgraph in self.subGraph:\l",
				pos="6771.2,510.25",
				shape=hexagon,
				style="filled,solid",
				width=4.5112];
			201 -> 205	[color=red,
				label="(not self.edgeLabel)",
				lp="6835.6,595.5",
				pos="e,6773.2,528.35 6758.4,664.01 6761.5,658.76 6764.5,652.72 6766.2,646.75 6776.6,610.88 6776,567.47 6774.1,539.62"];
			204 -> 206	[label=calls,
				lp="6595,552.88",
				pos="e,6551.6,528.48 6597.9,577.25 6586.8,565.53 6571.9,549.83 6559.4,536.68",
				style=dashed];
			204 -> 205	[color=black,
				pos="e,6738.4,528.68 6647.2,577.05 6670.7,564.56 6702.6,547.63 6728.2,534.07"];
			208	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{subgraph.graphViz(i...')\l",
				pos="6990.2,425",
				shape=rectangle,
				style="filled,solid",
				width=3.5451];
			205 -> 208	[color=green,
				label="self.subGraph",
				lp="6845.4,467.62",
				pos="e,6896.7,443.49 6778.2,492.05 6783.7,480.82 6792.4,466.82 6804.5,459 6823.3,446.86 6832.2,454.8 6854.2,451 6864.4,449.25 6875,447.37 \
6885.6,445.47"];
			209	[fillcolor="#FFBE52",
				height=0.5,
				label="for node in self.node:\l",
				pos="6726.2,425",
				shape=hexagon,
				style="filled,solid",
				width=3.2962];
			205 -> 209	[color=green,
				pos="e,6735.6,443.23 6761.9,492 6755.9,480.84 6747.9,466.07 6741,453.33"];
			208 -> 205	[color=black,
				pos="e,6843.1,491.76 6959.4,443.45 6940,453.95 6914.2,467.02 6890.2,476.25 6878.6,480.72 6866.2,484.87 6853.9,488.6"];
			208 -> 210	[label=calls,
				lp="7030.5,382.38",
				pos="e,7026.7,357.98 6999.8,406.75 7006,395.48 7014.3,380.52 7021.4,367.69",
				style=dashed];
			212	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str}  {node....')\l",
				pos="6838.2,339.75",
				shape=rectangle,
				style="filled,solid",
				width=3.4931];
			209 -> 212	[color=green,
				label="self.node",
				lp="6833.7,382.38",
				pos="e,6823.2,357.83 6762.4,406.6 6770.9,401.97 6779.6,396.66 6787.2,391 6797.1,383.68 6807,374.51 6815.4,366.01"];
			213	[fillcolor="#FFBE52",
				height=0.5,
				label="for edge in self.edge:\l",
				pos="6576.2,339.75",
				shape=hexagon,
				style="filled,solid",
				width=3.2962];
			209 -> 213	[color=green,
				pos="e,6607.7,358.18 6694.8,406.55 6672.4,394.12 6642.1,377.28 6617.7,363.75"];
			212 -> 209	[color=black,
				pos="e,6749.7,406.55 6814.8,358.18 6798.5,370.27 6776.6,386.54 6758.7,399.88"];
			212 -> 214	[label=calls,
				lp="6889.1,297.12",
				pos="e,6889,272.73 6851.5,321.5 6860.3,310 6872.1,294.68 6882.1,281.69",
				style=dashed];
			216	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str}  {edge....')\l",
				pos="6710.2,254.5",
				shape=rectangle,
				style="filled,solid",
				width=3.4931];
			213 -> 216	[color=green,
				label="self.edge",
				lp="6621.2,297.12",
				pos="e,6617.2,272.96 6578.3,321.65 6580.5,310.75 6585,297.11 6594.2,288.5 6598.2,284.76 6602.6,281.45 6607.3,278.5"];
			217	[fillcolor="#FFFB81",
				height=0.5,
				label="lines.append(f'{indent_str}}}')\l",
				pos="6466.2,254.5",
				shape=rectangle,
				style="filled,solid",
				width=2.7951];
			213 -> 217	[color=green,
				pos="e,6489.3,272.93 6553.2,321.3 6537.2,309.2 6515.7,292.93 6498.1,279.6"];
			216 -> 213	[color=black,
				pos="e,6622.4,321.39 6693.1,272.85 6682.1,283.31 6667.1,296.38 6652.2,305.75 6646,309.66 6639.3,313.33 6632.4,316.69"];
			216 -> 218	[label=calls,
				lp="6728.4,211.88",
				pos="e,6718.5,170.93 6712,236.12 6713.5,221.25 6715.7,199.54 6717.4,182.14",
				style=dashed];
			217 -> 220	[label=calls,
				lp="6553.1,211.88",
				pos="e,6581.2,171.14 6493.1,236.01 6510.1,224.75 6532.3,209.59 6551.2,195.25 6558.3,189.9 6565.8,183.91 6572.7,178.19",
				style=dashed];
			221	[fillcolor="#98fb98",
				height=1.1806,
				label="return '\n'.join(lines)\l",
				pos="6451.2,152.75",
				shape=parallelogram,
				style="filled,solid",
				width=2.3831];
			217 -> 221	[color=black,
				pos="e,6457.5,195.38 6463.6,236.12 6462.4,227.76 6460.8,217.23 6459.2,206.52"];
			186 -> 185	[color=black,
				pos="e,6787.4,1030.9 6761.2,2416.4 6778.2,2400.2 6799.2,2374.6 6799.2,2346.6 6799.2,2346.6 6799.2,2346.6 6799.2,1101.9 6799.2,1081.5 \
6794.7,1058.9 6790.3,1041.8"];
			186 -> 187	[label=calls,
				lp="6751.1,2392.1",
				pos="e,6735.5,2364.1 6739.1,2416.5 6738.3,2404.8 6737.2,2389 6736.2,2375.4",
				style=dashed];
		}
		3	[fillcolor="#FFFB81",
			height=2.0278,
			label="def __init__(self, input_str, parent=None, typesCode=None):...\ldef from_str(self, input_str):...\ldef assign_type(self):...\ldef \
print(self, indent=0):...\ldef collectionSubGraph(self):...\ldef collectionMethod(self):...\ldef collectionFunction(self):...\ldef \
graphViz(self, indent=0):...\l",
			pos="7334.2,4466.6",
			shape=rectangle,
			style="filled,solid",
			width=5.566];
	}
	subgraph cluster_KEY {
		graph [bb="7550.2,2408.8,7884.2,4517.9",
			fontname="DejaVu Sans Mono",
			label=KEY,
			lheight=0.24,
			lp="7717.2,4505.2",
			lwidth=0.33
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		input	[fillcolor="#afeeee",
			height=0.5,
			pos="7605.2,2523.2",
			shape=parallelogram,
			style=filled,
			width=1.3142];
		call	[fillcolor="#E552FF",
			height=0.5,
			pos="7605.2,2434.8",
			shape=tab,
			style=filled,
			width=0.75];
		input -> call	[pos="e,7605.2,2453.1 7605.2,2505.2 7605.2,2493.5 7605.2,2477.8 7605.2,2464.3",
			style=invis];
		default	[fillcolor="#FFFB81",
			height=0.5,
			pos="7725.2,2434.8",
			shape=rectangle,
			style=filled,
			width=0.80556];
		if	[fillcolor="#FF6752",
			height=0.5,
			pos="7600.2,4466.6",
			shape=diamond,
			style=filled,
			width=0.75];
		if -> input	[pos="e,7605.2,2541.7 7600.3,4448.2 7600.8,4270.3 7604.6,2780.3 7605.2,2553.2",
			style=invis];
		for	[fillcolor="#FFBE52",
			height=0.5,
			pos="7672.2,4466.6",
			shape=hexagon,
			style=filled,
			width=0.75];
		return	[fillcolor="#98fb98",
			height=0.5,
			pos="7725.2,2523.2",
			shape=parallelogram,
			style=filled,
			width=1.5285];
		for -> return	[pos="e,7718.9,2541.6 7670.8,4448.3 7659.9,4308.2 7591.4,3347.8 7708.2,2582.5 7709.8,2572.5 7712.5,2561.8 7715.4,2552.4",
			style=invis];
		while	[fillcolor="#FFBE52",
			height=0.5,
			pos="7755.2,4466.6",
			shape=hexagon,
			style=filled,
			width=1.0687];
		return -> default	[pos="e,7725.2,2453.1 7725.2,2505.2 7725.2,2493.5 7725.2,2477.8 7725.2,2464.3",
			style=invis];
		try	[fillcolor=orange,
			height=0.5,
			pos="7844.2,4466.6",
			shape=Mdiamond,
			style=filled,
			width=0.89559];
		raise	[fillcolor="#98fb98",
			height=0.5,
			pos="7837.2,2523.2",
			shape=house,
			style=filled,
			width=1.0899];
		try -> raise	[pos="e,7837.3,2541.7 7844.2,4448.2 7843.5,4270.3 7838.2,2780.3 7837.4,2553.2",
			style=invis];
	}
	1	[fillcolor="#FFFB81",
		height=52.337,
		label="import regex\limport re\limport graphviz\lfrom .Graph import Graph\lfrom .Node import Node\lfrom .NodeLabel import NodeLabel\lfrom \
.Edge import Edge\lfrom .EdgeLabel import EdgeLabel\lclass GraphParser:\l\l    def __init__(self, input_str, parent=None, typesCode=\
None):\l        self.name = None\l        self.graph = None\l        self.nodeLabel = None\l        self.edgeLabel = None\l        \
self.subGraph = []\l        self.node = []\l        self.edge = []\l        self.type = None\l        self.parent = parent\l        \
self.typeCode = typesCode\l        self.from_str(input_str)\l\l    def from_str(self, input_str):\l        header_match = regex.match('(\
subgraph|digraph)?\...',\l            input_str.strip())\l        if header_match:\l            raw_name = header_match.group(2) \
or 'Unnamed'\l            self.name = re.sub('^cluster\\d*_?', '', raw_name)\l            if self.name == '_init__':\l                \
self.name = '__init__'\l        else:\l            self.name = 'Unnamed'\l        start = input_str.find('{')\l        end = input_\
str.rfind('}')\l        if start == -1 or end == -1:\l            return\l        content = input_str[start:].strip()\l        full_\
pattern = \"\"\"\l        (?x)\l        # ===== Main Matching Logic: Match one of four DOT statement types =====\l        (?:\l            # \
OPTION 4: A subgraph definition (e.g., \"subgraph cluster_0 {...\")\l            # This uses recursion on the main pattern to parse \
inner statements.\l            subgraph \\s+ \\w+ \\s*\l            \\{\l                (?: (?R) | \\s+ )* # Recursively match \
statements inside the subgraph\l            \\}\l        |\l            # OPTION 1: An edge statement (e.g., \"node1 -> node2 [labe...\")\l            (?:[\
A-Za-z0-9_]+\\s*->\\s*[A-Za-z0-9_]+\\s*\\[(?:[^\"[\\]]+|\"(?:\\\\\"|[^\"])*\"|\\[(?:[^[\\]]+|\"(?:\\\\\"|[^\"])*\")*\\])*\\][^;]*;?) ;\l\l        | # \
OR\l\l            # OPTION 2: A node definition (e.g., \"node1 [shape=box];\")\l            # Note: A node ID not followed by '->' \
is a node statement.\l            (?:[A-Za-z0-9_]+\\s*\\[(?:[^\"[\\]]|\"[^\"]*\"|\\[.*?\\])*?\\];)\l\l        | # OR\l\l            # \
OPTION 3: Default attributes (e.g., \"graph [rankdir=LR];\")\l            (?:graph|node|edge) \\s* (?&attributes) \\s* ;\l        )\l\l        # ===== \
Sub-pattern Definitions =====\l        (?(DEFINE)\l            # Definition for a valid quoted string, handles escaped quotes \\\"\l            (?<\
quoted_string>\l                \" (?: \\\\\" | [^\"] )* \"\l            )\l\l            # Definition for a block of attributes (e.g., \"[\
label=\"foo\", color=blue]\")\l            (?<attributes>\l                \\[\l                (?: [^\\]\"]+ | (?&quoted_string) )* # \
Match any content inside, including quoted strings\l                \\]\l            )\l        )\l        \"\"\"\l        blocks = \
regex.findall(full_pattern, content, regex.VERBOSE)\l        for block in blocks:\l            block = block.strip()\l            \
space_split = block.split(' ')\l            edge_check = False\l            if len(space_split) > 1:\l                if space_split[\
1] == '->':\l                    edge_check = True\l            if block.startswith('graph'):\l                self.graph = Graph(\
block)\l            elif block.startswith('node'):\l                self.nodeLabel = NodeLabel(block)\l            elif block.startswith('\
edge'):\l                self.edgeLabel = EdgeLabel(block)\l            elif block.startswith('subgraph') or block.startswit...'\
digraph'):\l                sub_parser = GraphParser(block, parent=self, typesCode=self\l                    .typeCode)\l                \
if sub_parser.name == 'KEY':\l                    continue\l                self.subGraph.append(sub_parser)\l            elif edge_\
check:\l                try:\l                    self.edge.append(Edge(block))\l                except Exception as e:\l                    \
print(f'Failed to parse edge...')\l            else:\l                try:\l                    self.node.append(Node(block))\l                \
except Exception as e:\l                    print(f'[!] Tidak dikenali d...')\l        for sub in self.subGraph:\l            sub.assign_\
type()\l        self.assign_type()\l\l    def assign_type(self):\l        if self.parent is None:\l            self.type = 'dot'\l            \
return\l        if self.typeCode is not None:\l            if self.name in self.typeCode['function']:\l                self.type = '\
function'\l                return\l        if self.subGraph:\l            if getattr(self.parent, 'parent', None) == None:\l                \
self.type = 'class'\l                return\l        if getattr(getattr(self.parent, 'parent', None), 'parent', None\l            ) == \
None and getattr(self.parent, 'name', None) != 'main':\l            self.type = 'method'\l            return\l        self.type = \
None\l\l    def print(self, indent=0):\l        indent_str = '   ' * indent\l        print(f'{indent_str}Graph Na...')\l        \
print(f'{indent_str}Type    ...')\l        print(f'{indent_str}Graph   ...')\l        print(f'{indent_str}Node Lab...')\l        \
print(f'{indent_str}Edge Lab...')\l        print(f'{indent_str}Nodes   ...')\l        for n in self.node:\l            print(f'{\
indent_str}  -', n)\l        print(f'{indent_str}Edges   ...')\l        for e in self.edge:\l            print(f'{indent_str}  -', \
e)\l        print(f'{indent_str}Subgraph...')\l        for sg in self.subGraph:\l            print(f'{indent_str}  - Subg...')\l            \
sg.print(indent=indent + 1)\l\l    def collectionSubGraph(self):\l        res = {}\l        for subgraph in self.subGraph:\l            \
if subgraph.name == 'KEY':\l                continue\l            res[subgraph.name] = subgraph.graphViz()\l        return res\l\l    \
def collectionMethod(self):\l        res = []\l        className = []\l        for classItem in self.typeCode['class']:\l            \
className.append(classItem['classname'])\l        classMethod = {}\l        for classItem in self.typeCode['class']:\l            \
classMethod[classItem['classname']] = classItem['method']\l        for subgraph in self.subGraph:\l            if subgraph.name \
in className:\l                method_arr = []\l                for method in subgraph.subGraph:\l                    if method.name \
in classMethod[subgraph.name]:\l                        svg_str = graphviz.Source(method.graphViz(), format\l                            ='\
svg').pipe().decode('utf-8')\l                        method_arr.append({method.name: svg_str})\l                if method_arr:\l                    \
res.append({subgraph.name: method_arr})\l            res += subgraph.collectionMethod()\l        return res\l\l    def collectionFunction(\
self):\l        res = []\l        for subgraph in self.subGraph:\l            if subgraph.type == 'function':\l                svg_\
str = graphviz.Source(subgraph.graphViz(), format='svg'\l                    ).pipe().decode('utf-8')\l                res.append({\
subgraph.name: svg_str})\l            res += subgraph.collectionFunction()\l        return res\l\l    def graphViz(self, indent=\
0):\l        indent_str = '  ' * indent\l        lines = []\l        if self.name:\l            is_digraph = False\l            \
if 'cfg' in self.name:\l                is_digraph = True\l                self.name = 'MainCode'\l            if self.parent is \
None:\l                is_digraph = True\l            if indent == 0:\l                is_digraph = True\l            graph_type = '\
digraph' if is_digraph else ...'subgraph'\l            lines.append(f'{indent_str}{graph_t...')\l        else:\l            lines.append(\
f'{indent_str}digraph ...')\l        if self.graph:\l            lines.append(f'{indent_str} {self.g...')\l        if self.nodeLabel:\l            \
lines.append(f'{indent_str}  {self....')\l        if self.edgeLabel:\l            lines.append(f'{indent_str}  {self....')\l        \
for subgraph in self.subGraph:\l            lines.append(f'{subgraph.graphViz(i...')\l        for node in self.node:\l            \
lines.append(f'{indent_str}  {node....')\l        for edge in self.edge:\l            lines.append(f'{indent_str}  {edge....')\l        \
lines.append(f'{indent_str}}}')\l        return '\n'.join(lines)\l",
		pos="394.25,4466.6",
		shape=rectangle,
		style="filled,solid",
		width=10.951];
}


"""

res = GraphParser.GraphParser(input_str=input_str)

print(res.graphViz())