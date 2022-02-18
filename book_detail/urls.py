from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('book_d/', views.get_book_all, name='book_list'),
    path('book_d/<int:id>/', views.get_book_detail, name='book_detail'),
    path('book_d/<int:id>/update/', views.put_books_update, name='book_update'),
    path('add-books/', views.add_book, name='add_book'),
    path('book_d/<int:id>/delete/', views.books_delete, name='book_delete'),
]

