from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('b/<int:blog_id>/', views.blog, name='blog')
]
