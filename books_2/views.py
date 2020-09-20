from django.shortcuts import render
from rest_framework import generics

from .models import Book
from .permissions import IsAuthorOrReadOnly
from .serializer import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

