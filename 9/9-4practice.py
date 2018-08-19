##
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	"""打印餐馆信息"""
	def describe_restaurant(self):
		print(self.restaurant_name+ " is "+self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is now opening!!Welcome ")
	def sum_number(self):
		print("Total is "+str(self.number_served))
	def set_number_served(self,number_served):
		self.number_served = number_served
		print("This is "+str(self.number_served)+" eat food")
	def increment_number_served(self,max_served):
		print('This restaurant is '+ str(max_served)+' is eat')

my_restaurant = Restaurant('yijiaguan','beifangcai')
my_restaurant.describe_restaurant()
my_restaurant.sum_number()
my_restaurant.set_number_served('100') 
my_restaurant.increment_number_served('300')