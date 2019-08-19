from django.test import TestCase
from .models import Subscriber
from django.db.utils import IntegrityError


class SubscriberTestCases(TestCase):

    def test_cannot_have_duplicate_emails(self):
        test_email = "user123@test.com"
        _first_sub = Subscriber.objects.create(email=test_email)
        with self.assertRaises(IntegrityError):
            _second_sub = Subscriber.objects.create(email=test_email)
