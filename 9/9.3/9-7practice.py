class User():
	"""存储用户信息"""
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print("Hi Welcome "+self.first_name+self.last_name)
	def greet_user(self):
		print('Welcome ')


my_user = User('he','mm')
my_user.describe_user()
my_user.greet_user()
my_seconduser = User('wang','fei')
my_seconduser.describe_user()
my_seconduser.greet_user()
my_thirduser = User('qin','shihuang')
my_thirduser.describe_user()
my_thirduser.greet_user()

class Admin(User):
	"""添加属性"""
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = ['can add post','can delete post','can ban user','can grent owner']
	def show_privileges(self):
		for item in self.privileges:
			print("Admin grent is like"+item)

special_user= Admin('he','mm')
special_user.show_privileges()



