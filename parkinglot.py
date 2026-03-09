class Vehicle:
    def __init__(self, number):
        self.number = number


class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.parked_vehicles = {}
        self.available_spots = total_spots

    def vehicle_entry(self, vehicle_number, entry_time):
        if self.available_spots > 0:
            vehicle = Vehicle(vehicle_number)
            self.parked_vehicles[vehicle_number] = entry_time
            self.available_spots -= 1
            print("Vehicle parked successfully.")
        else:
            print("Parking Full!")

    def vehicle_exit(self, vehicle_number, exit_time):
        if vehicle_number in self.parked_vehicles:
            entry_time = self.parked_vehicles[vehicle_number]
            hours = exit_time - entry_time
            fee = hours * 10   # ₹10 per hour

            print("Vehicle Number:", vehicle_number)
            print("Parking Hours:", hours)
            print("Parking Fee: ₹", fee)

            del self.parked_vehicles[vehicle_number]
            self.available_spots += 1
        else:
            print("Vehicle not found!")

    def show_available_spots(self):
        print("Available Spots:", self.available_spots)


parking = ParkingLot(5)

parking.vehicle_entry("OD02AB1234", 1)
parking.vehicle_entry("OD05CD5678", 2)

parking.show_available_spots()

parking.vehicle_exit("OD02AB1234", 5)

parking.show_available_spots()