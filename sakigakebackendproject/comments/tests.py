from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from comments.models import Comment
from comments.serializers import CommentSerializer

class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_comment(self):
        data = {
            'commentor': 'John Doe',
            'content': 'Test comment content',
        }
        response = self.client.post(reverse('comment-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().commentor, 'John Doe')

    def test_get_comments(self):
        Comment.objects.create(commentor='Alice', content='Comment 1')
        Comment.objects.create(commentor='Bob', content='Comment 2')

        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_comment(self):
        comment = Comment.objects.create(commentor='Alice', content='Test Comment')
        response = self.client.get(reverse('comment-detail', args=[comment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['commentor'], 'Alice')

    def test_update_comment(self):
        comment = Comment.objects.create(commentor='Alice', content='Test Comment')
        updated_data = {
            'commentor': 'Updated Commentor',
            'content': 'Updated Content',
        }
        response = self.client.put(reverse('comment-detail', args=[comment.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get(id=comment.id).commentor, 'Updated Commentor')

    def test_delete_comment(self):
        comment = Comment.objects.create(commentor='Alice', content='Test Comment')
        response = self.client.delete(reverse('comment-detail', args=[comment.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
