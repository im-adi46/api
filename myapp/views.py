from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import Bookserializer
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer