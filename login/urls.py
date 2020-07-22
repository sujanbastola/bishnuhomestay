from django.urls import path
from . import views





urlpatterns = [

    path('', views.login, name='login'),
    path('contact', views.Contact, name='contact'),
    path('about', views.about, name='about'),
    path('book', views.book, name='book'),

    #path('gallery', views.gallery, name='gallery'),
    path('search', views.search, name='search'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handle_Login, name='handle_Login'),
    path('logout', views.handle_Logout, name='handle_Logout'),
    path('<str:slug>', views.blogpost, name='blogpost'),




]