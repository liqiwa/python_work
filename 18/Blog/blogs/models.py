from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Title(models.Model):
	"""bolog信息"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text
class BlogPost(models.Model):
	"""每个主题下的帖子"""
	title = models.ForeignKey(Title,on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'blogposts'

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50]+"......"