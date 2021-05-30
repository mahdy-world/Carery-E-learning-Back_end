from os import name
from django.urls import path
from . import views
app_name = 'Book'

urlpatterns=[
    path ('all', views.book_list, name = 'BookList'),
    path ('books/<int:pk>/detail', views.book_details, name = 'bookdetails'),
    path('download/<int:id>', views.download2, name="downloadfun"),
    #  path('show/<int:id>', views.show_pdf, name="show"),
    
]