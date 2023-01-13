import graph
import TASS_app_gui
import data

graphik = graph.create_graph()

airlines = data.create_list_of_airlines()
airports = data.create_list_of_airports()
#for a in airports:
#    print(str(a.airport_id) + " " + str(a.rating))
routes = data.create_list_of_routes()
aa = graph.find_best_routes(graphik, "1460", "347")


ee = graph.find_best_routes(graphik, "1460", "1197")
lista = list(aa)

score = graph.find_best_connection(given_graph=graphik, node1="1460", node2="347", airlines=airlines, airports=airports, routes=routes)
print(score)



