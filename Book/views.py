from django.http.response import Http404
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import HttpResponse
from PyPDF2 import PdfFileReader


# Create your views here.

# Book List & Paginator
def book_list(request):
    
    all_books= Book.objects.all()
    paginator = Paginator(all_books, 6)  # Show 6 contacts per page.
    page_number = request.GET.get('page')
    all_books = paginator.get_page(page_number)
    return render(request , 'book.html',{'all' : all_books})
# Book Details 
def book_details (request,pk):
    book = Book.objects.get(id=pk)
    
    with open(book.file.path , "rb") as filehandle:  # Get Count Of Pages PDF
        pdf = PdfFileReader(filehandle)
        pages = pdf.getNumPages()
    return render(request , 'book_details.html',{'details':book, 'pages':pages})

# # Download Pdf
# def download (path):
#     file_path = os.path.join(settings.MEDIA_ROOT,path)
#     print(file_path)
#     if os.path.exists(file_path):
#         with open (file_path,'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/file")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response    
#     raise Http404

def download2(request, id):
    target_book = Book.objects.get(id=id)
    target_book.count_of_download += 1
    target_book.save()
    with open (target_book.file.path ,'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/force-download")
        response['Content-Disposition']= 'attachment;filename="filename.pdf"'
        response['X-Sendfile'] = "filename.pdf"
        # print(response['Content-Disposition'])
        return response    
   
def show_pdf(request,id):
    target_book = Book.objects.get(id=id)
    with open (target_book.file.path ,'rb') as fh:
        response = HttpResponse(fh.read(),  mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response

        
    # fsock = open(target_book.file.path, 'r')
    # response = HttpResponse(fsock, mimetype='application/pdf')
  
