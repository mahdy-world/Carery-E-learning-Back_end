from django.urls import path
from . import views
app_name = 'Trainer'

urlpatterns=[
    path ('all', views.all_tranier, name = 'AllTrainer'),
]