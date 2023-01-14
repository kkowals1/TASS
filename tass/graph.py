from typing import Type

import networkx
import openpyxl

import tass.data as data

ROUTES_FILE = r'files\routes1.xlsx'
GRAPH_FILE = r'files\graph.txt'

class RouteScore:
    def __init__(self, score: float, airlines: list):
        self.score = score
        self.airlines = airlines


def create_graph() -> networkx.MultiGraph:
    wb = openpyxl.load_workbook(ROUTES_FILE)
    sheet = wb.active
    l = []
    sheet_length = len(sheet['A'])
    for i in range(2, sheet_length + 1):
        c1 = sheet["D" + str(i)]
        c2 = sheet["F" + str(i)]
        l.append((c1.value, c2.value))
    f = open(GRAPH_FILE, 'w+')
    for item in l:
        f.write(str(item[0]) + " " + str(item[1]) + " 1" + "\n")
    f.close()
    graph: networkx.MultiGraph = networkx.read_weighted_edgelist(
        GRAPH_FILE,
        create_using=networkx.MultiGraph)
    return graph


def find_best_routes(given_graph: networkx.Graph, node1: str, node2: str, ) -> str:
    paths = networkx.all_shortest_paths(given_graph, source=node1, target=node2)
    return paths


def find_best_connection(given_graph: networkx.Graph, node1: str, node2: str, airlines: list, airports: list,
                         routes: list) -> str:
    paths = list(networkx.all_shortest_paths(given_graph, source=node1, target=node2))
    best_route_airlines = []
    best_route_score = 0.0
    best_route_airports = []
    for path in paths:
        result = calculate_route_score(airports_ids=path, airlines=airlines, airports=airports, routes=routes)
        result_score = result.score
        result_list = result.airlines
        if best_route_score <= result_score:
            best_route_score = result_score
            best_route_airlines = result_list
            best_route_airlines = result_list
            best_route_airports = path

    return prepare_result_string(airlines=best_route_airlines, score=best_route_score, airports=best_route_airports, all_airlines=airlines, all_airports=airports)


def calculate_route_score(airports_ids: list, airlines: list, airports: list, routes: list) -> RouteScore:
    to_return = 0.0
    airports_score = 0.0
    airlines_score = 0.0
    for airport_id in airports_ids:
        score = data.get_airport_rating_by_id(airports=airports, airport_id=airport_id)
        airports_score += float(score)

    airlines_on_route = []

    for i in range(0, len(airports_ids) - 1):
        dest = airports_ids[i]
        src = airports_ids[i + 1]
        airlines_ids_set = data.get_airlines_by_destination_and_source(routes=routes, destination=dest,
                                                                       source=src)
        airlines_ids = list(airlines_ids_set)
        airline_id = str
        if len(airlines_ids) > 1:
            airline_id = find_best_airline(airlines_ids=airlines_ids, airlines=airlines)[0]
        else:
            airline_id = airlines_ids[0]
        airlines_on_route.append(str(airline_id))

    for airline in airlines_on_route:
        airlines_score += float(data.get_airline_rating_by_id(airlines=airlines, airline_id=airline))

    to_return += airports_score
    to_return += airlines_score
    return RouteScore(score=to_return, airlines=airlines_on_route)


def find_best_airline(airlines_ids: list, airlines: list) -> Type[tuple]:
    to_return = str
    airline_score = 0.0
    for airline in airlines_ids:
        to_compare = data.get_airline_rating_by_id(airlines=airlines, airline_id=airline)
        if to_compare >= airline_score:
            to_return = str(airline)
            airline_score = to_compare
    tup = (airline_score, to_return)
    return tup


def prepare_result_string(airlines: list, score: str, airports: list, all_airlines: list, all_airports: list) -> str:
    airline_names = []
    airport_names = []
    to_return = "Best route:\n"
    for airline in airlines:
        name = data.get_airline_name_by_id(airlines=all_airlines, airline_id=airline)
        airline_names.append(name)
    for airport in airports:
        name = data.get_airport_name_by_id(airports=all_airports, airport_id=airport)
        airport_names.append(name)
    airports_counter = 0
    airlines_counter = 0
    length = len(airport_names) + len(airline_names)
    for i in range(0, length):
        if i % 2 == 0:
            to_return += airport_names[airports_counter]
            airports_counter += 1
            to_return += " "

        else:
            to_return += '('
            to_return += airline_names[airlines_counter]
            to_return += ')'
            airlines_counter += 1
            to_return += " -> "

    to_return += "\n"
    to_return += "Route score: "
    formatted_score = '%.2f' % score
    to_return += str(formatted_score)

    return to_return



























