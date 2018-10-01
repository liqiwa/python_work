from user import User
class Admin(User):
	"""添加属性"""
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()
		#self.privileges = ['can add post','can delete post','can ban user','can grent owner']
	#def show_privileges(self):
		#for item in self.privileges:
			#print("Admin grent is like"+self.privileges)
	def describe_user(self):
		print('This is your special_user admin!!!'+self.first_name+"    "+self.last_name)
class Privileges():
	def __init__(self):
		self.privileges = ['can add post','can delete post','can ban user','can grent owner']
	def show_privileges(self):
		for item in self.privileges:
			print("Admin grent is like"+item)

#special_user= Admin('he','mm')
#special_user.privileges.show_privileges()
#special_user.describe_user()
