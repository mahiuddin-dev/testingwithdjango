from django.test import TestCase
from blog.models import Post

# Create your tests here.

class PostTest(TestCase):
    
    def setUp(self):
        self.post = Post.objects.create(title='Test Title', author='Test Author', slug='test-title')
    
    def test_post_model(self):
        data = self.post
        self.assertTrue(isinstance(data, Post))
        self.assertEqual(str(data), 'Test Title')