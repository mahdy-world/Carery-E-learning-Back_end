from django.urls import path
from . import views
app_name = 'Book'

urlpatterns=[
    path ('booklist/', views.book_list, name = 'booklist'),
    path ('^(?P<id>\d+)$', views.book_details, name = 'bookdetails'),
]