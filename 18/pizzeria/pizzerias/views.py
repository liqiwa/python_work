from django.shortcuts import render
from .models import Pizza
# Create your views here.
def index(request):
	"""披萨的店的主页"""
	return render(request,'pizzerias/index.html')
def pizzas(request):
	"""显示披萨的配料"""
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas':pizzas}
	return render(request,'pizzerias/pizzas.html',context)
def pizza(request,pizza_id):
	"""显示单个主题及其所有的条目"""
	pizza = Pizza.objects.get(id=pizza_id)
	entries = pizza.topping_set.order_by('-date_added')##使用小写外键_set方法获取明细数据
	context = {'pizza':pizza,'entries':entries}
	return render(request,'pizzerias/pizza.html',context)