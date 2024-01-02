import math

DESTINATIONS = [
    "Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Amasya",
    "Ankara", "Antalya", "Artvin", "Aydin", "Balikesir",
    "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur",
    "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli",
    "Diyarbakir", "Edirne", "Elazig", "Erzincan", "Erzurum",
    "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari",
    "Hatay", "Isparta", "Mersin", "Istanbul", "Izmir",
    "Kars", "Kastamonu", "Kayseri", "Kirklareli", "Kirsehir",
    "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa",
    "Kahramanmaras", "Mardin", "Mugla", "Mus", "Nevsehir",
    "Nigde", "Ordu", "Rize", "Sakarya", "Samsun",
    "Siirt", "Sinop", "Sivas", "Tekirdag", "Tokat",
    "Trabzon", "Tunceli", "Sanliurfa", "Usak", "Van",
    "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman",
    "Kirikkale", "Batman", "Sirnak", "Bartin", "Ardahan",
    "Igdir", "Yalova", "Karabuk", "Kilis", "Osmaniye",
    "Duzce"
]
CITY_COORDINATES = {
    "Adana": (37.0000, 35.3213),
    "Adiyaman": (37.7648, 38.2786),
    "Afyonkarahisar": (38.7581, 30.5386),
    "Agri": (39.7191, 43.0503),
    "Amasya": (40.6534, 35.8330),
    "Ankara": (39.9334, 32.8597),
    "Antalya": (36.8969, 30.7133),
    "Artvin": (41.1828, 41.8183),
    "Aydin": (37.8450, 27.8458),
    "Balikesir": (39.6484, 27.8826),
    "Bilecik": (40.1501, 29.9830),
    "Bingol": (38.8853, 40.4983),
    "Bitlis": (38.3938, 42.1232),
    "Bolu": (40.7395, 31.6111),
    "Burdur": (37.7203, 30.2909),
    "Bursa": (40.1828, 29.0665),
    "Canakkale": (40.1553, 26.4142),
    "Cankiri": (40.6013, 33.6134),
    "Corum": (40.5489, 34.9535),
    "Denizli": (37.7765, 29.0864),
    "Diyarbakir": (37.9144, 40.2306),
    "Edirne": (41.6771, 26.5557),
    "Elazig": (38.6743, 39.2232),
    "Erzincan": (39.7505, 39.4914),
    "Erzurum": (39.9043, 41.2679),
    "Eskisehir": (39.7667, 30.5256),
    "Gaziantep": (37.0662, 37.3833),
    "Giresun": (40.9128, 38.3895),
    "Gumushane": (40.4603, 39.4816),
    "Hakkari": (37.5744, 43.7408),
    "Hatay": (36.4018, 36.3498),
    "Isparta": (37.7648, 30.5566),
    "Mersin": (36.8121, 34.6415),
    "Istanbul": (41.0082, 28.9784),
    "Izmir": (38.4192, 27.1287),
    "Kars": (40.6013, 43.0954),
    "Kastamonu": (41.3887, 33.7827),
    "Kayseri": (38.7205, 35.4826),
    "Kirklareli": (41.7333, 27.2167),
    "Kirsehir": (39.1450, 34.1608),
    "Kocaeli": (40.8533, 29.8815),
    "Konya": (37.8746, 32.4932),
    "Kutahya": (39.4167, 29.9833),
    "Malatya": (38.3552, 38.3095),
    "Manisa": (38.6191, 27.4289),
    "Kahramanmaras": (37.5736, 36.9371),
    "Mardin": (37.3122, 40.7339),
    "Mugla": (37.2153, 28.3636),
    "Mus": (38.7433, 41.5065),
    "Nevsehir": (38.6244, 34.7140),
    "Nigde": (37.9666, 34.6794),
    "Ordu": (40.9862, 37.8797),
    "Rize": (41.0201, 40.5234),
    "Sakarya": (40.7569, 30.3781),
    "Samsun": (41.2867, 36.33),
    "Siirt": (37.9443, 41.9329),
    "Sinop": (42.0264, 35.1551),
    "Sivas": (39.7477, 37.0179),
    "Tekirdag": (40.9781, 27.5117),
    "Tokat": (40.3167, 36.5500),
    "Trabzon": (41.0027, 39.7168),
    "Tunceli": (39.1071, 39.5400),
    "Sanliurfa": (37.1591, 38.7969),
    "Usak": (38.6823, 29.4082),
    "Van": (38.4942, 43.3800),
    "Yozgat": (39.8200, 34.8044),
    "Zonguldak": (41.4564, 31.7987),
    "Aksaray": (38.3687, 34.0363),
    "Bayburt": (40.2552, 40.2249),
    "Karaman": (37.1759, 33.2287),
    "Kirikkale": (39.8468, 33.5153),
    "Batman": (37.8812, 41.1351),
    "Sirnak": (37.4187, 42.4918),
    "Bartin": (41.6344, 32.3375),
    "Ardahan": (41.1105, 42.7022),
    "Igdir": (39.9167, 44.0333),
    "Yalova": (40.6550, 29.2769),
    "Karabuk": (41.2061, 32.6204),
    "Kilis": (36.7184, 37.1212),
    "Osmaniye": (37.0681, 36.2610),
    "Duzce": (40.8438, 31.1565)
}
PRICE_PER_KM = 1.5

