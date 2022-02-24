from django.test import TestCase, Client
from rest_framework import status
import project.tests.constants as constants

class TestMonitoringAppUrls(TestCase):

    client = Client()

    def test_resolution_for_health_check(self):
        response = self.client.get(constants.URL_MONITORING.format('health-check'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resolution_for_sentry(self):
        with self.assertRaises(ZeroDivisionError):
            response = self.client.get(constants.URL_MONITORING.format('sentry'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestProjectAppUrls(TestCase):

    client = Client()

    def test_resolution_for_list_create(self):
        response = self.client.get(constants.URL_PROJECT_LIST_CREATE.format(constants.USER))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resolution_for_detail(self):
        print(constants.URL_PROJECT_DETAIL.format(
            constants.USER, constants.PROJECT))
        response = self.client.get(constants.URL_PROJECT_DETAIL.format(
            constants.USER, constants.PROJECT))
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)