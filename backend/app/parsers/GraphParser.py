import regex
import re
import graphviz
from .Graph import Graph
from .Node import Node
from .NodeLabel import NodeLabel
from .Edge import Edge
from .EdgeLabel import EdgeLabel

class GraphParser:
    def __init__(self, input_str, parent=None):
        self.name = None
        self.graph = None
        self.nodeLabel = None
        self.edgeLabel = None
        self.subGraph = []
        self.node = []
        self.edge = []
        self.type = None
        self.parent = parent  
        self.from_str(input_str)

    def from_str(self, input_str):
        header_match = regex.match(r'(subgraph|digraph)?\s*(\w+)?\s*{', input_str.strip())
        if header_match:
            raw_name = header_match.group(2) or "Unnamed"
            self.name = re.sub(r'^cluster\d*_?', '', raw_name)
        else:
            self.name = "Unnamed"

        start = input_str.find("{") + 1
        end = input_str.rfind("}")
        if start == -1 or end == -1:
            return

        content = input_str[start:end].strip()
        blocks = regex.findall(
            r'(?:[A-Za-z0-9_]+\s*\[.*?\];)|'
            r'(?:[A-Za-z0-9_]+\s*->\s*[A-Za-z0-9_]+\s*\[.*?\])|'
            r'(?:graph\s*\[.*?\])|'
            r'(?:node\s*\[.*?\])|'
            r'(?:edge\s*\[.*?\])|'
            r'(?:subgraph\s+\w+\s*{(?:(?R)|[^{}])*})|'
            r'(?:digraph\s+\w+\s*{(?:(?R)|[^{}])*})',
            content,
            regex.DOTALL
        )
        for block in blocks:
            block = block.strip()
            if block.startswith("graph"):
                self.graph = Graph(block)
            elif block.startswith("node"):
                self.nodeLabel = NodeLabel(block)
            elif block.startswith("edge"):
                self.edgeLabel = EdgeLabel(block)
            elif block.startswith("subgraph") or block.startswith("digraph"):
                sub_parser = GraphParser(block, parent=self)  
                if sub_parser.name == "KEY":
                    continue
                self.subGraph.append(sub_parser)
            elif "->" in block:
                try:
                    self.edge.append(Edge(block))
                except Exception as e:
                    print(f"Failed to parse edge: {e}")
            elif regex.match(r'^[A-Za-z0-9_]+\s*\[.*\];$', block, regex.DOTALL):
                try:
                    self.node.append(Node(block))
                except Exception as e:
                    print(f"Failed to parse node: {e}")
            else:
                print(f"[!] Tidak dikenali dan dilewati: {block}")

        # assign type setelah seluruh subgraph di-parse
        for sub in self.subGraph:
            sub.assign_type()
        self.assign_type()

    def assign_type(self):
        if self.parent is None:
            self.type = 'dot'
            return

        if self.name and self.name.lower() == 'main':
            self.type = 'main'
            return


        if self.subGraph:
            if getattr(self.parent, 'parent', None) == None:
                self.type = 'class'
                return

        if getattr(getattr(self.parent, 'parent', None), 'parent', None) == None and getattr(self.parent, 'name', None) != 'main':
            self.type = 'method'
            return

        self.type = None

    def print(self, indent=0):
        indent_str = "   " * indent
        print(f"{indent_str}Graph Name: {self.name}")
        print(f"{indent_str}Type      : {self.type}")
        print(f"{indent_str}Graph     : {self.graph}")
        print(f"{indent_str}Node Label: {self.nodeLabel}")
        print(f"{indent_str}Edge Label: {self.edgeLabel}")
        print(f"{indent_str}Nodes     :")
        for n in self.node:
            print(f"{indent_str}  -", n)
        print(f"{indent_str}Edges     :")
        for e in self.edge:
            print(f"{indent_str}  -", e)
        print(f"{indent_str}Subgraphs :")
        for sg in self.subGraph:
            print(f"{indent_str}  - Subgraph: {sg.name} (type: {sg.type})")
            sg.print(indent=indent+1)

    def collectionSubGraph(self):
        res = {}
        for subgraph in self.subGraph:
            if subgraph.name == "KEY":
                continue
            res[subgraph.name] = subgraph.graphViz()
        return res
    
    import graphviz

    def collectionMethod(self):
        res = []
        print("masuk collectioin methodd")
        for subgraph in self.subGraph:
            # print(f"class name: {subgraph.name} (type: {subgraph.type})")
            if subgraph.type == "class":
                method_arr = []
                for method in subgraph.subGraph:
                    print(f"method name: {method.name} (type: {method.type})")
                    if method.type == "method":
                        svg_str = graphviz.Source(method.graphViz(), format='svg').pipe().decode('utf-8')
                        method_arr.append({method.name: svg_str})
                if method_arr:
                    res.append({subgraph.name: method_arr})
            res += subgraph.collectionMethod()
        return res

    
    

    def graphViz(self, indent=0):
        indent_str = "  " * indent
        lines = []
        if self.name:
            is_digraph = False
            if "cfg" in self.name:
                is_digraph = True
            if self.parent is None:
                is_digraph = True 
            if indent == 0:
                is_digraph = True
            graph_type = "digraph" if is_digraph else "subgraph"
            lines.append(f"{indent_str}{graph_type} {self.name} {{")
        else:
            lines.append(f"{indent_str}digraph {{")
        
        # Global graph attributes
        if self.graph:
            lines.append(f"{indent_str} {self.graph.graphViz()}")
        
        # Default node attributes
        if self.nodeLabel:
            lines.append(f"{indent_str}  {self.nodeLabel.graphViz()}")
        
        # Default edge attributes
        if self.edgeLabel:
            lines.append(f"{indent_str}  {self.edgeLabel.graphViz()}")
        
        # Subgraphs
        for subgraph in self.subGraph:
            lines.append(f"{subgraph.graphViz(indent + 1)}")

        # Nodes
        for node in self.node:
            lines.append(f"{indent_str}  {node.graphViz()}")
        # Edges
        for edge in self.edge:
            lines.append(f"{indent_str}  {edge.graphViz()}")
        # Closing brace
        lines.append(f"{indent_str}}}")
        
        return "\n".join(lines)
