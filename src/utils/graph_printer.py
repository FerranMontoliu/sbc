from graphviz import Source
from model.city import City


def print_graph(cities: [City]) -> None:
    print('Printing graph...')
    graphviz_str: str = 'strict digraph tree {\n' \
                        '\tnode [label="\\N", shape=box, style="rounded,filled", colorscheme=blues5, color=5, fillcolor=1, width="1.2", fontname="Lucida Sans Unicode", fontsize=12];\n' \
                        '\tedge [colorscheme=blues5, color=5, fontsize=11, fontname="Lucida Sans Unicode"];\n\n'

    for city in cities:
        for connection in city.connections:
            graphviz_str += f'\t"{city.name}" -> "{cities[connection.to].name}"\t[label="Distance: {connection.distance}\\n Duration: {connection.duration}"];\n'

    graphviz_str += '}'
    source: Source = Source(source=graphviz_str,
                            filename='graph.gv',
                            directory='../assets/',
                            format='png')
    source.view()
    print('Graph printed successfully.')
