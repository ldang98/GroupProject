from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages



class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.sign_up_url = reverse('sign_up')
        self.logout_url = reverse('users')


    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_sign_up_GET(self):
        response = self.client.get(self.sign_up_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')


    def test_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)


    def test_sign_up_POST_create_new_account(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': 'John',
            'last_name' : 'Doe',
            'username' : 'JohnD',
            'email' : 'johnd@gmail.com',
            'password1' : 'abioh45',
            'password2' : 'abioh45'
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 1)


    def test_sign_up_POST_password_not_match(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': 'John',
            'last_name' : 'Doe',
            'username' : 'JohnD',
            'email' : 'johnd@gmail.com',
            'password1' : 'abioh45',
            'password2' : 'abioh46'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '**ERROR: Password not matching')


    def test_sign_up_POST_no_first_name(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': '',
            'last_name' : 'Doe',
            'username' : 'JohnD',
            'email' : 'johnd@gmail.com',
            'password1' : 'abioh45',
            'password2' : 'abioh45'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '**ERROR: First Name is required')


    def test_sign_up_POST_no_last_name(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': 'John',
            'last_name' : '',
            'username' : 'JohnD',
            'email' : 'johnd@gmail.com',
            'password1' : 'abioh45',
            'password2' : 'abioh45'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '**ERROR: Last Name is required')


    def test_sign_up_POST_no_username(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': 'John',
            'last_name' : 'Doe',
            'username' : '',
            'email' : 'johnd@gmail.com',
            'password1' : 'abioh45',
            'password2' : 'abioh45'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '**ERROR: Username is required')


    def test_sign_up_POST_no_email(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': 'John',
            'last_name' : 'Doe',
            'username' : 'JohnD',
            'email' : '',
            'password1' : 'abioh45',
            'password2' : 'abioh45'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '**ERROR: Email address is required')


    def test_sign_up_POST_no_pass(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': 'John',
            'last_name' : 'Doe',
            'username' : 'JohnD',
            'email' : 'johnd@gmail.com',
            'password1' : '',
            'password2' : 'abioh45'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[0]), '**ERROR: Password not matching')
        self.assertEqual(str(messages[1]), '**ERROR: Password is required')


    def test_sign_up_POST_no_info(self):
        response = self.client.post(self.sign_up_url, data={
            'first_name': '',
            'last_name' : '',
            'username' : '',
            'email' : '',
            'password1' : '',
            'password2' : ''
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 5)
        self.assertEqual(str(messages[0]), '**ERROR: First Name is required')
        self.assertEqual(str(messages[1]), '**ERROR: Last Name is required')
        self.assertEqual(str(messages[2]), '**ERROR: Username is required')
        self.assertEqual(str(messages[3]), '**ERROR: Email address is required')
        self.assertEqual(str(messages[4]), '**ERROR: Password is required')