class Trip:
    def __init__(self, driver_name, source, destination, date, max_passengers, price_per_passenger, conditions):
        self.driver_name = driver_name
        self.source = source
        self.destination = destination
        self.date = date
        self.max_passengers = max_passengers
        self.price_per_passenger = price_per_passenger
        self.conditions = conditions
        self.next = None

class TripNode:
    def __init__(self, trip):
        self.trip = trip
        self.next = None

class TripLinkedList:
    def __init__(self):
        self.head = None

    def add_trip(self, trip):
        new_trip_node = TripNode(trip)
        new_trip_node.next = self.head
        self.head = new_trip_node

def haversine(coord1, coord2):
    R = 6371  # Earth radius in kilometers
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

def calculate_price(from_city, to_city, number_of_passengers):
    from_coord = CITY_COORDINATES.get(from_city)
    to_coord = CITY_COORDINATES.get(to_city)
    if from_coord and to_coord:
        distance = haversine(from_coord, to_coord)
        total_price = distance * PRICE_PER_KM * number_of_passengers
        return total_price
    return None

def handle_customer():
    name = input("Please enter your name: ").capitalize()
    print("\nAs a customer, you can travel to all cities of Turkey \n")
    from_city = input("Please select the city you want to ride from: ").capitalize()
    to_city = input("Please select the city you want to go to: ").capitalize()
    date_of_travel = input("Enter the date of travel (dd/mm/yyyy): ")
    number_of_passengers = int(input("How many customers will travel? "))

    price = calculate_price(from_city, to_city, number_of_passengers)
    if price is not None:
        print(f"Trip Details:\nFrom: {from_city}\nTo: {to_city}\nDate: {date_of_travel}\n"
              f"Passengers: {number_of_passengers}\nPrice: {int(price)} liras.")
        print(f"Thank you, {name}! Your details have been recorded.")
    else:
        print("Invalid city names. Please choose from the available destinations.")

    another_action = input("Do you want to perform another action? (yes/no): ")
    if another_action.lower() == 'no':
        print("Thank you for using our app.")
    elif another_action.lower() == 'yes':
        print("Are you a customer or driver?")
    else:
        print("Invalid response. Exiting.")

def handle_driver(trips_linked_list):
    name = input("Please enter your name: ").capitalize()
    print("\nAs a driver, you can offer rides to all cities of Turkey \n")
    from_city = input("Please select the city you want to ride from: ").capitalize()
    to_city = input("Please select the city you want to go to: ").capitalize()
    date_of_travel = input("Enter the date of travel (dd/mm/yyyy): ")
    max_passengers = int(input("How many customers can you take with you? "))
    price_per_passenger = float(input("Enter the price per passenger: "))
    
    # Check for additional conditions
    conditions_response = input("If you have conditions like smoking or anything else, please specify (yes/no): ").lower()
    conditions = ""
    if conditions_response == 'yes':
        conditions = input("Please write your conditions: ")

    new_trip = Trip(name, from_city, to_city, date_of_travel, max_passengers, price_per_passenger, conditions)

    # Calculate and display price
    price = calculate_price(from_city, to_city, max_passengers)

    if price is not None:
        print("\nThank you! Your details have been recorded.")
        print(f"Trip Details:\nDriver: {name}\nFrom: {from_city}\nTo: {to_city}\nDate: {date_of_travel}\n"
              f"Max Passengers: {max_passengers}\nPrice per Passenger: {price_per_passenger} liras\n"
              f"Conditions: {conditions}\n")
    else:
        print("Invalid city names. Please choose from the available destinations.")

    # Add the trip to the linked list
    trips_linked_list.add_trip(new_trip)

    another_action = input("Do you want to perform another action? (yes/no): ")
    if another_action.lower() == 'no':
        print("Thank you for using our app, your details have been recorded.")
    elif another_action.lower() == 'yes':
        print("Are you a customer or driver?")
    else:
        print("Invalid response. Exiting.")

def main():
    print("Welcome to BlaBlaCar\nTravel between various Turkish cities")
    trips_linked_list = TripLinkedList()

    while True:
        role = input("Are you a customer or driver? ").capitalize()

        if role.lower() == "customer":
            handle_customer()
        elif role.lower() == "driver":
            handle_driver(trips_linked_list)
        else:
            print("Please enter a valid role (customer/driver).")
            continue

        another_action = input("Do you want to perform another action? (yes/no): ")

        if another_action.lower() == 'no':
            print("Thank you for using our app. Your details have been recorded.")
            break
        elif another_action.lower() != 'yes':
            print("Invalid response. Exiting.")
            break

if __name__ == "__main__":
    main()


