
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', views.book_all, name= 'Book Kirill'),
]