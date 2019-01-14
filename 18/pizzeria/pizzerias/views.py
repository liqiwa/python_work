from django.shortcuts import render
from .models import Topping
# Create your views here.
def index(request):
	"""披萨的店的主页"""
	return render(request,'pizzerias/index.html')
def toppings(request):
	"""显示披萨的配料"""
	topping = Topping.objects.order_by('date_added')
	context = {'toppings':topping}
	return render(request,'pizzerias/toppings.html',context)
def topping(request,topping_id):
	"""显示单个主题及其所有的条目"""
	topping = Topping.objects.get(id=topping_id)
	entries = topping.entry_set.order_by('-date_added')
	context = {'topping':topping,'entries':entries}
	return render(request,'pizzerias/topping.html',context)