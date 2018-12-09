"""test configurations"""
import json
from django.test import TestCase
from rest_framework.test import APIClient


class BaseTest(TestCase):
    """
      Test blog views
      :param: TestCase: Testing class initializer
    """

    def setUp(self):
        """Define the test client"""
        # define constant urls used throughout tests
        self.BLOG = '/api/articles/'
        self.BLOG = '/api/articles/{}/'

        self.client = APIClient()

       

        # define article data for create an article
        self.test_article_data = {
            "title": "test title",
            "body": "This is me testing. This line should be long enough to pass as a story.",
            "description": "testing"
        }

    def create_article(self, article):
        return self.client.post(
            self.BLOG,
            article,
            format='json'
        )
