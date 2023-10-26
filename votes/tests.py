from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from posts.models import Post
from votes.models import Vote
from votes.serializers import VoteSerializer

User = get_user_model()

class VoteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
        self.user2 = User.objects.create_user(username='testuser2', email='testuser2@example.com', password='test2pass123')

        self.client = APIClient()
        self.client2 = APIClient()

        # Force authentication
        self.client.force_authenticate(user=self.user)
        self.client2.force_authenticate(user=self.user2)

        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)
        self.post2 = Post.objects.create(title='Test Post2', content='This is a test post 2.', author=self.user)
        self.vote = Vote.objects.create(user=self.user, post=self.post, value=1)

    def test_create_upvote(self):
        url = '/votes/vote/'
        data = {'user':self.user.pk,'post': self.post2.id, 'value': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 2)
        self.assertEqual(Vote.objects.get(id=self.vote.id).value, 1)
