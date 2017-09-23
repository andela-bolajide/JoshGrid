"""Write Test for JoshGrid Mail API."""

from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status

from .models import Mail


# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the Mail model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.sender_address = "bolaji@yahoo.com"
        self.sender = User.objects.create(username='Bolaji')
        self.receiver_name = "Seni"
        self.receiver_address = "seni@yahoo.com"
        self.mail_subject = "Test Mail"
        self.mail_body = "Hello, this is just a test. \
            Don't bother taking this serious."
        self.mail = Mail(
            sender_address=self.sender_address,
            sender=self.sender,
            receiver_name=self.receiver_name,
            receiver_address=self.receiver_address,
            mail_subject=self.mail_subject,
            mail_body=self.mail_body
        )

    def test_model_can_create_a_mail(self):
        """Test the Mail model can create a mail."""
        old_count = Mail.objects.count()
        self.mail.save()
        new_count = Mail.objects.count()
        self.assertNotEqual(old_count, new_count)


# class ViewTestCase(TestCase):
#     """This class defines the test suite for the Views."""
#
#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.sender_address = "bolaji@yahoo.com"
#         self.receiver_address = "seni@yahoo.com"
#         self.mail_subject = "Test Mail"
#         self.mail_body = "Hello, this is just a test. \
#             Don't bother taking this serious."
#         self.client = APIClient()
#         self.mail = {
#             "sender_address": self.sender_address,
#             "receiver_address": self.receiver_address,
#             "mail_subject": self.mail_subject,
#             "mail_body": self.mail_body
#         }
#         self.response = self.client.post(
#             reverse('create'),
#             self.mail,
#             format="json"
#         )
#
#     def test_api_can_create_a_mail(self):
#         """Test the api has mail creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
