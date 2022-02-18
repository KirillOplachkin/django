from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import reverse, redirect
from django.http import Http404, HttpResponse
from . import models, forms


def get_book_all(request):
    books = models.Books.objects.all().order_by("id")
    return render(request, "books_list.html", {"books": books})


def get_book_detail(request, id):
    global comment
    try:
        book = get_object_or_404(models.Books, id=id)
        try:
            comment = models.BookComment.objects.filter(books_id=book).order_by("created_date")
        except models.Books.DoesNotExist:
            print('No comments')
    except models.Books.DoesNotExist:
        raise Http404('Books does not exist, try another id')
    return render(request, "book_detail.html", {"book": book,
                                                "books_comment": comment})


def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book_list"))
            # return HttpResponse("Book created Successfully")
    else:
        form = forms.BookForm()
    return render(request, "add_books.html", {"form": form})


def put_books_update(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_id,
                              data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book_list"))
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, "books_update.html", {"form": form,
                                                 "book": book_id})

def books_delete(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    book_id.delete()
    # return HttpResponse("Book deleted")
    return redirect(reverse("book:book_list"))





