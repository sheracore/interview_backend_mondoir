from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

# from .models import Link
# from .api.serializers import LinkSummarySerializer

User = get_user_model()

LINK_URL = reverse('link-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class UserTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testname123', password='testpa234word')
        self.user_staff = User.objects.create_user(
            username='ternamestaff123',
            password='testpasswor234dstaff',
            is_staff=True
        )

    # def authenticate_client(self):
    #     self.client = APIClient()
    #     self.client.force_authenticate(user=self.user)

    def test_protected_endpoint(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)

        self.headers = {"HTTP_AUTHORIZATION": f"{settings.JWT_AUTH.get('JWT_AUTH_HEADER_PREFIX')} {token}"}
        response = self.client.get(LINK_URL, **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register(self):
        """test user register"""
        payload = {
            "username": "tesnetname123",
            "password": "tenestpa234word"
        }
        res = self.client.post('/api/users_register/', payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        User.objects.create_user(username='t223estname123', password='testp223a234word')
        payload = {
            "username": "testname123",
            "password": "testpa234word"
        }
        res = self.client.post('/api/token_auth/', payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_verify_token(self):
        User.objects.create_user(username='usernameverify', password='testpsdf234f34d')
        payload = {
            "username": "usernameverify",
            "password": "testpsdf234f34d"
        }
        res_login = self.client.post('/api/token_auth/', payload)
        login_token = res_login.data.get('token')
        res_verify = self.client.post('/api/token_verify/', {"token": login_token})
        verify_token = res_verify.data.get('token')
        self.assertEqual(login_token, verify_token)
