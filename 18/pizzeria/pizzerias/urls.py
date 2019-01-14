
"""定义pizzerias的url模式"""
from . import views
from django.conf.urls import url

urlpatterns = [
	#主页
	url(r'^$',views.index,name = 'index'),
	#显示所有主题
	url(r'^toppings/$',views.toppings,name = 'toppings'),
	url(r'^toppings/(?P<topping_id>\d+)/$',views.topping,name = 'topping'),
]