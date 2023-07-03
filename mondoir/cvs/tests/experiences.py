from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from ..models import Experience, CV
from ..models.experiences import PositionType
from ..api.serializers import ExperienceSummarySerializer

User = get_user_model()

EXPERIENCE_URL = reverse('experience-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class ExperienceTest(APITestCase):

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
        response = self.client.get(EXPERIENCE_URL, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_experience(self):
        """Test retrieving experience"""
        Experience.objects.create(
            user=self.user,
            cv=self.cv,
            company_name='Misalearn',
            position=PositionType.SOFTWARE_ENGINEER,
            start_date='2023-05-01',
            description="backed developer with more than 5 years experience"

        )
        self.authenticate_client()
        res = self.client.get(EXPERIENCE_URL)
        experiences = Experience.objects.all().order_by('-company_name')
        serializer = ExperienceSummarySerializer(experiences, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(_client_result(res), serializer.data)

    def test_search_qeury_params_experience(self):
        """Test search by query params experience"""
        Experience.objects.create(
            user=self.user,
            cv=self.cv,
            company_name='Misalearn',
            position=PositionType.SOFTWARE_ENGINEER,
            start_date='2023-02-01',
            description="backed developer with more than 5 years experience"
        )
        Experience.objects.create(
            user=self.user,
            cv=self.cv,
            company_name='farafan',
            position=PositionType.SOFTWARE_ENGINEER,
            start_date='2023-04-01',
            description="backed developer with more than 5 years experience"
        )
        self.authenticate_client()
        res_1 = self.client.get(EXPERIENCE_URL, {'start_date_after': '2023-01-01'})
        res_2 = self.client.get(EXPERIENCE_URL, {'start_date_after': '2023-08-01'})
        res_3 = self.client.get(EXPERIENCE_URL, {'start_date_after': '2023-03-01'})
        self.assertEqual(len(_client_result(res_1)), 2)
        self.assertEqual(len(_client_result(res_2)), 0)
        self.assertEqual(len(_client_result(res_3)), 1)

    def test_create_experience(self):
        """Test create experience"""
        payload1 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "company_name": 'farafan',
            "start_date": '2023-02-01',
            "description": "backed developer with more than 5 years experience"
        }
        payload2 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "company_name": 'mondoir',
            "start_date": '2023-04-01',
            "description": "frontend developer with more than 5 years experience"
        }
        self.authenticate_client()
        res_1 = self.client.post(EXPERIENCE_URL, payload1)
        res_2 = self.client.post(EXPERIENCE_URL, payload2)
        self.assertEqual(res_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_2.status_code, status.HTTP_201_CREATED)

        experiences = Experience.objects.all()
        self.assertEqual(len(experiences), 2)
