class City():
	"""docstring for City"""
	def __init__(self,City_name,City_adress):
	 	self.City_name = City_name
	 	self.City_adress = City_adress
	def print(self):
		print(self.City_name+'  '+self.City_adress)
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	"""打印餐馆信息"""
	def describe_restaurant(self):
		print(self.restaurant_name+ " is "+self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is now opening!!Welcome ")



#my_restaurant = Restaurant('sijiacai','chuangyi')
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

