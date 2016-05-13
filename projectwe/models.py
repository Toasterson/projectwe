from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    name = models.TextField(blank=True)
    idea = models.TextField(blank=True)
    goal = models.TextField(blank=True)
    state = models.TextField(blank=True)
    next_steps = models.TextField(blank=True)
    preferred_skills = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='project_images')

    def __str__(self):
        return self.title


class ProjectMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

