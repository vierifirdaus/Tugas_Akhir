import re
import regex
from Graph import Graph
from Node import Node
from NodeLabel import NodeLabel
from Edge import Edge

class GraphParser:
    def __init__(self, input_str, parent=None):
        self.name = None
        self.graph = None
        self.nodeLabel = None
        self.edgeLabel = None
        self.subGraph = []
        self.node = []
        self.edge = []
        self.parent = parent  
        self.from_str(input_str)

    def from_str(self, input_str):
        header_match = re.match(r'(subgraph|digraph)?\s*(\w+)?\s*{', input_str.strip())
        if header_match:
            self.name = header_match.group(2) or "Unnamed"

        start = input_str.find("{") + 1
        end = input_str.rfind("}")
        if start == -1 or end == -1:
            return

        content = input_str[start:end].strip()

        blocks = regex.findall(
            r'(?:\d+\s*\[.*?\])|'
            r'(?:\d+\s*->\s*\d+\s*\[.*?\])|'
            r'(?:graph\s*\[.*?\])|'
            r'(?:node\s*\[.*?\])|'
            r'(?:edge\s*\[.*?\])|'
            r'(?:subgraph\s+\w+\s*{(?:(?R)|[^{}])*})|'
            r'(?:digraph\s+\w+\s*{(?:(?R)|[^{}])*})',
            content,
            regex.DOTALL
        )


        for block in blocks:
            # print(f"index {blocks.index(block)}: {block}")
            block = block.strip()
            if block.startswith("graph"):
                self.graph = Graph.from_str(block)
            elif block.startswith("node"):
                self.nodeLabel = NodeLabel.from_str(block)
            elif block.startswith("edge"):
                self.edgeLabel = NodeLabel.from_str(block)
            elif block.startswith("subgraph") or block.startswith("digraph"):
                # print("[!] Subgraph ditemukan:", block)
                sub_parser = GraphParser(block, parent=self)  # Pass parent reference
                self.subGraph.append(sub_parser)
            elif "->" in block:
                try:
                    self.edge.append(Edge(block))
                except Exception as e:
                    print(f"Failed to parse edge: {e}")
            elif re.match(r'^\d+\s+\[.*\]$', block, re.DOTALL):
                try:
                    self.node.append(Node(block))
                except Exception as e:
                    print(f"Failed to parse node: {e}")
            else:
                print(f"[!] Tidak dikenali dan dilewati: {block}")

    def print(self, indent=0):
        indent_str = "   " * indent
        print(f"{indent_str}Graph Name: {self.name}")
        print(f"{indent_str}Graph:", self.graph)
        print(f"{indent_str}Node Label:", self.nodeLabel)
        print(f"{indent_str}Edge Label:", self.edgeLabel)
        print(f"{indent_str}Nodes:")
        for n in self.node:
            print(f"{indent_str}  -", n)
        print(f"{indent_str}Edges:")
        for e in self.edge:
            print(f"{indent_str}  -", e)
        
        print(f"{indent_str}Subgraphs:")
        for sg in self.subGraph:
            print(f"{indent_str}  - Subgraph: {sg.name}")
            sg.print(indent=indent+1)  