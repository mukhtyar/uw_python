# Create your views here.
from books.models import Book
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q

def index(request):
    book_list = Book.objects.all
    return render_to_response('books/index.html', {'book_list': book_list})
    
def detail(request, book_id):
    b = get_object_or_404(Book, pk=book_id)
    return render_to_response('books/detail.html', {'book': b})
