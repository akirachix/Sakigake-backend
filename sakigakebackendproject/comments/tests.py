from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from comments.models import Comment
from django.core.exceptions import ObjectDoesNotExist

class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_comment(self):
        data = {
            'commentor': 'Alice Williams',
            'content': 'Test comment content',
        }
        response = self.client.post(reverse('comment-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().commentor, 'Alice Williams')
    
    
        
    def test_create_comment_missing_data(self):
        data = {
        'commentor': 'Alice Williams',    
        }
        response = self.client.post(reverse('comment-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Comment.objects.count(), 0)
    
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
    
    def test_get_invalid_comment(self):
        invalid_comment_id = 100
        with self.assertRaises(ObjectDoesNotExist):
            self.client.get(reverse('comment-detail', args=[invalid_comment_id]))  
    
    def test_update_comment(self):
        comment = Comment.objects.create(commentor='Alice', content='Test Comment')
        updated_data = {
            'commentor': 'Updated Commentor',
            'content': 'Updated Content',
        }
        response = self.client.put(reverse('comment-detail', args=[comment.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get(id=comment.id).commentor, 'Updated Commentor')
    
    def test_update_invalid_comment(self):
        invalid_comment_id = 90
        updated_data = {
        'commentor': 'Updated Commentor',
        'content': 'Updated Content',
        }
        with self.assertRaises(ObjectDoesNotExist):
            self.client.put(reverse('comment-detail', args=[invalid_comment_id]), updated_data, format='json')
     
    def test_delete_comment(self):
        comment = Comment.objects.create(commentor='Alice', content='Test Comment')
        response = self.client.delete(reverse('comment-detail', args=[comment.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
        
    def test_delete_invalid_comment(self):
        invalid_comment_id = 999
        with self.assertRaises(ObjectDoesNotExist):
            self.client.delete(reverse('comment-detail', args=[invalid_comment_id]))
            