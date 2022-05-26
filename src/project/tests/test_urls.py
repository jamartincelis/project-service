from django.test import TestCase
from django.urls import reverse
import project.tests.constants as constants

class TestProjectUrls(TestCase):
    def test_resolution_for_list_create(self):
        url = reverse('list_create', args=[constants.USER])
        self.assertEqual(url, constants.URL_PROJECT_LIST_CREATE.format(constants.USER))

    def test_resolution_for_detail(self):
        url = reverse('detail', args=[constants.USER, constants.PROJECT])
        self.assertEqual(url, constants.URL_PROJECT_DETAIL.format(
            constants.USER, constants.PROJECT))