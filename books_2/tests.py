from django.test import TestCase
# from django.contrib.auth import get_user_model
from django.contrib.auth.model import User

from .models import Book


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # testcurator1 = get_user_model().objects.create_user(username='testcurator1', password='password')
        testcurator1 = User.objects.create_user(username='testcurator1', password='password')
        testcurator1.save()

        testbook = Book.objects.create(
            curator = testcurator1,
            author = 'Guy Kidding',
            title = 'Beau Jest',
            notes = 'Humor, Satire\nA man down on his yuk.',
        )
        testbook.save()

    def test_book_particulars(self):
        book = Book.objects.get(id=1)
        # expected_curator = f'{book.curator}
        # expected_author = f'{book.author}
        # expected_title = f'{book.title}
        # expected_notes = f'{book.notes}

        # self.assertEqual(expected_curator, 'testcurator1')
        # self.assertEqual(expected_author, 'Guy Kidding')
        # self.assertEqual(expected_title, 'Beau Jest')
        # self.assertEqual(expected_notes, 'Humor, Satire\nA man down on his yuk.')

    # Alternate implementation:
        actual_curator = str(book.curator)
        actual_author = str(book.author)
        actual_title = str(book.title)
        actual_notes = str(book.notes)

        self.assertEqual(actual_curator, 'testcurator1')
        self.assertEqual(actual_author, 'Guy Kidding')
        self.assertEqual(actual_title, 'Beau Jest')
        self.assertEqual(actual_notes, 'Humor, Satire\nA man down on his yuk.')
