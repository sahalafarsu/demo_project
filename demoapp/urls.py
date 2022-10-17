from .import views
from django.urls import path

urlpatterns = \
    [

    path('',views.demo1,name='demo1'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    path('thankspage/',views.thankspage,name='thankspage'),
    path('add/',views.addition,name='addition'),

    ]