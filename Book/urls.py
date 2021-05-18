from django.urls import path
from . import views
app_name = 'Book'

urlpatterns=[
    path ('books/all', views.book_list, name = 'booklist'),
    path ('books/<int:pk>/detail', views.book_details, name = 'bookdetails'),
]