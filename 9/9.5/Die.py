from random import randint
class  Die():
	"""docstring for  Die"""
	def __init__(self,sides = 6):
		self.sides = sides
	def roll_die(self):
		x = randint(1,self.sides)
		print('sides is '+str(self.sides)+' This is '+str(x))



ddie = Die()
for i in range(1,11):
	ddie.roll_die()

ddie_10 = Die(10)
for i in range(1,11):
	ddie_10.roll_die()
ddie_20 = Die(20)
for i in range(1,11):
	ddie_20.roll_die()
