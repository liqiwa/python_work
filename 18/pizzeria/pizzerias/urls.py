
"""定义pizzerias的url模式"""
from . import views
from django.conf.urls import url

urlpatterns = [
	#主页
	url(r'^$',views.index,name = 'index')
]