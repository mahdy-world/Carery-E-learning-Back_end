from django.urls import path
from . import views
app_name = 'Book'

urlpatterns=[
    path ('all', views.book_list, name = 'BookList'),
    path ('books/<int:pk>/detail', views.book_details, name = 'bookdetails'),
]