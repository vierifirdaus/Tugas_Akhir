from graphviz import Source

# Define your Graphviz source in DOT format
dot_source = """
digraph G {
    A -> B;
    B -> C;
    C -> A;
}
"""

# Create a Source object
graph = Source(dot_source)

# Render the graph to SVG format
svg_data = graph.pipe(format='svg')

# Convert SVG bytes to string and print
svg_text = svg_data.decode('utf-8')
print(svg_text)