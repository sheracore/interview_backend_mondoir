from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from ..models import Certificate, CV
from ..api.serializers import CertificateSummarySerializer

User = get_user_model()

CERTIFICATE_URL = reverse('certificate-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class CertificateTest(APITestCase):

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
        response = self.client.get(CERTIFICATE_URL, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_certificate(self):
        """Test retrieving certificate"""
        Certificate.objects.create(
            user=self.user,
            cv=self.cv,
            name='CCNA',
            issuer="IBM",
            issuer_date='2023-05-01',

        )
        self.authenticate_client()
        res = self.client.get(CERTIFICATE_URL)
        certificates = Certificate.objects.all().order_by('-name')
        serializer = CertificateSummarySerializer(certificates, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(_client_result(res), serializer.data)

    def test_search_qeury_params_certificate(self):
        """Test search by query params certificate"""
        Certificate.objects.create(
            user=self.user,
            cv=self.cv,
            name='DJANGO',
            issuer="IBM",
            issuer_date='2023-01-01',
        )
        Certificate.objects.create(
            user=self.user,
            cv=self.cv,
            name='CCNA',
            issuer="Udemy",
            issuer_date='2023-04-01',
        )
        self.authenticate_client()
        res_1 = self.client.get(CERTIFICATE_URL, {'issuer_date_after': '2023-01-01'})
        res_2 = self.client.get(CERTIFICATE_URL, {'issuer_date_after': '2023-08-01'})
        res_3 = self.client.get(CERTIFICATE_URL, {'issuer_date_after': '2023-03-01'})
        self.assertEqual(len(_client_result(res_1)), 2)
        self.assertEqual(len(_client_result(res_2)), 0)
        self.assertEqual(len(_client_result(res_3)), 1)

    def test_create_certificate(self):
        """Test create certificate"""
        payload1 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "name": 'CCNA',
            "issuer": "Udemy",
            "issuer_date": '2023-01-01',
        }
        payload2 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "name": 'DJANGO',
            "issuer": "IBM",
            "issuer_date": '2023-04-01',
        }
        self.authenticate_client()
        res_1 = self.client.post(CERTIFICATE_URL, payload1)
        res_2 = self.client.post(CERTIFICATE_URL, payload2)
        self.assertEqual(res_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_2.status_code, status.HTTP_201_CREATED)

        certificates = Certificate.objects.all()
        self.assertEqual(len(certificates), 2)
