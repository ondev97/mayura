from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blogpost/<str:id>', views.blog_post, name='blog_post'),
    path('whoarewe', views.who_are_we, name='who_are_we'),
    path('contactus', views.contactus, name='contactus'),
    path('comment', views.comment, name='comment'),
]