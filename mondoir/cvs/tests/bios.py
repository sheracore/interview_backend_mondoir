from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from ..models import Bio, CV
from ..api.serializers import BioSummarySerializer

User = get_user_model()

BIO_URL = reverse('bio-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class BioTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testname123', password='testpa234ssword')
        self.user_staff = User.objects.create_user(
            username='ternamestaff123',
            password='testpasswor234dstaff',
            is_staff=True
        )
        self.cv = CV.objects.create(
            user=self.user,
            title='backend'
        )

    def authenticate_client(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_protected_endpoint(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)

        self.headers = {"HTTP_AUTHORIZATION": f"{settings.JWT_AUTH.get('JWT_AUTH_HEADER_PREFIX')} {token}"}
        response = self.client.get(BIO_URL, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_bio(self):
        """Test retrieving bio"""
        Bio.objects.create(
            user=self.user,
            cv=self.cv,
            content="Mohammad Ghaffay"
        )
        self.authenticate_client()
        res = self.client.get(BIO_URL)
        bios = Bio.objects.all().order_by('-type')
        serializer = BioSummarySerializer(bios, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(_client_result(res), serializer.data)

    def test_search_qeury_params_bio(self):
        """Test search by query params bio"""
        Bio.objects.create(
            user=self.user,
            cv=self.cv,
            content="Mohammad Ghaffary"
        )
        Bio.objects.create(
            user=self.user,
            cv=self.cv,
            content="Ayub salary"
        )
        self.authenticate_client()
        res_1 = self.client.get(BIO_URL, {'content': 'Mohammad'})
        res_2 = self.client.get(BIO_URL, {'content': 'salary'})
        res_3 = self.client.get(BIO_URL, {'content': 'ar'})
        self.assertEqual(len(_client_result(res_1)), 1)
        self.assertEqual(len(_client_result(res_2)), 1)
        self.assertEqual(len(_client_result(res_3)), 2)

    def test_create_bio(self):
        """Test create bio"""
        payload1 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "content": 'Mohammad Ghaffay',
        }
        payload2 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "content": 'aria ziabary',
        }
        self.authenticate_client()
        res_1 = self.client.post(BIO_URL, payload1)
        res_2 = self.client.post(BIO_URL, payload2)
        self.assertEqual(res_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_2.status_code, status.HTTP_201_CREATED)

        bios = Bio.objects.all()
        self.assertEqual(len(bios), 2)
