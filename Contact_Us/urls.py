from django.urls import path
from . import views
app_name = 'Contact_Us'

urlpatterns=[
    path('home' , views.index , name='home')
]