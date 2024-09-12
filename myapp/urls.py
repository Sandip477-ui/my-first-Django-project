from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('index', views.index,name='index'),
]