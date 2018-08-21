class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	"""打印餐馆信息"""
	def describe_restaurant(self):
		print(self.restaurant_name+ " is "+self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is now opening!!Welcome ")
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors


my_restaurant = Restaurant('sijiacai','chuangyi')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

