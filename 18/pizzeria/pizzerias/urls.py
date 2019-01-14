
"""定义pizzerias的url模式"""
from . import views
from django.conf.urls import url

urlpatterns = [
	#主页
	url(r'^$',views.index,name = 'index'),
	#显示所有主题
	url(r'^pizzas/$',views.pizzas,name = 'pizzas'),
	url(r'^pizzas/(?P<pizza_id>\d+)/$',views.pizza,name = 'pizza'),
]