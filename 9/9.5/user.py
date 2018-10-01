class User():
	"""存储用户信息"""
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print("Hi Welcome "+self.first_name+self.last_name)
	def greet_user(self):
		print('Welcome ')


#my_user = User('he','mm')
#my_user.describe_user()
#my_user.greet_user()
#my_seconduser = User('wang','fei')
#my_seconduser.describe_user()
#my_seconduser.greet_user()
#my_thirduser = User('qin','shihuang')
#my_thirduser.describe_user()
#my_thirduser.greet_user()
