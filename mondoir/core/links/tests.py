from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from .models import Link
from .api.serializers import LinkSummarySerializer

User = get_user_model()

LINK_URL = reverse('link-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class LinkTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testname123', password='testpa234ssword')
        self.user_staff = User.objects.create_user(
            username='ternamestaff123',
            password='testpasswor234dstaff',
            is_staff=True
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
        response = self.client.get(LINK_URL, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_link(self):
        """Test retrieving link"""
        Link.objects.create(
            user=self.user,
            description="description",
            url="http://www.google.com",
            title='test',
        )
        self.authenticate_client()
        res = self.client.get(LINK_URL)
        links = Link.objects.all().order_by('-title')
        serializer = LinkSummarySerializer(links, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(_client_result(res), serializer.data)

    def test_search_qeury_params_link(self):
        """Test search by query params link"""
        Link.objects.create(
            user=self.user,
            description="description",
            url="http://www.google.com",
            title='custom',
        )
        Link.objects.create(
            user=self.user,
            description="description",
            url="http://www.google.com",
            title='up',
        )
        self.authenticate_client()
        res_1 = self.client.get(LINK_URL, {'title': 'u'})
        res_2 = self.client.get(LINK_URL, {'title': 'up'})
        res_3 = self.client.get(LINK_URL, {'title': 'cus'})
        self.assertEqual(len(_client_result(res_1)), 2)
        self.assertEqual(len(_client_result(res_2)), 1)
        self.assertEqual(len(_client_result(res_3)), 1)

    def test_create_link(self):
        """Test create link"""
        payload1 = {
            "user": self.user.pk,
            "description": "description",
            "url": "http://www.google.com",
            "title": 'backend',
        }
        payload2 = {
            "user": self.user.pk,
            "description": "description",
            "url": "http://www.google.com",
            "title": 'frontend',
        }
        self.authenticate_client()
        res_1 = self.client.post(LINK_URL, payload1)
        res_2 = self.client.post(LINK_URL, payload2)
        self.assertEqual(res_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_2.status_code, status.HTTP_201_CREATED)

        links = Link.objects.all()
        self.assertEqual(len(links), 2)

    # def test_update_skill(self):
    #     """Test update skill"""
    #     changed_title = 'frontend'
    #     obj = Skill.objects.create(
    #         user=self.user,
    #         title='test1',
    #     )
    #     self.authenticate_client()
    #     res = self.client.patch(LINK_URL, {"title": changed_title}, kwargs={'pk': obj.pk})
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    #     skills = Skill.objects.all().order_by('-title')
    #     serializer = SkillSummarySerializer(skills, many=True)
    #     self.assertEqual(len(skills), 2)
