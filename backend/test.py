from app.parsers import GraphParser
f = open("C:\\Users\\ACER\\OneDrive - Institut Teknologi Bandung\\Tugas Akhir\\Kode\\Tugas_Akhir\\backend\\test.txt","r")
content = f.read()
input_str = content

parser = GraphParser.GraphParser(input_str)
# print(parser.graphViz())
collection = parser.collectionSubGraph()
pirnttt = parser.graphViz()
# print("Subgraph Collection:", collection)
# for name, graph in collection.items():
# 	print(f"Subgraph Name: {name}")
# 	print(f"subgraph type: {type}")
# 	print(graph)
# 	print("\n")
# print(parser.collectionSubGraph())

# from graphviz import Source
# # Create a Source object
# graph = Source(parser.graphViz())

# # Render the graph to SVG format
# svg_data = graph.pipe(format='svg')

# # Convert SVG bytes to string and print
# svg_text = svg_data.decode('utf-8')
# print(svg_text)

# print