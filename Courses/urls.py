from django.urls import path
from . import views
app_name = 'Courses'

urlpatterns=[
  path('category_list/' , views.category_list , name = 'category_list'),
  path('programming_list/' , views.programming_list , name = 'programming_list'),
  path('design_list/' , views.design_list , name = 'design_list'),
  path('development_list/' , views.development_list , name = 'development_list'),
  path('lang_list/' , views.lang_list , name = 'lang_list'),
  path('network_list/' , views.network_list , name = 'network_list'),
  path('secuirty_list/' , views.secuirty_list , name = 'secuirty_list'),
  path('system_list/' , views.system_list , name = 'system_list'),
  path('database_list/' , views.database_list , name = 'database_list'),

  path('rate/<int:pk>/' , views.rate , name = 'rate'),  
  path ('course_details/<int:pk>/detail', views.course_detail, name = 'course_details'),
  path ('course_contante/<int:pk>/contante', views.course_contante, name = 'course_contante'),
  
  
]