import datetime
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Author, Post, Category, Comment


# To bypass authentication entirely and force all requests by the test client
# to be automatically treated as authenticated

#user = User.objects.get(username='lauren')
#client = APIClient()
#client.force_authenticate(user=None, token=None)
# Include an appropriate `Authorization:` header on all requests.

# token = Token.objects.get(user__username='admin')
# client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='Token 9f56fa6ea710e301adc0ab26f6295d9441a70bb0')


class PostsTests(APITestCase):

    # Include an appropriate `Authorization:` header on all requests.
    def setUp(self):
        user_test_01 = User.objects.create_user(username='Horowitz', password='ydtgrty1')
        user_test_01.save()
        self.user_test_01_token = Token.objects.create(user=user_test_01)

        self.new_category = Category.objects.create(
            category='Computer Science'
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

    def test_posts_list(self):
        # Header for authorization
        client = APIClient
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test_01_token.key)
        # Checking whether the post from setUp() method has been published
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)












# class PostsTests(APITestCase, APIClient):
#
#     def test_list_all_posts(self):
#         response = self.client.get('/api/posts/')
#         print(response.data)

    # def test_create_post(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = reverse('api/posts')
    #     data = {'name': 'DabApps'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Account.objects.count(), 1)
    #     self.assertEqual(Account.objects.get().name, 'DabApps')
