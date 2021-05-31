from os import name
from django.urls import path
from . import views
app_name = 'Book'

urlpatterns=[
    path ('all', views.book_list, name = 'BookList'),
    path ('books/<int:pk>/detail', views.book_details, name = 'bookdetails'),
    path('download/<int:id>', views.download2, name="downloadfun"),
    #  path('show/<int:id>', views.show_pdf, name="show"),
    path('programming_list/' , views.programming_list , name = 'programming_list'),
    path('design_list/' , views.design_list , name = 'design_list'),
    path('development_list/' , views.development_list , name = 'development_list'),
    path('lang_list/' , views.lang_list , name = 'lang_list'),
    path('network_list/' , views.network_list , name = 'network_list'),
    path('secuirty_list/' , views.secuirty_list , name = 'secuirty_list'),
    path('system_list/' , views.system_list , name = 'system_list'),
    path('database_list/' , views.database_list , name = 'database_list'),
        
]