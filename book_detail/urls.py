from django.urls import path
from . import views


urlpatterns = [
    path('book_d/', views.get_book_all, name= 'book_list'),
    path('book_d_com/', views.comment_book, name= 'book_comment'),

]

