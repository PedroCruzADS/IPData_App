from django.urls import path

from .views import index, log

urlpatterns = [
    path('', index, name='index'),
    path('log', log, name='log')
 
]
