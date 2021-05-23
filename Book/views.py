from django.http.response import Http404
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import HttpResponse
from pikepdf import Pdf

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
        'details':book,
    }
    return render(request , 'book_details.html',context)


def download (path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open (file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
             
    raise Http404

def home(path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    image_data = open(file_path, 'rd').read()
    return HttpResponse(image_data, mimetype='application/pdf')



def get_pdf_page_count(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    pdf_doc = Pdf.open(file_path)
    pdf_page_count = len(pdf_doc)
    context={
        'count_pdf' : pdf_page_count
    }
    return render (request ,'book_details.html',context)