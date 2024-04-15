import datetime

class Device:

    def __init__(self, id, name, model, serial_number, price, manufacture_date):
        self.id = id
        self.name = name
        self.model = model
        self.serial_number = serial_number
        self.price = price
        self.manufacture_date = manufacture_date

    def __str__(self):
        return f"Device id: {self.id}, Name: {self.name}, Model: {self.model}, Serial Number: {self.serial_number}, Price: {self.price}, Manufacture Date: {self.manufacture_date}"
    
