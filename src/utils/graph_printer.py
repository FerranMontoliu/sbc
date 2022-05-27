from graphviz import Source

from model.connection import Connection


def print_graph(connections: [Connection]) -> None:
    graphviz_str: str = 'strict digraph tree {\n' \
                        '\tnode [label="\\N", shape=box, style="rounded,filled", colorscheme=blues5, color=5, fillcolor=1, width="1.2", fontname="Lucida Sans Unicode", fontsize=12];\n' \
                        '\tedge [colorscheme=blues5, color=5, fontsize=11, fontname="Lucida Sans Unicode"];\n'

    for connection in connections:
        graphviz_str += f'\t"{connection.from_name}" -> "{connection.to_name}"\n'

    graphviz_str += '}'
    source: Source = Source(source=graphviz_str,
                            filename='graph.gv',
                            directory='../assets/',
                            format='png')
    source.view()
