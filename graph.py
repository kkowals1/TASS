import networkx
import openpyxl

import data


def create_graph() -> networkx.MultiGraph:
    wb = openpyxl.load_workbook(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\routes1.xlsx')
    sheet = wb.active
    l = []
    sheet_length = len(sheet['A'])
    for i in range(2, sheet_length + 1):
        c1 = sheet["D" + str(i)]
        c2 = sheet["F" + str(i)]
        l.append((c1.value, c2.value))
    f = open(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\graph.txt', 'w+')
    for item in l:
        f.write(str(item[0]) + " " + str(item[1]) + " 1" + "\n")
    f.close()
    graph: networkx.MultiGraph = networkx.read_weighted_edgelist(
        r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\graph.txt',
        create_using=networkx.MultiGraph)
    print("graph: ", graph)
    print("nodes: ", graph.nodes)
    print("edges: ", graph.edges)
    return graph


def find_best_routes(given_graph: networkx.Graph, node1: str, node2: str, ) -> str:
    paths = networkx.all_shortest_paths(given_graph, source=node1, target=node2)
    return paths


def find_best_connection(given_graph: networkx.Graph, node1: str, node2: str, airlines: list, airports: list,
                         routes: list) -> str:
    paths = list(networkx.all_shortest_paths(given_graph, source=node1, target=node2))
    best_route = str

    return "HAHAH"


def calculate_route_score(airports_ids: list, airlines: list, airports: list, routes: list) -> float:
    to_return = 0.0
    airports_score = 0.0
    airlines_score = 0.0
    for airport in airports_ids:
        airports_score += data.get_airport_rating_by_id(airports=airports, airport_id=airport.airport_id)



    for airline in airlines:
        airlines_score += data.get_airline_rating_by_id(airlines=airlines, airline_id=airline.airline_id)
    return to_return
