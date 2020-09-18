from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    curator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
