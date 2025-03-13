
from django.contrib import admin
from django.urls import path

from cardealerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('services/', views.services,name='services'),
    path('gallery/', views.gallery,name='gallery'),
    path('gallery-single/', views.gallery_single,name='index'),
    path('contact/', views.contact,name='contact'),
    path('starter/', views.starter,name='starter'),

]
