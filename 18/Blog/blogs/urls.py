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
#用于添加新主题的网页
url(r'^new_title/$',views.new_title,name = 'new_title'),
#用于添加新回复的页面
url(r'^new_blogpost/(?P<title_id>\d+)/$',views.new_blogpost,name = 'new_blogpost'),
#用于编辑现有的主题页面
url(r'^edit_blogpost/(?P<blogpost_id>\d+)/$',views.edit_blogpost,name = 'edit_blogpost'),
]