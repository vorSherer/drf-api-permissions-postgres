from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'curator', 'author', 'title', 'notes', 'created_at')
        model = Book

    