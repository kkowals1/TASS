import networkx
import openpyxl


def create_graph() -> networkx.MultiGraph:
    wb = openpyxl.load_workbook(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\routes1.xlsx')
    sheet = wb.active
    l = []
    sheet_length = len(sheet['A'])
    for i in range(2, sheet_length+1):
        c1 = sheet["C" + str(i)]
        c2 = sheet["E" + str(i)]
        l.append((c1.value, c2.value))
    f = open(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\graph.txt', 'w+')
    for item in l:
        f.write(item[0] + " " + item[1] + " 1" + "\n")
    f.close()
    graph: networkx.MultiGraph = networkx.read_weighted_edgelist(
        r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\graph.txt',
        create_using=networkx.MultiGraph)
    print("graph: ", graph)
    print("nodes: ", graph.nodes)
    print("edges: ", graph.edges)
    return graph


def find_route(given_graph: networkx.Graph, node1: str, node2: str) -> list:
    test = networkx.all_shortest_paths(given_graph, source=node1, target=node2)
    print([p for p in test])
    return test


graph = create_graph()
print(find_route(graph, 'DUS', 'BOD'))
