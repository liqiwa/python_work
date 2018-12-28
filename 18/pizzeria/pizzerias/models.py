from django.db import models

# Create your models here.
"""披萨模型"""
class Pizza(models.Model):
	"""披萨名字"""

	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add =True)

	def __str__(self):
		"""返回模型的字符类型"""
		return self.name

class Topping(models.Model):
	"""添加披萨的配料信息"""
	pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
	name = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.name[:50]+"....."
		