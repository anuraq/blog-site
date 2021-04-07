from django.shortcuts import render
from .models import Blog
#from django.http import HttpResponse

def index(request):
    queryset = Blog.objects.filter()
    context = {
        'object_list': queryset
    }
    return render(request, 'blogs/index.html', context)

def blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)[0]
    context = {
        'blog_id': blog_id,
        'blog': blog
    }
    return render(request, 'blogs/blog.html', context)
