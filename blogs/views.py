from django.shortcuts import render
from .models import Blog
#from django.http import HttpResponse

def index(request):
    queryset = Blog.objects.filter()
    context = {
        'object_list': queryset
    }
    return render(request, 'blogs/index.html', context)
