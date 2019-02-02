"""定义blogs的URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
#主页
url(r'^$',views.index,name = 'index'),
#显示所有的主题
url(r'^titles/$',views.titles,name = 'titles'),
#显示特定主题的博客
url(r'^titles/(?P<title_id>\d+)/$',views.title,name = 'title'),
]