from django.test import TestCase
from django.test import Client
from projectwe.models import Project, User


class ProjectTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="tester", password="pass", email="test@example.com")
        Project.objects.create(name="Test Project1", created_by=user)

    def test_new_project_create(self):
        project = Project.objects.get(slug="test-project1")
        user = User.objects.get(username="tester")
        self.assertEqual(project.name, "Test Project1")
        self.assertEqual(project.created_by.username, user.username)