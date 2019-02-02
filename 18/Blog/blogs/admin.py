from django.contrib import admin

# Register your models here.
from blogs.models import Title,BlogPost
admin.site.register(Title)
admin.site.register(BlogPost)