from django.urls import path
from . import views
urlpatterns = [
    path('serial/', views.show_all, name= 'serial_list')
]
