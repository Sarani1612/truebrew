from django.test import TestCase
from django.contrib.auth.models import User
from .forms import ContactMessageForm


class TestViews(TestCase):
    '''
    Tests correct pages are shown for users that are not logged in
    '''
    def test_home_page(self):
        page = self.client.get('/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')

    def test_contact_page(self):
        page = self.client.get('/contact/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'contact.html')

    def test_contact_page_logged_in_user(self):
        '''
        Tests the email field is prepolulated when a user is logged in
        '''
        self.testuser = User.objects.create_user(username='johnsmith', email='john@smith.com', password='Teapot486')
        self.client.login(username='johnsmith', password='Teapot486')

        page = self.client.get('/contact/')

        self.assertContains(page, '<input type="email" name="email" value="john@smith.com" maxlength="254" class=" form-control" required id="id_email">')

    def test_contact_form(self):
        '''
        Tests form is valid without a user
        '''
        form = ContactMessageForm(
            {'user': '',
            'email': 'john@smith.com',
            'title': 'Test Title',
            'message_body': 'Test email message body'
            })

        self.assertTrue(form.is_valid())

    def test_send_message(self):
        '''
        Tests the page redirects correctly after submitting form
        '''
        page = self.client.post('/contact/', {'email': 'john@smith.com', 'title': 'Test Title', 'message_body': 'Test email message body'})

        self.assertRedirects(page, '/contact/', status_code=302, target_status_code=200)