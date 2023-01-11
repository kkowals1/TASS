import tkinter as tk
import data
from tkinter import ttk
from tkinter import messagebox

list_of_airports = data.create_list_of_airports()


def list_of_airports_names():
    l = []
    for i in list_of_airports:
        name = i.name
        l.append(name)
    return l


def validate_data():
    source = source_combobox.get()
    destination = destination_combobox.get()

    if source and destination:
        if source == destination:
            tk.messagebox.showwarning(title="Error", message="Source and destination airports cannot be the same!")
        else:
            source_id = str(data.get_id_by_airport_name(list_of_airports, source))
            destination_id = str(data.get_id_by_airport_name(list_of_airports, destination))
            return source_id, destination_id
    else:
        tk.messagebox.showwarning(title="Error", message="Source and destination airports are required!")


result_value = "Albert-Bray Airport (Air France) -> Frankfurt am Main Airport (LOT) -> Warsaw Chopin Airport"

window = tk.Tk()
window.title("Flying App")

frame = tk.Frame(window)
frame.pack()

# Flight parameters frame
flight_params_frame = tk.LabelFrame(frame, text="Flight parameters")
flight_params_frame.grid(row=0, column=0, padx=20, pady=10)

source_airport_label = tk.Label(flight_params_frame, text="Source airport:")
source_combobox = ttk.Combobox(flight_params_frame, values=list_of_airports_names())
source_airport_label.grid(row=0, column=0)
source_combobox.grid(row=1, column=0)

destination_airport_label = tk.Label(flight_params_frame, text="Destination airport:")
destination_combobox = ttk.Combobox(flight_params_frame, values=list_of_airports_names())
destination_airport_label.grid(row=0, column=1)
destination_combobox.grid(row=1, column=1)

confirm_button = tk.Button(flight_params_frame, text="Find my flights", command=validate_data)
confirm_button.grid(row=1, column=2, sticky="news", padx=20, pady=10)

# Improve padding
for widget in flight_params_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Search results
results_frame = tk.LabelFrame(frame, text="Search results:")
results_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check = tk.Label(results_frame, text=result_value)
terms_check.grid(row=0, column=0, padx=10, pady=10)

window.mainloop()
