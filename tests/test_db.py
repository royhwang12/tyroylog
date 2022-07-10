# test_db.py

import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jame@example.com', content="Hello world, I\'m Jane!")
        assert second_post.id == 2

        # TODO: Get timeline posts and assert that they are correct

        # Get first post
        first_post_from_db = TimelinePost.get_by_id(first_post.id)
        
        # Get second post
        second_post_from_db = TimelinePost.get_by_id(second_post.id)

        # id of the first post when created must be equal to id of the first post in the database
        self.assertEqual(first_post.id, first_post_from_db.id)

        # name of the first post when created must be equal to name of the first post in the database
        self.assertEqual(first_post.name, first_post_from_db.name)

        # email of the first post when created must be equal to email of the first post in the database
        self.assertEqual(first_post.email, first_post_from_db.email)

        # content of the first post when created must be equal to content of the first post in the database
        self.assertEqual(first_post.content, first_post_from_db.content)

        # created_at of the first post when created must be equal to created_at of the first post in the database
        self.assertEqual(first_post.created_at, first_post_from_db.created_at)

        # id of the second post when created must be equal to id of the second post in the database
        self.assertEqual(second_post.id, second_post_from_db.id)

        # name of the second post when created must be equal to name of the second post in the database
        self.assertEqual(second_post.name, second_post_from_db.name)

        # email of the second post when created must be equal to email of the second post in the database
        self.assertEqual(second_post.email, second_post_from_db.email)

        # content of the second post when created must be equal to content of the second post in the database
        self.assertEqual(second_post.content, second_post_from_db.content)

        # created_at of the second post when created must be equal to created_at of the second post in the database
        self.assertEqual(second_post.created_at, second_post_from_db.created_at)