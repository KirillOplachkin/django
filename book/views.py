from django.shortcuts import render
from . import models


def book_all(request):
    post = models.Book.objects.all()
    return render(request, "post_list.html", {"post": post})