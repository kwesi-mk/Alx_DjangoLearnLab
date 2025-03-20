from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogPostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_post_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        response = self.client.get(f'/post/{self.post.id}/')
        self.assertEqual(response.status_code, 200)


class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Test Comment')

    def test_add_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/comment/{self.comment.id}/edit/', {'content': 'Updated Comment'})
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')

    def test_delete_comment(self):
        self.client.login(username='testuser', password='password') 
        response = self.client.post(f'/comment/{self.comment.id}/delete/')
        self.assertEqual(response.status_code, 302) # Redirects to post-detail
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())   


class BlogFeatureTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post1 = Post.objects.create(title = 'Django Search', content='Testing search feature', author=self.user)
        self.post1.tags.add('Django', 'Search')
        self.post2 = Post.objects.create(title= 'Machine Learning', content='AI and ML insights', author=self.user)
        self.post2.tags.add('AI', 'ML')

    def test_search_functionality(self):
        response = self.client.get('/search/?q=Django')
        self.assertContains(response, 'Django Search')

    def test_tag_filtering(self):
        response = self.client.get('/tags/Django')
        self.assertContains(response, 'Django Search')
        self.assertNotContains(response, 'Machine Learning')