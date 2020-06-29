# OOP in Python, for idiots

# how to create a class:

class Cat:
	pass			# (class attributes, methods etc go here)
	
# how to create an instance of class Cat:

jasper = Cat()		

# and give it a name attribute of 'Jasper':
					
jasper.name = 'Jasper'	

# and a size attribute of 'small':
			
jasper.size = 'small'

print(f'{jasper.name} is {jasper.size}.')		# Jasper is small.

# alternatively:
	
class Dog:
	
	def __init__(self, name, size):		# this is called a class constructor. like a blueprint
		self.name = name								# assigns self.name (e.g. jasper.name) to whatever you supply as name
		self.size = size								# likewise self.size
		
hector = Dog('Hector', 'large')			# more efficient, ensures objects are initialised correctly

class Bird:		# to illustrate class attributes
	
	sound = 'cheep'			# a class attribute, shared by all Bird instances
	
feathers = Bird()

print(Bird.sound)				# cheep
print(feathers.sound)		# cheep

class Ferret:
	
	legs = 'short'
	mood = 'bitey'
	
	def __init__(self, name):
		self.name = name
		self._noise = 'honk honk'		# underscore means private i.e. LEAVE ALONE
		self.__mangled = 'mangled'	# __ means strongly private, cannot be accessed using self.mangled
		
	def poke(self):								# this is called an 'instance' or 'normal' method
		self.mood = 'very bitey'		# reassigns mood attribute
	
	@classmethod
	def mutate(cls):							# this is called a class method. note decorator
		cls.legs = 'spiderlike'			# called by the class, not an instance
		
	@property
	def noise(self):							# property decorator in effect makes function look like attribute
		return self._noise					# so cannot reassign with self.noise = 'new noise'
		
	@noise.setter
	def noise(self, value):				# but can reassign using setters 
		if value == 'bite yo azz':
			self._noise = value
	
gnasher = Ferret('Gnasher')
gnipper = Ferret('Gnipper')
print(gnasher.mood)							# bitey
Ferret.poke(gnasher)						# call method like this
gnipper.poke()									# or this ('syntactic sugar')
print(gnasher.mood)							# very bitey
print(gnipper.mood)							# very bitey
print(gnasher.legs)							# short
Ferret.mutate() 								# class method called. no instance required
print(Ferret.legs)							# 'spiderlike'
print(gnasher.legs)							# 'spiderlike'

gnasher.legs = 'short'					# can reassign instance attributes like this

print(gnasher.noise)						# but can only reassign properties by satisfying the logic of the setter
gnasher.noise = 'bite yo azz'		# ...like so
print(gnasher.noise)						# voila

# note setter must (??) be used in conjunction with _ or __, or else throws (max recursion depth) error

#print(gnasher.mangled)					# throws error
print(gnasher._Ferret__mangled)	# this works though ('mangling' basically involves prepending _Classname)
