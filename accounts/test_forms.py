from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, EditUserInfoForm, EditUserForm

# Create your tests here.
class TestUserRegistrationForm(TestCase):

    def test_register_user(self):
        form = UserRegistrationForm(
            {'username': 'User123',
            'email': 'user@user.com',
            'password1': 'Teapot486',
            'password2': 'Teapot486'
            })

        self.assertTrue(form.is_valid())

    def test_correct_msg_for_passwords_not_matching(self):
        form = UserRegistrationForm(
            {'username': 'User123',
            'email': 'user@user.com',
            'password1': 'Teapot486',
            'password2': 'Teapot485'
            })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u"The two password fields didn't match."])

    def test_correct_msg_for_invalid_email(self):
        form = UserRegistrationForm(
            {'username': 'User123',
            'email': 'user@user',
            'password1': 'Teapot486',
            'password2': 'Teapot486'
            })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u"Enter a valid email address."])


class TestEditUserForm(TestCase):
    '''
    Tests the correct pages and content is shown to logged in users
    '''
    def setUp(self):
        self.testuser = User.objects.create_user(username='johnsmith', email='john@smith.com', password='Teapot486')
    
    def tearDown(self):
        self.testuser.delete()

    '''
    Tests the user form can be filled out and is valid
    '''
    def test_edit_user_form(self):
        user = User.objects.get(id=1)
        form = EditUserForm(
            {'username': 'john',
            'email': "john@smith.com",
            'first_name': 'John',
            'last_name': 'Smith'
            })

        self.assertTrue(form.is_valid())

    def test_edit_user_info_form(self):
        '''
        test the user form accepts blank fields
        '''
        user = User.objects.get(id=1)
        form = EditUserInfoForm(
            {'street_address1': '12 Test St',
            'street_address2': '',
            'town_or_city': 'Test City',
            'postcode': '',
            'county': 'Cork',
            'country': 'Ireland',
            'phone_number': '0123456789'
            })
            
        self.assertTrue(form.is_valid())