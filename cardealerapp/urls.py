
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
    path('nature/', views.nature, name='nature'),
    path('people/', views.people, name='people'),
    path('architecture/', views.architecture, name='architecture'),
    path('animals/', views.animals, name='animals'),
    path('sports/', views.sports, name='sports'),
    path('travel/', views.travel, name='travel'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('', views.register,name='register'),
    path('login/', views.login_view,name='login'),
    path('appointment/', views.appointment,name='appointment'),
    path('show/', views.show,name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete),

#Mpesa API

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),


]
