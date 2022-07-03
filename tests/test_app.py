# tests/test_app.py

from app.generators import generate_random_name, generate_random_email, generate_random_content
from app import app
import unittest
import os
os.environ['TESTING'] = 'true'


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>TyRoyLog Portfolio</title>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    # TODO Add more tests relating to the /api/timeline_post GET and POST apis
    def test_get_and_post_timeline(self):
        
        # Testing POST method of /api/timeline_post
        name = generate_random_name()
        email = generate_random_email(name)
        content = generate_random_content()

        response = self.client.post("/api/timeline_post", data={
            "name": name,
            "email": email,
            "content": content
        })
        
        assert response.status_code == 200
        assert response.is_json

        json = response.get_json()

        self.assertEqual(name, json['name'])

        self.assertEqual(email, json['email'])

        self.assertEqual(content, json['content'])
        
        self.assertEqual(json['id'], 1)

        # Testing GET method of /api/timeline_post

        response = self.client.get("/api/timeline_post")

        json = response.get_json()
        assert response.status_code == 200
        assert response.is_json

        print(json['timeline_posts'][0])

        values = list(json['timeline_posts'][0].values())
        

        self.assertIn(name, values)

        self.assertIn(email, values)

        self.assertIn(content, values)

        # Clear all timeline posts
        self.client.delete("/api/timeline_post")

    # TODO Add more tests relating to the timeline page
    def test_timeline_page(self):
        response = self.client.get("/timeline/")
        html = response.get_data(as_text=True)
        

    def test_malformed_timeline_post(self):
        # POST request with missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John"
        })

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

        # POST request with missing email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "content": "Hello world, I'm John"
        })

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
