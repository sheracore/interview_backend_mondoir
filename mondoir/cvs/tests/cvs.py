from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from ..models import CV
from ..api.serializers import CVSummarySerializer

User = get_user_model()

CV_URL = reverse('cv-list')


def _client_result(res):
    """
    Use this method for paginated APIs
    """
    return res.data['results'] if 'results' in res.data else res.data


class CVTest(APITestCase):

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
        response = self.client.get(CV_URL, **self.headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_cv(self):
        """Test retrieving cv"""
        CV.objects.create(
            user=self.user,
            title='test1',
        )
        self.authenticate_client()
        res = self.client.get(CV_URL)
        cvs = CV.objects.all().order_by('-title')
        serializer = CVSummarySerializer(cvs, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(_client_result(res), serializer.data)

    def test_search_qeury_params_cv(self):
        """Test search by query params cv"""
        CV.objects.create(
            user=self.user,
            title='backend',
        )
        CV.objects.create(
            user=self.user,
            title='frontend',
        )
        self.authenticate_client()
        res_1 = self.client.get(CV_URL, {'title': 'end'})
        res_2 = self.client.get(CV_URL, {'title': 'back'})
        res_3 = self.client.get(CV_URL, {'title': 'front'})
        self.assertEqual(len(_client_result(res_1)), 2)
        self.assertEqual(len(_client_result(res_2)), 1)
        self.assertEqual(len(_client_result(res_3)), 1)

    def test_create_cv(self):
        """Test create cv"""
        payload1 = {
            "user": self.user,
            "title": 'backend',
        }
        payload2 = {
            "user": self.user,
            "title": 'frontend',
        }
        self.authenticate_client()
        res_1 = self.client.post(CV_URL, payload1)
        res_2 = self.client.post(CV_URL, payload2)
        self.assertEqual(res_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_2.status_code, status.HTTP_201_CREATED)

        cvs = CV.objects.all()
        self.assertEqual(len(cvs), 2)

    # def test_update_cv(self):
    #     """Test update cv"""
    #     changed_title = 'frontend'
    #     obj = CV.objects.create(
    #         user=self.user,
    #         title='test1',
    #     )
    #     self.authenticate_client()
    #     res = self.client.patch(reverse('cv-list', kwargs={'pk': obj.pk}), {"title": changed_title})
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #
    #     cvs = CV.objects.all().order_by('-title')
    #     serializer = CVSummarySerializer(cvs, many=True)
    #     self.assertEqual(len(cvs), 2)