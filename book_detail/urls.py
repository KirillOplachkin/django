from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('book_d/', views.get_book_all, name='book_list'),
    path('book_d/<int:id>/', views.get_book_detail, name='book_detail'),
    path('add-books/', views.add_book, name='add_book'),
]

