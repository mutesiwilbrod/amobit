# Use include() to add paths from the catalog application 
from django.urls import path
from django.conf.urls import include, url
from .import views


app_name='oursite'
urlpatterns = [    
    path('index/',views.index,name='index'),
    path('index/contact', views.contact ,name='contact'),
    path('index/register',views.register, name='register'),
]