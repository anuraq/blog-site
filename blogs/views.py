from django.shortcuts import render
from .models import Blog
import random
#from django.http import HttpResponse

def index(request):
    queryset = Blog.objects.filter()
    seed = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    bg_color = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
    avatar_list = ['male', 'female', 'human', 'bottts', 'avataaars', 'jdenticon', 'gridy', 'micah', 'open-peeps', 'adventurer', 'big-smile']
    context = {
        'object_list': queryset[::-1],
        'avatar_sprites': avatar_list[random.randint(0, len(avatar_list)-1)],
        'avatar_seed': seed,
        'bg_color': bg_color
    }
    return render(request, 'blogs/index.html', context)

def blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)[0]
    context = {
        'blog_id': blog_id,
        'blog': blog
    }
    return render(request, 'blogs/blog.html', context)
