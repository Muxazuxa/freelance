from django.test import TestCase
from django.shortcuts import reverse
from django.test import Client


class UserProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post(reverse('users:list'), {'username': 'test', 'email': 'test@mail.ru', 'password': '12345'})
        self.client.login(username='test', password='12345')

    def test_user_login(self):
        response = self.client.post('/api-auth/login/?next=/tasks/', {'username': 'test', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

    def test_user_list(self):
        response = self.client.get(reverse('users:list'))
        self.assertEqual(response.status_code, 200)

    def test_user_not_exist(self):
        response = self.client.get('/users/10000')
        self.assertEqual(response.status_code, 404)

    def test_user_username_unique(self):
        response = self.client.post(reverse('users:list'), {'username': 'test', 'email': 'test@mail.ru', 'password': '12345'})
        self.assertEqual(response.status_code, 400)
