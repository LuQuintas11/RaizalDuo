from django.test import TestCase
from website.models import Post
from django.utils import timezone
from django.urls import reverse
import json
import unittest


class TestViews(unittest.TestCase):
    
    def test_title(self, title='test', content='this is  a test'):
        post=Post


        self.assertEqual(post.title, 'test')
        self.assertEqual(post.content, 'this is a test')


if __name__ == "__main__":
    unittest.main()

