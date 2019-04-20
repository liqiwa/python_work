from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Title,BlogPost
from .forms import TitleForm,BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
# Create your views here.


def index(request):
	"""博客的主页"""
	return render(request,'blogs/index.html')
@login_required
def titles(request):
	"""显示所有标题"""
	titles = Title.objects.order_by('date_added')
	context = {'titles':titles}
	return render(request,'blogs/titles.html',context)

def title(request,title_id):
	"""显示单个主题及其所有的条目"""
	title = Title.objects.get(id=title_id)
	#确认请求的主题属于当前登陆的用户,使用函数check_blog_owner
	#check_blog_owner(request,title)
	blogposts = title.blogpost_set.order_by('-date_added')
	context = {'title':title,'blogposts':blogposts}
	return render(request,'blogs/title.html',context)
def new_title(request):
	"""添加新主题"""

	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = TitleForm()
	else:
		#POST提交的数据，对数据进行处理
		form = TitleForm(request.POST)
		if form.is_valid():
			new_title = form.save(commit = False)
			new_title.owner = request.user
			new_title.save()
			return HttpResponseRedirect(reverse('blogs:titles'))
	context = {'form':form}
	return render(request,'blogs/new_title.html',context)
def new_blogpost(request,title_id):
	"""在特定博客中添加新回复"""
	title = Title.objects.get(id = title_id)
#确认请求的主题属于当前登陆的用户,使用函数check_blog_owner
	check_blog_owner(request,title)
	if request.method != 'POST':
		#未提交数据，创建一个空表单
		form = BlogPostForm()
	else:
		#POST提交的数据，对数据进行处理
		form = BlogPostForm(data =request.POST)
		if form.is_valid():
			new_blogpost = form.save(commit = False)
			new_blogpost.title = title
			new_blogpost.save()
			return HttpResponseRedirect(reverse('blogs:title',args = [title_id]))
	context = {'title':title,'form':form}
	return render(request,'blogs/new_blogpost.html',context)
def edit_blogpost(request,blogpost_id):
	"""编辑已有条目"""
	blogpost = BlogPost.objects.get(id = blogpost_id)
	title = blogpost.title
#确认请求的主题属于当前登陆的用户,使用函数check_blog_owner
	check_blog_owner(request,title)
	if request.method !='POST':
		#初次请求，使用当前条目填充表单
		form = BlogPostForm(instance = blogpost)
	else:
		#POST提交的数据，对数据进行处理
		form = BlogPostForm(instance = blogpost,data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:title',args=[title.id]))
	context = {'blogpost':blogpost,'title':title,'form':form}
	return render(request,'blogs/edit_blogpost.html',context)
	#检查当前blog创建人与当前登陆用户是否一致
def check_blog_owner(request,title):
	if title.owner != request.user:
		raise Http404

