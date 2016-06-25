print 'Sat car_app.py gamma'

from car import Car

red_car = Car()
print 'Colour ' + red_car.getColour()
print 'Mileage ' + str(red_car.getMileage())
print 'Make ' + red_car.getMake()

red_car.setMake('Ferrari')

print 'Make ' + red_car.getMake()

print('Getting a paint job - the new colour is ' + red_car.paint('red'))

print 'Colour ' + red_car.getColour()

print ('Car moved ' + str(red_car.move(15)) + 'kms')
print 'Mileage ' + str(red_car.getMileage())

print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize
