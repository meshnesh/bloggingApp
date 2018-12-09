import json
from django.test import TestCase
from .models import BlogApp

from rest_framework.test import APIClient
from rest_framework import status
from .base import BaseTest


class ModelTestCase(TestCase):
    """This class defines the test suite for the blog model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.blog_title = "My first title"
        self.blog_body = "Lorem Ipsum is simply dummy text"
        self.blogApp = BlogApp(title=self.blog_title)

    def test_model_can_create_a_blog(self):
        """Test the blogApp model can create a blog."""
        old_count = BlogApp.objects.count()
        self.blogApp.save()
        new_count = BlogApp.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.BLOG = '/blogapp/'
        self.SINGLEBLOG = '/blogapp/1/'
        self.blog_data = {
	        "title": "new title",
	        "body": "mama mia is never going to England1",
	        "description": "happy feet"
        }

    def test_create_article(self):
        '''test creating blog article'''
        response = self.client.post(self.BLOG, self.blog_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_get_articles(self):
        """Test the api can get a given blog article."""
        response = self.client.get(
            self.BLOG, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(json.loads(response.content)), 0)
    
    def test_api_can_get_single_article(self):
        '''Test the api can get a single article'''
        self.client.post(self.BLOG, self.blog_data, format="json")
        response = self.client.get(self.SINGLEBLOG)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(self.blog_data["title"], json.loads(response.content)["title"])

#     def test_api_can_update_blog(self):
#         """Test the api can update a given blog."""
#         update_blog = {'name': 'Something new'}
#         res = self.client.put(
#             reverse('details', kwargs={'pk': blog.id}),
#             update_blog, format='json'
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)

#     def test_api_can_delete_blog(self):
#         """Test the api can delete a blog."""
#         blog = BlogApp.objects.get()
#         response = self.client.delete(
#             reverse('details', kwargs={'pk': blog.id}),
#             format='json',
#             follow=True)

#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
