from django.urls import path
from . import views, models


app_name = "books"
urlpatterns = [
    path('book_d/', views.BookListView.as_view(),
         name='book_list'),
    path('book_d/action/', views.BookListView.as_view(queryset=models.Books.objects.filter(genre="Action")),
         name='book_list'),
    path('book_d/drama/', views.BookListView.as_view(queryset=models.Books.objects.filter(genre="Drama").order_by("-id")),
         name='book_list'),
    path('book_d/romantic/', views.BookListView.as_view(queryset=models.Books.objects.filter(genre="Romantic")),
         name='book_list'),
    path('book_d/fantastic/', views.BookListView.as_view(queryset=models.Books.objects.filter(genre="Fantastic")),
         name='book_list'),
    path('book_d/<int:id>/', views.BookDetailView.as_view(),
         name='book_detail'),
    path('book_d/<int:id>/update/', views.BookUpdateView.as_view(),
         name='book_update'),
    path('add-books/', views.BookCreateView.as_view(),
         name='add_book'),
    path('book_d/<int:id>/delete/', views.BookDeleteView.as_view(),
         name='book_delete'),

]

