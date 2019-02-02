from django.shortcuts import render
from .models import Title
# Create your views here.
def index(request):
	"""博客的主页"""
	return render(request,'blogs/index.html')

def titles(request):
	"""显示所有标题"""
	titles = Title.objects.order_by('date_added')
	context = {'titles':titles}
	return render(request,'blogs/titles.html',context)

def title(request,title_id):
	"""显示单个主题及其所有的条目"""
	title = Title.objects.get(id=title_id)
	blogposts = title.blogpost_set.order_by('-date_added')
	context = {'title':title,'blogposts':blogposts}
	return render(request,'blogs/title.html',context)
