from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from ..models import Skill, CV
from ..api.serializers import SkillSummarySerializer

User = get_user_model()

SKILL_URL = reverse('skill-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class SkillTest(APITestCase):

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
        response = self.client.get(SKILL_URL, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_skill(self):
        """Test retrieving skill"""
        Skill.objects.create(
            cv=self.cv,
            user=self.user,
            title='test1',
        )
        self.authenticate_client()
        res = self.client.get(SKILL_URL)
        skills = Skill.objects.all().order_by('-title')
        serializer = SkillSummarySerializer(skills, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(_client_result(res), serializer.data)

    def test_search_qeury_params_skill(self):
        """Test search by query params skill"""
        Skill.objects.create(
            cv=self.cv,
            user=self.user,
            title='backend',
        )
        Skill.objects.create(
            cv=self.cv,
            user=self.user,
            title='frontend',
        )
        self.authenticate_client()
        res_1 = self.client.get(SKILL_URL, {'title': 'end'})
        res_2 = self.client.get(SKILL_URL, {'title': 'back'})
        res_3 = self.client.get(SKILL_URL, {'title': 'front'})
        self.assertEqual(len(_client_result(res_1)), 2)
        self.assertEqual(len(_client_result(res_2)), 1)
        self.assertEqual(len(_client_result(res_3)), 1)

    def test_create_skill(self):
        """Test create skill"""
        payload1 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "title": 'backend',
        }
        payload2 = {
            "cv": self.cv.pk,
            "user": self.user.pk,
            "title": 'frontend',
        }
        self.authenticate_client()
        res_1 = self.client.post(SKILL_URL, payload1)
        res_2 = self.client.post(SKILL_URL, payload2)
        self.assertEqual(res_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_2.status_code, status.HTTP_201_CREATED)

        skills = Skill.objects.all()
        self.assertEqual(len(skills), 2)

    # def test_update_skill(self):
    #     """Test update skill"""
    #     changed_title = 'frontend'
    #     obj = Skill.objects.create(
    #         user=self.user,
    #         title='test1',
    #     )
    #     self.authenticate_client()
    #     res = self.client.patch(SKILL_URL, {"title": changed_title}, kwargs={'pk': obj.pk})
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    #     skills = Skill.objects.all().order_by('-title')
    #     serializer = SkillSummarySerializer(skills, many=True)
    #     self.assertEqual(len(skills), 2)
