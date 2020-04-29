from django.test import TestCase, Client
from django.contrib.auth.models import User
from .views import user_account


class TestViews(TestCase):
    '''
    Tests correct pages are shown for users that are not logged in
    '''
    def test_login_page(self):
        page = self.client.get('/accounts/login/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    def test_register_page(self):
        page = self.client.get('/accounts/register/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')
    
    def test_redirect_from_account_page_when_not_logged_in(self):
        page = self.client.get('/accounts/account/')

        self.assertEqual(page.status_code, 302)
        self.assertTemplateNotUsed(page, 'account.html')
        self.assertEqual(page.url, '/accounts/login/?next=/accounts/account/')


class TestViewsLoggedInUser(TestCase):
    '''
    setUp and tearDown methods run before and after each test
    '''
    def setUp(self):
        self.testuser = User.objects.create_user(username='johnsmith', email='john@smith.com', password='Teapot486')
        self.client.login(username='johnsmith', password='Teapot486')
    
    def tearDown(self):
        self.testuser.delete()

    '''
    Tests the correct pages and content is shown to logged in users
    '''
    def test_editaccount_page(self):
        page = self.client.get('/accounts/edit/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'editaccount.html')

    def test_login_page_when_user_is_logged_in(self):
        page = self.client.get('/accounts/login/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
        self.assertContains(page, '<p>It looks like you are already logged in.</p>')

    def test_register_page_when_user_is_logged_in(self):
        page = self.client.get('/accounts/register/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')
        self.assertContains(page, '<p>It looks like you already have an account and are signed in.</p>')

    def test_account_page(self):
        page = self.client.get('/accounts/account/')
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'account.html')
