from django.urls import path
from . import views
app_name = 'Auth'

urlpatterns=[
    path ('home', views.home, name = 'Home'),

]