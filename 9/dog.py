class Dog():
	"""一次模拟小狗的简单测速"""
	def __init__(self,name,age):	
	 	"""初始化属性name和age"""
	 	self.name = name
	 	self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title()+" is now sitting.")

	def roll_over(self):
		"""模拟小狗打滚"""
		print(self.name.title()+" rolled over! ")


my_dog = Dog('qiqi',1)
print("My dog is name is "+my_dog.name.title())
print("My dog is "+str(my_dog.age)+" years old")
my_dog.sit()
my_dog.roll_over()