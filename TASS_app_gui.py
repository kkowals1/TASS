import tkinter as tk
import data
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import graph

graphik = graph.create_graph()
# Stwórz listę objektów linii lotniczych, lotnisk oraz tras
airlines = data.create_list_of_airlines()
airports = data.create_list_of_airports()
routes = data.create_list_of_routes()


def list_of_airports_names():
    l = []
    for i in airports:
        name = i.name
        l.append(name)
    return l


def search_source(event):
    value = event.widget.get()
    if value == '':
        source_combobox['values'] = list_of_airports_names()
    else:
        temp_list = []
        for item in list_of_airports_names():
            if value.lower() in item.lower():
                temp_list.append(item)
        source_combobox['values'] = temp_list


def search_destination(event):
    value = event.widget.get()
    if value == '':
        destination_combobox['values'] = list_of_airports_names()
    else:
        temp_list = []
        for item in list_of_airports_names():
            if value.lower() in item.lower():
                temp_list.append(item)
        destination_combobox['values'] = temp_list


def find_result():
    source = source_combobox.get()
    destination = destination_combobox.get()

    if source and destination:
        if source == destination:
            tk.messagebox.showwarning(title="Error", message="Source and destination airports cannot be the same!")
        else:
            source_id = str(data.get_id_by_airport_name(airports, source))
            destination_id = str(data.get_id_by_airport_name(airports, destination))
            print(source_id, destination_id)
            result = "123"
            score = graph.find_best_connection(given_graph=graphik, node1=source_id, node2=destination_id, airlines=airlines,
                                               airports=airports, routes=routes)
            print(score)

            # answer.insert(INSERT, result)
            # answer.pack()
            my_label.config(text=score)


    else:
        tk.messagebox.showwarning(title="Error", message="Source and destination airports are required!")


window = tk.Tk()
window.title("Flying App")

frame = tk.Frame(window)
frame.pack()

# Flight parameters frame
flight_params_frame = tk.LabelFrame(frame, text="Flight parameters")
flight_params_frame.grid(row=0, column=0, padx=20, pady=10)

source_airport_label = tk.Label(flight_params_frame, text="Source airport:")
source_combobox = ttk.Combobox(flight_params_frame, width=40, values=list_of_airports_names())
source_airport_label.grid(row=0, column=0)
source_combobox.grid(row=1, column=0)
source_combobox.bind('<KeyPress>', search_source)

destination_airport_label = tk.Label(flight_params_frame, text="Destination airport:")
destination_combobox = ttk.Combobox(flight_params_frame, width=40, values=list_of_airports_names())
destination_airport_label.grid(row=0, column=1)
destination_combobox.grid(row=1, column=1)
destination_combobox.bind('<KeyPress>', search_destination)

confirm_button = tk.Button(flight_params_frame, text="Find my flights", command=find_result)
confirm_button.grid(row=1, column=2, sticky="news", padx=20, pady=10)

# Improve padding
for widget in flight_params_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Search results
results_frame = tk.LabelFrame(frame, text="Search results:")
results_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check = tk.Label(results_frame)
terms_check.grid(row=0, column=0, padx=10, pady=10)

# Create a Label widget
my_label = Label(terms_check, text="")
my_label.pack()
# answer = Text(terms_check, width=50, height=1)

window.mainloop()
