from django.test import TestCase
from subscriptions.form import SubscriptionForm

class SubscribeFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()


    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))