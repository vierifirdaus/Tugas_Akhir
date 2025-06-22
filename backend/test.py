# from app.parsers import GraphParser

# # Pakai context manager untuk buka file, jadi aman otomatis close
# with open(r"C:\Users\ACER\OneDrive - Institut Teknologi Bandung\Tugas Akhir\Kode\Tugas_Akhir\backend\test.txt", "r") as f:
#     input_str = f.read()

# parser = GraphParser.GraphParser(input_str)
# # test print nama type dari subgraph 
# parser.print()
from app.parsers import GraphParser,Node,Edge
dot_format = r"""
94 -> 97  [color=green,
                                label="getattr(self.parent, 'parent', None) == None",
                                lp="2116.1,1598.9",        
                                pos="e,1994.3,1574.7 2088.7,1641.9 2039.7,1636.1 1995.8,1625.7 1980,1607.5 1972.6,1599 1977.1,1589.9 1985.6,1581.8"];               
"""
node_format = r"""
1 [fillcolor="#FFFB81",
                height=41.66,
                label="import regex\limport re\limport graphviz\lfrom .Graph import Graph\lfrom .Node import Node\lfrom .NodeLabel import NodeLabel\lfrom \
.Edge import Edge\lfrom .EdgeLabel import EdgeLabel\lclass GraphParser:\l\l    def __init__(self, input_str, parent=None, types=\
None):\l        self.name = None\l        self.graph = None\l        self.nodeLabel = None\l        self.edgeLabel = None\l        \
self.subGraph = []\l        self.node = []\l        self.edge = []\l        self.type = None\l        self.parent = parent\l        \
self.typeCode = types\l        self.from_str(input_str)\l\l    def from_str(self, input_str):\l        header_match = regex.match('(\
subgraph|digraph)?\...',\l            input_str.strip())\l        if header_match:\l            raw_name = header_match.group(2) \
or 'Unnamed'\l            self.name = re.sub('^cluster\\d*_?', '', raw_name)\l            if self.name == '_init__':\l                \
self.name = '__init__'\l        else:\l            self.name = 'Unnamed'\l        start = input_str.find('{') + 1\l        end = \
input_str.rfind('}')\l        if start == 0 or end == -1:\l            return\l        content = input_str[start:end].strip()\l        \
patterns = ['subgraph\\s+\\w+\\s*...',\l            '(?:graph|node|edge)\...',\l            '\\w+\\s*->\\s*\\w+\\...', '\\w+\\s*\\[[^\\]]*\\...']\l        \
full_pattern = '|'.join(patterns)\l        blocks = [m.group(0) for m in regex.finditer(full_pattern, content,\l            regex.DOTALL)]\l        \
for block in blocks:\l            block = block.strip()\l            if not block:\l                continue\l            if block.startswith('\   
subgraph') or block.startswit...'digraph'):\l                sub_parser = GraphParser(block, parent=self, types=self.\l                    \       
typeCode)\l                if sub_parser.name != 'KEY':\l                    self.subGraph.append(sub_parser)\l            elif \
block.startswith('graph'):\l                self.graph = Graph(block)\l            elif block.startswith('node'):\l                \
self.nodeLabel = NodeLabel(block)\l            elif block.startswith('edge'):\l                self.edgeLabel = EdgeLabel(block)\l            \    
elif '->' in block or '--' in block:\l                try:\l                    self.edge.append(Edge(block))\l                except \
Exception as e:\l                    print(f'Failed to parse edge...')\l            else:\l                try:\l                    \
self.node.append(Node(block))\l                except Exception as e:\l                    print(f'Failed to parse node...')\l        \
for sub in self.subGraph:\l            sub.assign_type()\l        self.assign_type()\l\l    def assign_type(self):\l        if self.parent \       
is None:\l            self.type = 'dot'\l            return\l        if self.typeCode is not None:\l            if self.name in \
self.typeCode['function']:\l                self.type = 'function'\l                return\l        if self.subGraph:\l            \
if getattr(self.parent, 'parent', None) == None:\l                self.type = 'class'\l                return\l        if getattr(\
getattr(self.parent, 'parent', None), 'parent', None\l            ) == None and getattr(self.parent, 'name', None) != 'main':\l            \       
self.type = 'method'\l            return\l        self.type = None\l\l    def print(self, indent=0):\l        indent_str = '   ' * \
indent\l        print(f'{indent_str}Graph Na...')\l        print(f'{indent_str}Type    ...')\l        print(f'{indent_str}Graph   \
...')\l        print(f'{indent_str}Node Lab...')\l        print(f'{indent_str}Edge Lab...')\l        print(f'{indent_str}Nodes   \
...')\l        for n in self.node:\l            print(f'{indent_str}  -', n)\l        print(f'{indent_str}Edges   ...')\l        \
for e in self.edge:\l            print(f'{indent_str}  -', e)\l        print(f'{indent_str}Subgraph...')\l        for sg in self.subGraph:\l            \
print(f'{indent_str}  - Subg...')\l            sg.print(indent=indent + 1)\l\l    def collectionSubGraph(self):\l        res = {}\l        \       
for subgraph in self.subGraph:\l            if subgraph.name == 'KEY':\l                continue\l            res[subgraph.name] = \
subgraph.graphViz()\l        return res\l\l    def collectionMethod(self):\l        res = []\l        for subgraph in self.subGraph:\l            \
if subgraph.type == 'class':\l                method_arr = []\l                for method in subgraph.subGraph:\l                    \
if method.type == 'method':\l                        svg_str = graphviz.Source(method.graphViz(), format\l                            ='\
svg').pipe().decode('utf-8')\l                        method_arr.append({method.name: svg_str})\l                if method_arr:\l                  
  \
res.append({subgraph.name: method_arr})\l            res += subgraph.collectionMethod()\l        return res\l\l    def collectionFunction(\        
self):\l        res = []\l        for subgraph in self.subGraph:\l            if subgraph.type == 'function':\l                print('\
Function name:', subgraph.graphViz())\l                svg_str = graphviz.Source(subgraph.graphViz(), format='svg'\l                    )\
.pipe().decode('utf-8')\l                res.append({subgraph.name: svg_str})\l            res += subgraph.collectionFunction()\l        \
return res\l\l    def graphViz(self, indent=0):\l        indent_str = '  ' * indent\l        lines = []\l        if self.name:\l            \      
is_digraph = False\l            if 'cfg' in self.name:\l                is_digraph = True\l                self.name = 'MainCode'\l            \   
if self.parent is None:\l                is_digraph = True\l            if indent == 0:\l                is_digraph = True\l            \
graph_type = 'digraph' if is_digraph else ...'subgraph'\l            lines.append(f'{indent_str}{graph_t...')\l        else:\l            \        
lines.append(f'{indent_str}digraph ...')\l        if self.graph:\l            lines.append(f'{indent_str} {self.g...')\l        \
if self.nodeLabel:\l            lines.append(f'{indent_str}  {self....')\l        if self.edgeLabel:\l            lines.append(f'{\
indent_str}  {self....')\l        for subgraph in self.subGraph:\l            lines.append(f'{subgraph.graphViz(i...')\l        \
for node in self.node:\l            lines.append(f'{indent_str}  {node....')\l        for edge in self.edge:\l            lines.append(\
f'{indent_str}  {edge....')\l        lines.append(f'{indent_str}}}')\l        return '\n'.join(lines)\l",
                pos="232.25,3492.5",
                shape=rectangle,
                style="filled,solid",
                width=6.4514];
"""
# parser = Edge.Edge(dot_format)
# print(parser)


eg2 = r"""
14        [pos="e,1116.2,1577.9 1229.1,1631.1 1198.8,1617.5 1158.1,1598.4 1126.5,1583"];
"""

node = Node.Node(eg2)
print(node)