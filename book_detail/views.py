from django.shortcuts import render
from . import models

def get_book_all(request):
    books = models.Books.objects.all()
    return render(request, "books_list.html", {"books": books})
def comment_book(request):
    comment = models.BookComment.objects.all()
    return render(request, "books_list.html", {"comment": comment})