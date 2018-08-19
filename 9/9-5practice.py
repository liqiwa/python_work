class User():
	"""存储用户信息"""
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
	def describe_user(self):
		print("Hi Welcome "+self.first_name+self.last_name + " is login "+str(self.login_attempts))
	def greet_user(self):
		print('Welcome ')
	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts +1
	def reset_login_attempts(self):
		self.login_attempts = 0

my_user = User('he','mm')
my_user.describe_user()
my_user.greet_user()
my_seconduser = User('wang','fei')
my_seconduser.describe_user()
my_seconduser.greet_user()
my_thirduser = User('qin','shihuang')
my_thirduser.describe_user()
my_thirduser.greet_user()

my_user.increment_login_attempts()
my_user.increment_login_attempts()

my_user.describe_user()
my_user.reset_login_attempts()
my_user.describe_user()
