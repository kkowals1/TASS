import tass.graph as graph
import tass.data as data

graphik = graph.create_graph()
routes = data.create_list_of_routes()
airlines = data.create_list_of_airlines()
airports = data.create_list_of_airports(routes=routes)
for a in airports:
    print(str(a.airport_id) + " " + str(a.name))
aa = graph.find_best_routes(graphik, "1460", "347")


ee = graph.find_best_routes(graphik, "1460", "1197")
lista = list(aa)

score = graph.find_best_connection(given_graph=graphik, node1="1460", node2="347", airlines=airlines, airports=airports, routes=routes)
print(score)



