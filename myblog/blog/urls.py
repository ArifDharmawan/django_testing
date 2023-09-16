# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home/about/', views.about, name='about'),
    path('home/blog/', views.blog, name='blog'),
    path('home/features/', views.features, name='features'),
    path('home/contact/', views.contact, name='contact'),
    path('home/post/', views.post_list, name='post_list'),
    path('home/post/post/<int:pk>/', views.post_detail, name='post_detail'),
]
