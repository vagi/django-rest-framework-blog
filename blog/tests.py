#import unittest
import datetime

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Author, Post, Category, Comment


class BlogTests(APITestCase):
    '''
    This class provides testing of Blog creation
    '''
    # This method creates new user and its token, author, category and one post
    def setUp(self):
        user_test_01 = User.objects.create_user(username='Horowitz', password='ydtgrty1')
        user_test_01.save()
        self.user_test_01_token = Token.objects.create(user=user_test_01)

        self.new_category = Category.objects.create(
            category=['Computer Science']
        )

        self.new_author = Author.objects.create(
            first_name = "Ben",
            surname = "Horowitz",
            email = "ben@paypal.com",
        )

        self.new_post = Post.objects.create(
            headline="First Test Ever",
            post_text="A test case is the individual unit of testing. "
                      "It checks for a specific response to a particular set of inputs. "
                      "unittest provides a base class, TestCase , which may be used "
                      "to create new test cases.",
            category=self.new_category,
            author=self.new_author,
            pub_date=datetime.date.today(),
        )


    # Ensure the new post has been published
    def test_posts_list(self):
        # Header for authorization
        client = APIClient
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test_01_token.key)

        # Checking whether the posts
        response = self.client.get('/api/posts/')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)


    # Ensure we can create a comment to the post
    def test_create_comment_to_post(self):
        # Header for authorization
        client = APIClient
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test_01_token.key)

        data = {
            "post": 1,
            'comment_text': 'Excellent explanation, thanks!',
            'pub_date': datetime.date.today(),
            }
        response = self.client.post('/api/comments/', data)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().comment_text, 'Excellent explanation, thanks!')


    def test_create_another_post(self):
        # Header for authorization
        client = APIClient
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test_01_token.key)

        data = {
            'headline': 'Second Post',
            'post_text': 'Here must be a very long useless text',
            'category': 1,
            'author': 1,
            'pub_date': datetime.date.today(),
            }
        response = self.client.post('/api/posts/', data)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(pk=2).headline, 'Second Post')
