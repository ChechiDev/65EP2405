from django.shortcuts import render
from django.http import HttpResponse

def booksView(request):
    return HttpResponse("Hola, soy un libro!")

