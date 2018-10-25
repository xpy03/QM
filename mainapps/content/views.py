from django.shortcuts import render

from content.models import Book
from utils import rank


# Create your views here.
def show(request, book_id):

    rank.add_week_rank(book_id)

    book = Book.objects.get(pk=book_id)

    rank_books = rank.get_week_rank()  # 查询前5的阅读排行

    return render(request, 'book/show.html',locals())