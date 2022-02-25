from urllib.parse import urldefrag
from django.test import TestCase
from django.urls import reverse
import rule.tests.constants as constants

class TestRuleUrls(TestCase):
    def test_resolution_for_list_create(self):
        url = reverse('list_create', args=[constants.USER, constants.PROJECT])
        self.assertEqual(url, constants.URL_RULE_LIST_CREATE.format(
            constants.USER, constants.PROJECT))

    def test_resolution_for_detail(self):
        url = reverse('detail', args=[constants.USER, constants.PROJECT, 
            constants.RULE])
        self.assertEqual(url, constants.URL_PROJECT_DETAIL.format(
            constants.USER, constants.PROJECT, constants.RULE))