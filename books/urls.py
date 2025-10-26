from django.urls import path
from .views import booksView

urlpatterns = [
    path('', booksView, name='books'),
]
