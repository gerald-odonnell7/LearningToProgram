class Animal:
	'This class is designed to represent real world animal'
	numAnimals = 0
	def __init__(self, name, length, weight, color, sound):
		self.name = name
		self.length = length
		self.weight = weight
		self.color = color
		self.sound = sound
		Animal.numAnimals += 1


	def eat(self):
		print self.name, "is eating"

	def sleep(self):
		print self.name, "is sleeping"

	def run(self):
		print self.name, "is running"

	def displayAnimalCount(self):
		print Animal.numAnimals


kitty = Animal("Fluffy", 18, 5, "Gray", "Meow")
kitty.eat()
kitty.sleep()
kitty.run()
kitty.displayAnimalCount()

puppy = Animal("Rover", 36, 48, "Brown", "Bark")
puppy.eat()
puppy.sleep()
puppy.run()
puppy.displayAnimalCount()

