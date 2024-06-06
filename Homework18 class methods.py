class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self):
        self.numberOfFloors += 1
        print(self.numberOfFloors)

house1 = House()
house1.setNewNumberOfFloors()
