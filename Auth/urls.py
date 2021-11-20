from django.urls import path
from . import views
app_name = 'Auth'

urlpatterns=[
    path ('', views.home, name = 'Home'),
    path('student' , views.student , name = 'student'),
    path('student_edit/', views.edit_student , name = 'student_edit'),
    path('my_dashboard/', views.my_dashboard , name = 'my_dashboard'),
    path('notFound' , views.page404 , name='page404')
    
]