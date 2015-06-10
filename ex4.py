cars = 100
space=4.0
drivers=30
passengers=90
cars_not_driven= cars - drivers
carsdriven= drivers
carpool = carsdriven * space
average = passengers /carsdriven

print "there are", cars, "cars available"
print "there are only",drivers, "drivers"
print "there will be ",cars_not_driven," empty cars"
print "we can transport", carpool, "people"
print "we have", passengers, "to carpool"
print "we need ",average, "in each car"


print "hey %s there." % "you"
