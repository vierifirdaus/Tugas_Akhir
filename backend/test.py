# from app.parsers import GraphParser

# # Pakai context manager untuk buka file, jadi aman otomatis close
# with open(r"C:\Users\ACER\OneDrive - Institut Teknologi Bandung\Tugas Akhir\Kode\Tugas_Akhir\backend\test.txt", "r") as f:
#     input_str = f.read()

# parser = GraphParser.GraphParser(input_str)
# # test print nama type dari subgraph 
# parser.print()
from app.parsers import Node
input = r"""
19 [fillcolor="#FFFB81", height=0.5, label="self.items = []\l", pos="1107.5,456.88", shape=rectangle, style="filled,solid", width=1.4306]
"""
node = Node.Node(input)
print(node.graphViz())

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