from Device import Device
import datetime
class DataOperations:
    def __init__(self):
        self.filename = "things.txt"
        self.deviceInventory = []
        self.loadDevices()

    def loadDevices(self):
        self.deviceInventory = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    id, name, model, serial_number, price, manufacture_str = line.strip().split("-")
                    year, month, day = map(int, manufacture_str.split(','))
                    manufacture_date = datetime.date(year, month, day)
                    device = Device(int(id), name, model, serial_number, float(price), manufacture_date)
                    self.deviceInventory.append(device)
        except FileNotFoundError:
            print(f"The file {self.filename} was not found. Creating a new one.")
            open(self.filename, 'w').close()
        except IOError as e:
            print(f"An error has occurred while accessing the file: {e}")

    def saveInventory(self):
        try:
            with open(self.filename, "w") as file:
                for device in self.deviceInventory:
                    manufacture_str = device.manufacture_date.strftime("%Y,%m,%d")
                    file.write(f"{device.id}-{device.name}-{device.model}-{device.serial_number}-{device.price}-{manufacture_str}\n")
        except IOError as e:
            print(f"An error occurred while saving to the file: {e}")

    def getAllThings(self):
        self.loadDevices()
        return self.deviceInventory

    def add_device(self, name, model, serial_number, price, manufacture_str):
        try:
            new_id = max(device.id for device in self.deviceInventory) + 1 if self.deviceInventory else 1
            year, month, day = map(int, manufacture_str.split(','))
            manufacture_date = datetime.date(year, month, day)
            newDevice = Device(new_id, name, model, serial_number, price, manufacture_date)
            self.deviceInventory.append(newDevice)
            self.saveInventory()
        except ValueError as e:
            print(f"Invalid date or other input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def remove_device(self, id):
        for device in self.deviceInventory:
            if device.id == id:
                self.deviceInventory.remove(device)
        self.saveInventory()

    def edit_device(self, id, name, model, serial_number, price, manufacture_str):
        try:
            for device in self.deviceInventory:
                if device.id == id:
                    device.name = name
                    device.model = model
                    device.serial_number = serial_number
                    device.price = price
                    year, month, day = map(int, manufacture_str.split(','))
                    device.manufacture_date = datetime.date(year, month, day)
            self.saveInventory()
        except ValueError as e:
            print(f"Invalid date or other input: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")



    def search_device(self, search):
        search_results = []  # Initialize an empty list to hold search results
        for device in self.deviceInventory:
            if search.lower() in device.name.lower():  # Case-insensitive search
                search_results.append(device)
        return search_results
    
    def find_device_id(self, id):
        # load all things first
        self.loadDevices()

        # find the matching thing using the id number by iterating through the list. when found, return it
        for device in self.deviceInventory:
            if device.id == id:
                return device
        return None
