A fi de comprendre com s'ha d'executar aquest projecte, es presenta la següent ajuda:

1. Instal·lar `Python 3.10.4`
2. Executar la comanda `pip install -r requirements.txt` o bé `pip3 install -r requirements.txt` per instal·lar les dependències necessàries.
3. En cas de voler fer ús de la funcionalitat per visualitzar el graph de les ciutats en format PNG, descarregar i instal·lar Graphviz (https://graphviz.org/download/).
4. Executar el programa amb la comanda següent:

Comanda: `main.py [-h] -f dataset_path -o origin -d destination -a algorithm -hf heuristic_function_name [-p]`

Opcions:

    -h, --help          show this help message and exit
    -f dataset_path, --file dataset_path
                        Path of the dataset.
    -o origin, --origin origin
                        Name of the origin city.
    -d destination, --destination destination
                        Name of the destination city.
    -a algorithm, --algorithm algorithm
                        Name of the algorithm. Choices: ['a*', 'csp', 'dijkstra'].
    -hf heuristic_function_name, --heuristic heuristic_function_name
                        Name of the heuristic function. Choices: ['distance', 'duration', 'duration_distance', 'weighted'].
    -p, --print-graph     [OPTIONAL] Enable generation of graph in GV and PNG format.
