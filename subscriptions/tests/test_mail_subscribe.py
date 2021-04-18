from django.core import mail
from django.test import TestCase
from subscriptions.form import SubscriptionForm


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Marcio Ramos", cpf="12345678901",
                    email="marcioalvesramos90@hotmail.com", phone="15-996042331")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'marcioalvesramos90@hotmail.com'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['marcioalvesramos90@hotmail.com', 'marcioalvesramos90@hotmail.com']
        self.assertEqual(expected, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ('Marcio Ramos', '12345678901', 'marcioalvesramos90@hotmail.com', '15-996042331')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
