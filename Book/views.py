from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
# Create your views here.

# Book List & Paginator
def book_list(request):
    
    all_books= Book.objects.all()
    paginator = Paginator(all_books, 6)  # Show 4 contacts per page.
    page_number = request.GET.get('page')
    all_books = paginator.get_page(page_number)
    context ={
        'all' : all_books
    }
    return render(request , 'book.html',context)
# Book Details 
def book_details (request,pk):
    
    book = Book.objects.get(id=pk)
    context = {
        'details':book
    }
    return render(request , 'book_details.html',context)
