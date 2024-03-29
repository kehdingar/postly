from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from posts.models import Post, Like
from posts.serializers import PostSerializer, LikeSerializer

User = get_user_model()

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_create_post(self):
        url = '/posts/'
        data = {'title': 'New Post', 'content': 'This is a new post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=2).title, 'New Post')

    def test_get_post_list(self):
        url = '/posts/'
        response = self.client.get(url)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_detail(self):
        url = f'/posts/{self.post.id}/'
        response = self.client.get(url)
        serializer = PostSerializer(self.post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        

    def test_update_post(self):
        url = f'/posts/{self.post.id}/'
        data = {'title': 'Updated Post', 'content': 'This post has been updated.'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=self.post.id).title, 'Updated Post')        

    def test_delete_post(self):
        url = f'/posts/{self.post.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)    


class LikeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_like_post(self):
        url = f'/posts/{self.post.id}/like/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(Like.objects.get().user, self.user)

    def test_unlike_post(self):
        like = Like.objects.create(post=self.post, user=self.user)
        url = f'/posts/{self.post.id}/like/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.count(), 0)