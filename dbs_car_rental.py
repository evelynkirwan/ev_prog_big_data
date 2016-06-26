print ('Welcome to the Car Rental Program')

#Handle user input

from dbs_car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []    

    def create_current_stock(self):
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range(8):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.electric_cars.append(ElectricCar())         
        for i in range(4):
           self.hybrid_cars.append(HybridCar())               
           
    def stock_count(self):
        print 'Petrol cars remaining in stock ' + str(len(self.petrol_cars))
        print 'Diesel cars remaining in stock ' + str(len(self.diesel_cars))
        print 'Electric cars remaining in stock ' + str(len(self.electric_cars))
        print 'Hybrid cars remaining in stock ' + str(len(self.hybrid_cars))

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Sorry, there are not enough cars in stock, please try again later.'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
          
    def process_rental(self):
        selection = raw_input ('Would you like to rent a car? Y/N:\n')
        selection = selection.lower()
        if selection == 'y':
            selection = raw_input('Which type of car would you like to process?\nPlease type P for Petrol, D for Diesel, E for Electric, H for Hybrid. \n')
            selection = selection.lower()
            amount = int(raw_input('How many cars would you like to process?'))         
            if selection == 'p':
                print ('Thank you for selecting from the petrol range.\n')
                self.rent(self.petrol_cars, amount)
            elif selection == 'd':
                print ('Thank you for selecting from the diesel range.\n')
                self.rent(self.diesel_cars, amount)              
            elif selection == 'e':
                print ('Thank you for selecting from the electric range.\n')
                self.rent(self.electric_cars, amount)
            elif selection == 'h':
                print ('Thank you for selecting from the hybrid range.\n')
                self.rent(self.hybrid_cars, amount)
            self.stock_count() 
    
dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('Would you like to process another car? Y/N:\n')
    proceed = proceed.lower()