from django.shortcuts import render

from content.models import Book

# Create your views here.
def show(request, book_id):

    book = Book.objects.get(pk=book_id)

    return render(request, 'book/show.html',locals())