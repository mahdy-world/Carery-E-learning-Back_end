from django.urls import path
from . import views
app_name = 'Auth'

urlpatterns=[
    path ('home', views.home, name = 'Home'),
    path('student' , views.student , name = 'student'),
    path('student_edit/', views.edit_student , name = 'student_edit')
    
]