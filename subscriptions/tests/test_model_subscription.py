from datetime import datetime

from django.test import TestCase
from subscriptions.models import Subscription


class SubscribeModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Marcio Ramos",
            cpf="36911563213",
            email="contato.marcio@mail.com",
            phone="15-996042331"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)