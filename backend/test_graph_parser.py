from app.parsers import GraphParser

input_str = r"""
digraph cluster0cfg_db479e498f9c4ff892e149e3c6706f69 {
	graph [bb="0,0,1702.5,1631.2",
		compound=True,
		fontname="DejaVu Sans Mono",
		label=cfg_db479e498f9c4ff892e149e3c6706f69,
		lheight=0.24,
		lp="851.25,12.625",
		lwidth=3.51,
		pack=False,
		rankdir=TB,
		ranksep=0.02
	];
	node [fontname="DejaVu Sans Mono",
		label="\N"
	];
	edge [fontname="DejaVu Sans Mono"];
	subgraph cluster0extract_subgraph {
		graph [bb="255.5,33.25,1352.5,1623.2",
			compound=True,
			fontname="DejaVu Sans Mono",
			label=extract_subgraph,
			lheight=0.24,
			lp="804,1610.6",
			lwidth=1.48,
			pack=False,
			rankdir=TB,
			ranksep=0.02
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		subgraph cluster_3 {
			graph [bb="985.5,1410.5,1055.5,1462.5",
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
				label=len,
				pos="1020.5,1436.5",
				shape=tab,
				style=filled,
				width=0.75];
		}
		subgraph cluster_21 {
			graph [bb="656.5,881.25,786.5,933.25",
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
			25	[color="#E552FF",
				height=0.5,
				label="file_content.find",
				pos="721.5,907.25",
				shape=tab,
				style=filled,
				width=1.5868];
		}
		subgraph cluster_26 {
			graph [bb="413.5,743,483.5,795",
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
				label=range,
				pos="448.5,769",
				shape=tab,
				style=filled,
				width=0.75];
		}
		subgraph cluster_40 {
			graph [bb="659.5,94.25,775.5,146.25",
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
			42	[color="#E552FF",
				height=0.5,
				label="result.append",
				pos="717.5,120.25",
				shape=tab,
				style=filled,
				width=1.3785];
		}
		3	[fillcolor="#FFFB81",
			height=1.309,
			label="result = []\lbrace_level = 0\lin_quotes = False\li = 0\lcontent_length = len(file_content)\l",
			pos="1029.5,1542.9",
			shape=rectangle,
			style="filled,solid",
			width=3.1389];
		3 -> 4	[label=calls,
			lp="1037.9,1479.1",
			pos="e,1022,1454.8 1025.5,1495.5 1024.6,1485.5 1023.8,1475.3 1023,1466.2",
			style=dashed];
		5	[fillcolor="#FFBE52",
			height=0.5,
			label="while i < content_length:\l",
			pos="1203.5,1436.5",
			shape=hexagon,
			style="filled,solid",
			width=3.8362];
		3 -> 5	[color=black,
			pos="e,1174.4,1455 1107.1,1495.3 1127.1,1483.3 1147.8,1470.9 1164.8,1460.7"];
		6	[fillcolor="#FFFB81",
			height=0.5,
			label="char = file_content[i]\l",
			pos="1019.5,1359.2",
			shape=rectangle,
			style="filled,solid",
			width=2.0451];
		5 -> 6	[color=green,
			label="i < content_length",
			lp="1142.9,1393.9",
			pos="e,1043.3,1377.7 1131.6,1418.8 1116.4,1414.3 1100.5,1408.9 1086.2,1402.5 1074.9,1397.4 1063.1,1390.6 1052.8,1384"];
		7	[fillcolor="#98fb98",
			height=0.5,
			label="return result\l",
			pos="1205.5,1359.2",
			shape=parallelogram,
			style="filled,solid",
			width=2.6213];
		5 -> 7	[color=red,
			label="(i >= content_length)",
			lp="1271.4,1393.9",
			pos="e,1204.5,1377.7 1203.6,1418.3 1203.7,1410.7 1203.8,1401.5 1204.2,1389"];
		8	[fillcolor="#FF6752",
			height=0.5,
			label="if char == '\"' and (i == 0 or file...'\\'):\l",
			pos="1019.5,1298.2",
			shape=diamond,
			style="filled,solid",
			width=6.8478];
		6 -> 8	[color=black,
			pos="e,1019.5,1316.7 1019.5,1340.9 1019.5,1336.8 1019.5,1332.4 1019.5,1328"];
		9	[fillcolor="#FFFB81",
			height=0.5,
			label="in_quotes = not in_quotes\l",
			pos="1077.5,1229",
			shape=rectangle,
			style="filled,solid",
			width=2.4514];
		8 -> 9	[color=green,
			label="char == '\"' and (i == 0 or file_content[i - 1] != '\\')",
			lp="1181.4,1263.6",
			pos="e,1031.4,1247.4 1017.7,1280.2 1017.7,1273.8 1018.6,1266.4 1024.8,1256.4"];
		10	[fillcolor="#FF6752",
			height=0.5,
			label="if not in_quotes:\l",
			pos="626.5,1176",
			shape=diamond,
			style="filled,solid",
			width=3.1897];
		8 -> 10	[color=red,
			label="(not (char == '\"' and (i == 0 or file_content[i - 1] != '\\')))",
			lp="800.88,1229",
			pos="e,619.29,1193.3 889.19,1289.3 779.96,1281.3 639.02,1267.2 621.25,1247 611.14,1235.5 612.2,1218.5 615.91,1204.1"];
		9 -> 10	[color=black,
			pos="e,700.66,1182.8 988.79,1213 983.96,1212.3 979.17,1211.6 974.5,1211 885.09,1199.3 782.26,1189.7 711.7,1183.7"];
		11	[fillcolor="#FF6752",
			height=0.5,
			label="if file_content[i:i + 9] == 'subgraph ' and brace_level == 1:\l",
			pos="669.5,1106.8",
			shape=diamond,
			style="filled,solid",
			width=10.713];
		10 -> 11	[color=green,
			label="not in_quotes",
			lp="694.37,1141.4",
			pos="e,658.68,1124.7 636.47,1159.4 641.25,1151.9 647.11,1142.8 652.56,1134.2"];
		12	[fillcolor="#FFFB81",
			height=0.5,
			label="i += 1\l",
			pos="1059.5,59.25",
			shape=rectangle,
			style="filled,solid",
			width=0.78472];
		10 -> 12	[color=red,
			label="(not not in_quotes)",
			lp="339.85,638.75",
			pos="e,1030.9,60.892 539.5,1171.1 449.59,1165.7 316.61,1153 274.5,1124.8 267.22,1119.9 264.5,1116.5 264.5,1107.8 264.5,1107.8 264.5,1107.8 \264.5,734 264.5,679.58 281.5,667.17 281.5,612.75 281.5,612.75 281.5,612.75 281.5,119.25 281.5,81.835 861.15,65.052 1019.8,61.16"];
		13	[fillcolor="#FFFB81",
			height=0.5,
			label="block_start_index = i\l",
			pos="667.5,1037.5",
			shape=rectangle,
			style="filled,solid",
			width=2.0139];
		11 -> 13	[color=green,
			label="file_content[i:i + 9] == 'subgraph ' and brace_level == 1",
			lp="846.49,1072.1",
			pos="e,668.02,1056 668.98,1088.4 668.8,1082 668.57,1074.6 668.36,1067.5"];
		15	[fillcolor="#FF6752",
			height=0.5,
			label="if char == '{':\l",
			pos="1083.5,325",
			shape=diamond,
			style="filled,solid",
			width=2.8383];
		11 -> 15	[color=red,
			label="(not (file_content[i:i + 9] == 'subgraph ' and brace_level == 1))",
			lp="1138.2,708",
			pos="e,1083.5,343.47 904.42,1099.2 965.14,1095.5 1016.9,1089.8 1028.5,1080.8 1069.6,1048.8 1066.1,1017.3 1054.5,966.5 1024.7,836.53 847.27,\787.73 938,690 954.3,672.44 1024.3,693.22 1045.5,682 1076.5,665.55 1083.5,647.86 1083.5,612.75 1083.5,612.75 1083.5,612.75 1083.5,\377 1083.5,369.85 1083.5,362.14 1083.5,354.93"];
		21	[fillcolor=orange,
			height=0.5,
			label="open_brace_index = file_content.find('{', block_start_index)\l",
			pos="664.5,984.5",
			shape=Mdiamond,
			style="filled,solid",
			width=10.589];
		13 -> 21	[color=black,
			pos="e,665.51,1002.7 666.48,1019.2 666.39,1017.6 666.29,1015.9 666.18,1014.1"];
		21 -> 25	[label=calls,
			lp="709.54,949.88",
			pos="e,708.29,925.69 677.15,966.8 684.3,957.36 693.41,945.33 701.51,934.64",
			style=dashed];
		22	[fillcolor="#FFFB81",
			height=0.5,
			label="local_brace_level = 1\l",
			pos="572.5,907.25",
			shape=rectangle,
			style="filled,solid",
			width=2.0556];
		21 -> 22	[color=black,
			pos="e,593.7,925.59 644.54,967.17 632.23,957.1 616.2,944 602.4,932.7"];
		23	[fillcolor="#FFFB81",
			height=0.59028,
			label="i += 1\lcontinue\l",
			pos="1203.5,1542.9",
			shape=rectangle,
			style="filled,solid",
			width=0.94097];
		23 -> 5	[color=black,
			pos="e,1203.5,1455 1203.5,1521.3 1203.5,1505.6 1203.5,1483.9 1203.5,1466.5"];
		26	[fillcolor="#FFBE52",
			height=0.5,
			label="for j in range(open_brace_index + 1, content_length):\l",
			pos="572.5,846.25",
			shape=hexagon,
			style="filled,solid",
			width=7.8862];
		22 -> 26	[color=black,
			pos="e,572.5,864.71 572.5,888.87 572.5,884.82 572.5,880.41 572.5,876.02"];
		26 -> 27	[label=calls,
			lp="534.95,811.62",
			pos="e,469.12,787.48 536.73,827.87 519.06,818.8 497.68,807.1 479.5,795 479.07,794.71 478.64,794.42 478.2,794.12",
			style=dashed];
		28	[fillcolor="#FFFB81",
			height=0.5,
			label="local_char = file_content[j]\l",
			pos="585.5,769",
			shape=rectangle,
			style="filled,solid",
			width=2.5451];
		26 -> 28	[color=green,
			label="range(open_brace_index + 1, content_length)",
			lp="721.9,811.62",
			pos="e,582.5,787.36 575.52,827.8 577.01,819.15 578.85,808.5 580.54,798.69"];
		29	[fillcolor="#FFFB81",
			height=0.5,
			label="in_quotes = False\l",
			pos="959.5,120.25",
			shape=rectangle,
			style="filled,solid",
			width=1.7222];
		26 -> 29	[color=green,
			pos="e,954.99,138.7 780.7,836.21 824.49,832.51 860.12,827.36 868.5,820.25 914.04,781.62 855.55,728.14 901.5,690 923.26,671.94 1002.8,\693.7 1028.5,682 1059.9,667.73 1063.5,647.24 1063.5,612.75 1063.5,612.75 1063.5,612.75 1063.5,480.88 1063.5,422.04 1053.8,398.7 \1009.5,360 995.87,348.1 982.71,357.94 972.5,343 932.36,284.25 943.33,194.99 952.58,149.72"];
		30	[fillcolor="#FF6752",
			height=0.5,
			label="if local_char == '\"' and (j == 0 or file...'\\'):\l",
			pos="585.5,708",
			shape=diamond,
			style="filled,solid",
			width=7.8399];
		28 -> 30	[color=black,
			pos="e,585.5,726.46 585.5,750.62 585.5,746.57 585.5,742.16 585.5,737.77"];
		31	[fillcolor="#FFFB81",
			height=0.5,
			label="in_quotes = not in_quotes\l",
			pos="956.5,638.75",
			shape=rectangle,
			style="filled,solid",
			width=2.4514];
		30 -> 31	[color=green,
			label="local_char == '\"' and (j == 0 or file_content[j - 1] != '\\')",
			lp="853,673.38",
			pos="e,867.85,655.18 612.28,691.35 630.12,681.78 654.44,670.34 677.5,664.75 715.77,655.47 815.34,660.88 854.5,656.75 855.18,656.68 855.87,\656.6 856.56,656.53"];
		32	[fillcolor="#FF6752",
			height=0.5,
			label="if not in_quotes:\l",
			pos="697.5,585.75",
			shape=diamond,
			style="filled,solid",
			width=3.1897];
		30 -> 32	[color=red,
			label="(not (local_char == '\"' and (j == 0 or file_content[j - 1] != '\\')))",
			lp="661.5,638.75",
			pos="e,636.38,594.65 516.12,693.95 495.74,686.54 475.67,674.93 463.5,656.75 454.6,643.46 453.03,632.85 463.5,620.75 466.2,617.63 557.56,\605.05 625.31,596.1"];
		31 -> 32	[color=black,
			pos="e,746.67,596.43 868.09,620.34 831.78,613.19 790.66,605.09 757.89,598.64"];
		33	[fillcolor="#FF6752",
			height=0.5,
			label="if local_char == '{':\l",
			pos="697.5,516.5",
			shape=diamond,
			style="filled,solid",
			width=3.8097];
		32 -> 33	[color=green,
			label="not in_quotes",
			lp="738.75,551.12",
			pos="e,697.5,534.99 697.5,567.43 697.5,561.05 697.5,553.63 697.5,546.5"];
		34	[fillcolor="#FF6752",
			height=0.5,
			label="if local_brace_level == 0:\l",
			pos="690.5,325",
			shape=diamond,
			style="filled,solid",
			width=4.8431];
		32 -> 34	[color=red,
			label="(not not in_quotes)",
			lp="518,447.25",
			pos="e,576.02,331.68 645.86,575.37 575.86,561.94 459.5,536.71 459.5,517.5 459.5,517.5 459.5,517.5 459.5,377 459.5,352.27 510.64,339.52 \564.8,332.95"];
		35	[fillcolor="#FFFB81",
			height=0.5,
			label="local_brace_level += 1\l",
			pos="673.5,447.25",
			shape=rectangle,
			style="filled,solid",
			width=2.2014];
		33 -> 35	[color=green,
			label="local_char == '{'",
			lp="740.86,481.88",
			pos="e,679.7,465.62 691.57,498.88 689.14,492.08 686.27,484.03 683.54,476.37"];
		37	[fillcolor="#FF6752",
			height=0.5,
			label="if local_char == '}':\l",
			pos="907.5,447.25",
			shape=diamond,
			style="filled,solid",
			width=3.8097];
		33 -> 37	[color=red,
			label="(local_char != '{')",
			lp="901,481.88",
			pos="e,876.09,461.49 746.66,504.47 762.96,500.48 781.12,495.67 797.5,490.5 820.32,483.29 845.25,473.85 865.6,465.72"];
		35 -> 34	[color=black,
			pos="e,688.08,343.12 675.97,428.76 678.73,409.24 683.24,377.35 686.5,354.27"];
		34 -> 26	[color=red,
			label="(local_brace_level != 0)",
			lp="491,585.75",
			pos="e,451.85,827.84 548.4,328.79 482.07,334.1 417.5,346.99 417.5,377 417.5,612.75 417.5,612.75 417.5,612.75 417.5,633.41 417.33,642.36 \402.5,656.75 366.46,691.73 324.33,649.6 294.5,690 285,702.87 286.62,712.08 294.5,726 324.52,779.02 384.43,808.48 440.97,824.84"];
		40	[fillcolor="#FFFB81",
			height=1.309,
			label="block_end_index = j\lfound_block = file_content[block_start_index:block_end_index + 1]\lresult.append(found_block)\li = block_end_\index\lbreak\l",
			pos="717.5,226.62",
			shape=rectangle,
			style="filled,solid",
			width=5.9826];
		34 -> 40	[color=green,
			label="local_brace_level == 0",
			lp="772.83,290.38",
			pos="e,704.5,274.03 695.2,307.21 697.01,300.76 699.19,292.98 701.47,284.85"];
		40 -> 42	[label=calls,
			lp="730.62,162.88",
			pos="e,717.5,138.52 717.5,179.24 717.5,169.28 717.5,159.04 717.5,149.99",
			style=dashed];
		40 -> 29	[color=black,
			pos="e,919.02,138.71 825.41,179.08 854.39,166.58 884.39,153.64 908.65,143.18"];
		29 -> 12	[color=black,
			pos="e,1030.9,77.103 988.96,101.87 999,95.943 1010.4,89.229 1021,82.95"];
		12 -> 5	[color=black,
			pos="e,1289.7,1422.5 1088,60.189 1160,60.801 1343.5,67.444 1343.5,119.25 1343.5,1360.2 1343.5,1360.2 1343.5,1360.2 1343.5,1379.2 1351,\1388.3 1338.5,1402.5 1332.4,1409.4 1318,1415.1 1300.7,1419.7"];
		37 -> 34	[color=red,
			label="(local_char != '}')",
			lp="950.52,378",
			pos="e,772.28,335.05 905.33,429.29 901.75,409.04 892.53,375.89 869.5,360 854.99,349.99 819.18,342.25 783.37,336.7"];
		38	[fillcolor="#FFFB81",
			height=0.5,
			label="local_brace_level -= 1\l",
			pos="783.5,378",
			shape=rectangle,
			style="filled,solid",
			width=2.1285];
		37 -> 38	[color=green,
			label="local_char == '}'",
			lp="844,412.62",
			pos="e,782.55,396.25 838.47,437.87 817.77,434 798.66,428.59 791.5,421.25 787.82,417.48 785.57,412.58 784.22,407.46"];
		38 -> 34	[color=black,
			pos="e,717.15,340.62 751.75,359.59 743.84,355.25 735.28,350.56 727.15,346.1"];
		16	[fillcolor="#FFFB81",
			height=0.5,
			label="brace_level += 1\l",
			pos="1040.5,226.62",
			shape=rectangle,
			style="filled,solid",
			width=1.7118];
		15 -> 16	[color=green,
			label="char == '{'",
			lp="1106.8,290.38",
			pos="e,1048.2,244.87 1076.4,308.09 1070,293.79 1060.5,272.48 1052.9,255.38"];
		18	[fillcolor="#FF6752",
			height=0.5,
			label="if char == '}':\l",
			pos="1222.5,226.62",
			shape=diamond,
			style="filled,solid",
			width=2.8383];
		15 -> 18	[color=red,
			label="(char != '{')",
			lp="1205.8,290.38",
			pos="e,1209.3,242.74 1118.1,312.64 1127.3,308.92 1137.1,304.35 1145.5,299 1166.5,285.69 1186.9,266.33 1201.5,251.13"];
		16 -> 12	[color=black,
			pos="e,1057.5,77.545 1042.5,208.2 1045.3,183.04 1050.8,135.07 1055.5,94.25 1055.7,92.468 1055.9,90.633 1056.1,88.783"];
		18 -> 12	[color=red,
			label="(char != '}')",
			lp="1123.4,120.25",
			pos="e,1061.1,77.474 1188.8,214.16 1157.9,201.97 1112.9,179.77 1086.2,146.25 1073.1,129.77 1066.4,106.82 1063,88.776"];
		19	[fillcolor="#FFFB81",
			height=0.5,
			label="brace_level -= 1\l",
			pos="1228.5,120.25",
			shape=rectangle,
			style="filled,solid",
			width=1.6389];
		18 -> 19	[color=green,
			label="char == '}'",
			lp="1261.4,162.88",
			pos="e,1227.5,138.51 1223.5,208.39 1224.4,192.53 1225.8,168.69 1226.9,149.95"];
		19 -> 12	[color=black,
			pos="e,1087.9,70.159 1178.7,101.87 1153.2,92.947 1122.5,82.237 1098.6,73.916"];
	}
	subgraph cluster_KEY {
		graph [bb="1360.5,1333.2,1694.5,1594.1",
			fontname="DejaVu Sans Mono",
			label=KEY,
			lheight=0.24,
			lp="1527.5,1581.5",
			lwidth=0.33
		];
		node [fontname="DejaVu Sans Mono"];
		edge [fontname="DejaVu Sans Mono"];
		input	[fillcolor="#afeeee",
			height=0.5,
			pos="1415.5,1436.5",
			shape=parallelogram,
			style=filled,
			width=1.3142];
		call	[fillcolor="#E552FF",
			height=0.5,
			pos="1415.5,1359.2",
			shape=tab,
			style=filled,
			width=0.75];
		input -> call	[pos="e,1415.5,1377.6 1415.5,1418 1415.5,1409.4 1415.5,1398.7 1415.5,1388.9",
			style=invis];
		default	[fillcolor="#FFFB81",
			height=0.5,
			pos="1535.5,1359.2",
			shape=rectangle,
			style=filled,
			width=0.80556];
		if	[fillcolor="#FF6752",
			height=0.5,
			pos="1410.5,1542.9",
			shape=diamond,
			style=filled,
			width=0.75];
		if -> input	[pos="e,1414.7,1454.9 1411.3,1525.1 1412.1,1509.2 1413.2,1485.1 1414.1,1466.2",
			style=invis];
		for	[fillcolor="#FFBE52",
			height=0.5,
			pos="1482.5,1542.9",
			shape=hexagon,
			style=filled,
			width=0.75];
		return	[fillcolor="#98fb98",
			height=0.5,
			pos="1535.5,1436.5",
			shape=parallelogram,
			style=filled,
			width=1.5285];
		for -> return	[pos="e,1526.7,1454.8 1491.3,1524.6 1499.5,1508.4 1512,1483.8 1521.6,1464.9",
			style=invis];
		while	[fillcolor="#FFBE52",
			height=0.5,
			pos="1565.5,1542.9",
			shape=hexagon,
			style=filled,
			width=1.0687];
		return -> default	[pos="e,1535.5,1377.6 1535.5,1418 1535.5,1409.4 1535.5,1398.7 1535.5,1388.9",
			style=invis];
		try	[fillcolor=orange,
			height=0.5,
			pos="1654.5,1542.9",
			shape=Mdiamond,
			style=filled,
			width=0.89559];
		raise	[fillcolor="#98fb98",
			height=0.5,
			pos="1647.5,1436.5",
			shape=house,
			style=filled,
			width=1.0899];
		try -> raise	[pos="e,1648.6,1454.6 1653.4,1525.1 1652.3,1509.1 1650.7,1484.8 1649.4,1465.8",
			style=invis];
	}
	1	[fillcolor="#FFFB81",
		height=0.5,
		label="def extract_subgraph(file_content):...\l",
		pos="123.5,1542.9",
		shape=rectangle,
		style="filled,solid",
		width=3.4306];
}


"""

res = GraphParser.GraphParser(input_str=input_str)

# print(res.graphViz())