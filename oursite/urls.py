# Use include() to add paths from the catalog application 
from django.urls import path
from django.conf.urls import include, url
from .import views
urlpatterns = [    
    path('index/',views.index,name='index'),
]