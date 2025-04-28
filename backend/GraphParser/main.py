from GraphParser import GraphParser

input_str = r"""
digraph cluster0example {
    graph [compound=True fontname="DejaVu Sans Mono" label=example pack=False rankdir=TB ranksep=0.02]
    node [fontname="DejaVu Sans Mono"]
    edge [fontname="DejaVu Sans Mono"]
    1 [label="class Circle:...\l" fillcolor="#FFFB81" shape=rectangle style="filled,solid"]
    subgraph cluster0Circle {
        graph [compound=True fontname="DejaVu Sans Mono" label=Circle pack=False rankdir=TB ranksep=0.02]
        node [fontname="DejaVu Sans Mono"]
        edge [fontname="DejaVu Sans Mono"]
        3 [label="def __init__(self, radius):...\ldef area(self):...\l" fillcolor="#FFFB81" shape=rectangle style="filled,solid"]
        subgraph cluster0__init__ {
            graph [compound=True fontname="DejaVu Sans Mono" label=__init__ pack=False rankdir=TB ranksep=0.02]
            node [fontname="DejaVu Sans Mono"]
            edge [fontname="DejaVu Sans Mono"]
            5 [label="self.radius = radius\l" fillcolor="#FFFB81" shape=rectangle style="filled,solid"]
        }
        subgraph cluster0area {
            graph [compound=True fontname="DejaVu Sans Mono" label=area pack=False rankdir=TB ranksep=0.02]
            node [fontname="DejaVu Sans Mono"]
            edge [fontname="DejaVu Sans Mono"]
            8 [label="return 3.14 * self.radius ** 2\l" fillcolor="#98fb98" shape=parallelogram style="filled,solid"]
        }
    }
}

"""

parser = GraphParser(input_str)
parser.print()