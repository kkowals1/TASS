import graph
import TASS_app_gui
import data

graphik = graph.create_graph()

airlines = data.create_list_of_airlines()
airports = data.create_list_of_airports()
#for a in airports:
#    print(str(a.airport_id) + " " + str(a.rating))
routes = data.create_list_of_routes()

ee = graph.find_best_routes(graphik, "1460", "1197")
print(list(ee))
for a in ee:
    print(len(a))
    for b in a:
        print (b)

rating = data.get_airport_rating_by_id(airports=airports, airport_id="302")
print(rating)

graph.calculate_route_score()



