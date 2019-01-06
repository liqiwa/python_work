from django.shortcuts import render

# Create your views here.
def index(request):
	"""披萨的店的主页"""
	return render(request,'pizzerias/index.html')