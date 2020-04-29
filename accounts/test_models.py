from django.test import TestCase
from .models import UserInfo
from django.contrib.auth.models import User


class TestUserInfoModel(TestCase):
    '''
    setUp and tearDown methods run before and after each test
    '''
    def setUp(self):
        self.testuser = User.objects.create_user(username='johnsmith', email='john@smith.com', password='Teapot486')
    
    def tearDown(self):
        self.testuser.delete()

    
    def test_user_in_userinfo_object(self):
        '''
        Tests the related user id and other fields are correctly stored in UserInfo object
        '''
        user = self.testuser
        userinfo = UserInfo(user=user, street_address1='10 Test St', town_or_city='Test City')

        self.assertEqual(userinfo.user.id, 1)
        self.assertEqual(userinfo.town_or_city, 'Test City')

    def test_userinfo_string_returned(self):
        user = self.testuser
        userinfo = UserInfo(user=user, street_address1='10 Test St', town_or_city='Test City')

        self.assertEqual(str(userinfo), 'johnsmith')