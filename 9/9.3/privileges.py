class Privileges:
	def __int__(self,privileges):
		self.privileges = ['can add post','can delete post','can ban user','can grent owner']
	def show_privileges(self):
		for item in self.privileges:
			print("Admin grent is like"+item)
