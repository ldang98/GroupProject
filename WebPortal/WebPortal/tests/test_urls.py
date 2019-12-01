from django.test import SimpleTestCase
from django.urls import resolve, reverse
from portal.views import login, home
from sign_up.views import sign_up
from users.views import logout



class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_sign_up_url_is_resolved(self):
        url = reverse('sign_up')
        self.assertEquals(resolve(url).func, sign_up)

    def test_logout_url_is_resolved(self):
        url = reverse('users')
        self.assertEquals(resolve(url).func, logout)