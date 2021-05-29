from django.urls import path
from . import views
app_name = 'Courses'

urlpatterns=[
  path('category_list/' , views.category_list , name = 'category_list'),
  path('programming_list/' , views.programming_list , name = 'programming_list'),
  path ('course_details/<int:pk>/detail', views.course_detail, name = 'course_details'),
  
]