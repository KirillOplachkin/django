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
            comment = models.BookComment.objects.filter(book_id=id).order_by("created_date")
        except models.Books.DoesNotExist:
            print('No comments')
    except models.Books.DoesNotExist:
        raise Http404('Books does not exist, try another id')
    return render(request, "books_detail.html", dict(book=book, books_comment=comment))

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