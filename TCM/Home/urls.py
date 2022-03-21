from django.urls import path
from . import views
urlpatterns = [
    path("home", views.index , name="index"),
    path('contact', views.contact , name='contact'),
    path('try',views.home , name='try')
    
]
