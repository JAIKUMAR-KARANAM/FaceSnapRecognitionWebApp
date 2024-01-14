from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path('shwdt',views.shwdt,name='result')
]