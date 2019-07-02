import unittest
from django.shortcuts import reverse
from django.test import Client


class TaskTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.client.post(reverse('users:list'), {'username': 'test', 'email': 'test@mail.ru', 'password': '12345'})
        self.client.login(username='test', password='12345')

    def test_task_create(self):
        response = self.client.post(reverse('tasks:list'), {'title': 'Python', 'description': 'Blog Api', 'price': 50})
        self.assertEqual(response.status_code, 201)

    def test_task_list(self):
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, 200)

    def test_task_detail(self):
        response = self.client.get('/tasks/1')
        self.assertEqual(response.status_code, 200)

    def test_task_create_for_unauthorized_user(self):
        client = Client()
        response = client.post(reverse('tasks:list'), {'title': 'Test', 'description': 'Testing', 'price': 50})
        self.assertEqual(response.status_code, 401)





