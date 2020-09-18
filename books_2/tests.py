from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Book


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testcurator = get_user_model().objects.creat_user(username='testcurator', password='password')
        testcurator.save()

        testbook = Book.objects.create(
            curator = testcurator,
            author = 'Guy Kidding'
            title = 'Beau Jest'
            notes = 'A guy walks into a bear...'
        )
        testbook.save()

    def test_book_particulars(self):
        book = Book.objects.get(id=1)
        actual_curator = str(book.curator)
        actual_author = str(book.author)
        actual_title = str(book.title)
        actual_notes = str(book.notes)

        self.assertEqual(actual_curator, 'testcurator')
        self.assertEqual(actual_author, 'Guy Kidding')
        self.assertEqual(actual_title, 'Beau Jest')
        self.assertEqual(actual_notes, 'A guy walks into a bear...')
