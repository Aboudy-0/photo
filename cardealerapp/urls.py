
from django.contrib import admin
from django.urls import path

from cardealerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('services/', views.services,name='services'),
    path('gallery/', views.gallery,name='gallery'),
    path('gallery-single/', views.gallery_single,name='gallery_single'),
    path('contact/', views.contact, name='contact'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('', views.register,name='register'),
    path('login/', views.login_view,name='login'),
    path('appointment/', views.appointment,name='appointment'),

]
