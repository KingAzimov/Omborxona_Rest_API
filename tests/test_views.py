from unittest import TestCase

from asosiyapp.views import *
from asosiyapp.serializers import *
from userapp.views import *
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class TestUsersView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        token = Token.objects.get(user__username='OmborxonaAPI')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_hamma_userlar(self):
        natija = self.client.get('/asosiy/users/')
        assert natija.status_code == 200
        assert len(natija.data) == 2
        assert dict(natija.data[0])['username'] == 'OmborxonaAPI'

class TestMahsulotlarView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        token = Token.objects.get(user__username='OmborxonaAPI')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_hamma_mahsulotlar(self):
        natija = self.client.get('/asosiy/mahsulotlar/')
        assert natija.status_code == 200
        self.assertEqual(len(natija.data), 3)
        self.assertEqual(dict(natija.data[0])['nom'], 'Samsung a21')

