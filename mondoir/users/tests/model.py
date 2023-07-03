from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

User = get_user_model()


class TestUser(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='username1', password="pases1234", is_staff=True)
        User.objects.create_user(username='username2', password="passr1234", is_staff=True)
        User.objects.create_user(username='username3', password="paess534", is_active=False)

    def test_check_user(self):
        """
        check
        """
        self.assertEqual(
            User.objects.create_superuser(username='superuser', password="passr1234", is_staff=True).username, 'superuser'
        )
        self.assertTrue(User.objects.get(username='username2').is_staff)
        self.assertFalse(User.objects.get(username='username3').is_staff)

    def test_active(self):
        """
        Active user
        """
        self.assertEqual(User.objects.active().count(), 2)

    # TODO: test strong passwod
    # TODO: test userinformation

