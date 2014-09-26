class Car:
	'This class is simulating a car'
	def __init__(self, carId, name, direction, speed):
		self.carId = carId
		self.name = name
		self.direction = direction
		self.speed = speed

	def accelerate(self):
		if self.speed < 65:
			self.speed += 1
		else:
			print "Top speed reached"

	def brake(self):
		if self.speed > 0:
			self.speed -= 1
		else:
			print "You are already stopped"

	def turnLeft(self):
		if self.direction > 9:
			self.direction -= 10	
		else:
			self.direction = 360

	def turnRight(self):
		if self.direction < 360:
			self.direction += 10
		else:
			self.direction = 0

	def carStatus(self):
		print "Status of", self.carId
		print "Car name:", self.name
		print "Car direction:", self.direction
		print "Car speed:", self.speed

myCar = Car("001", "Mable", 0, 10)
myCar.carStatus()

action = ""

while action != "X":
	print "Drive your Car"
	print "+ to accelerate"
	print "- to brake"
	print "L to turn Left"
	print "R to turn Right"
	action = raw_input("What would you like to do (X to exit):")

	if action == "+":
		myCar.accelerate()

	elif action == "-":
		myCar.brake()

	elif action == "L":
		myCar.turnLeft()

	elif action == "R":
		myCar.turnRight()

	else:
		print "Action not recognized"
	myCar.carStatus()
