'''
1) define decorator function e.g. eggs()
2) define function to be decorated and prepend with @eggs
'''

def spam():
	return 'spam'

print(spam()) # spam, obviously

def eggs(spam):
	return spam() * 3 # eggs takes an argument, calls it, then returns its return multiplied by 3
	
print(eggs(spam)) # spamspamspam

spam = eggs(spam)

spam # does bugger all (might as well type x = 3; x)

# spam() # throws error (might as well type 'spamspamspam'())

@eggs
def smee():
	return 'heee'

print(smee) 

'''
so instead of writing...

def spam():
	etc
	
def eggs(spam):
	etc
	
spam = eggs(spam)

...you can write...

def eggs(spam):
	etc
	
@eggs
def spam():
	etc

if your decorator function (eggs() above) returns a function (rather than e.g. a string as above), you need to call it to return its output (e.g. smee() rather than just smee))
'''
