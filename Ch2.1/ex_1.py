class Vehicle: # Define a class called Vehicle
    def __init__(self, weight, passengers, vehicle_economy):
        self.weight = weight
        self.passengers = passengers
        self.vehicle_economy = vehicle_economy

    def weight_per_passenger(self): # Define a function in the class
        return self.weight / self.passengers
    def passenger_economy(self): # Define another class function
        return self.vehicle_economy * self.passengers

    def passenger_distance_cost(self, fuel_price):
        return fuel_price / self.passenger_economy()

    def __repr__(self):
        return ('<' + self.__class__.__name__ +
        ' weight='+ str(self.weight)+
        ' passengers=' + str(self.passengers)+
        ' vehicle economy=' + str(self.vehicle_economy)+
        '>')

'''
titanic = Vehicle()
titanic.weight = 54000
titanic.passengers = 2400
titanic.vehicle_economy = 0.75

print (titanic.weight_per_passenger())
print (titanic.passenger_economy())
print (titanic.passenger_distance_cost(72))
print (Vehicle)
'''
UFO = Vehicle(213, 71, 4)
print (UFO.weight_per_passenger())
print (UFO.passenger_economy())
print (UFO.passenger_distance_cost(1420))
print (UFO)
