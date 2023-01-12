import openpyxl


class Airport:
    def __init__(self, airport_id: str, rating: float, name: str):
        self.airport_id = airport_id
        self.rating = rating
        self.name = name


class Airline:
    def __init__(self, airline_id: int, name: str, rating: int):
        self.airline_id = airline_id
        self.name = name
        self.rating = rating


class Route:
    def __init__(self, airline_id: int, destination_id: str, source_id: str):
        self.airline_id = airline_id
        self.destination_id = destination_id
        self.source_id = source_id


def create_list_of_airlines() -> list:
    wb = openpyxl.load_workbook(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\airlines_ratings.xlsx')
    sheet = wb.active
    l = []
    sheet_length = len(sheet['A'])
    for i in range(2, sheet_length + 1):
        name = sheet["B" + str(i)]
        rating = sheet["G" + str(i)]
        airline_id = sheet["A" + str(i)]
        airline = Airline(airline_id=airline_id.value, name=name.value, rating=rating.value)
        l.append(airline)
    return l


def get_airline_rating_by_id(airlines: list, airline_id: str) -> float:
    for airline in airlines:
        if str(airline.airport_id) == airline_id:
            return airline.rating
    return -1.0


def create_list_of_airports() -> list:
    wb = openpyxl.load_workbook(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\airports_ratings.xlsx')
    sheet = wb.active
    l = []
    sheet_length = len(sheet['A'])
    for i in range(2, sheet_length + 1):
        name = sheet["B" + str(i)]
        rating = sheet["J" + str(i)]
        airport_id = sheet["A" + str(i)]
        airport = Airport(airport_id=airport_id.value, name=name.value, rating=rating.value)
        l.append(airport)
    return l


def get_airport_rating_by_id(airports: list, airport_id: str) -> float:
    for airport in airports:
        if str(airport.airport_id) == airport_id:
            return airport.rating
    return -1.0


def create_list_of_routes() -> list:
    wb = openpyxl.load_workbook(r'C:\Users\jasie\STUDIA\TASS\projekt2\TASS\routes1.xlsx')
    sheet = wb.active
    l = []
    sheet_length = len(sheet['A'])
    for i in range(2, sheet_length + 1):
        airline_id = sheet["B" + str(i)]
        destination = sheet["F" + str(i)]
        source = sheet["D" + str(i)]
        route = Route(airline_id=airline_id.value, destination_id=destination.value, source_id=source.value)
        l.append(route)
    return l


def get_airline_by_destination_and_source(routes: list, destination: str, source: str) -> list:
    l = []
    for route in routes:
        if (route.source_id == source) and (route.destination_id == destination):
            l.append(route.airline_id)
    return l