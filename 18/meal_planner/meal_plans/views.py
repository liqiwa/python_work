from django.shortcuts import render

# Create your views here.

def index(request):
	"""膳食管理的主页"""
	return render(request,'meal_plans/index.html')