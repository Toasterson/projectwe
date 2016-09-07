from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    members = models.ManyToManyField(BaseUser, blank=True, related_name='project')
    created_by = models.ForeignKey(BaseUser, related_name='created_by')
    idea = models.TextField(blank=True)
    goal = models.TextField(blank=True)
    state = models.TextField(blank=True)
    next_steps = models.TextField(blank=True)
    preferred_skills = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='project_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projectwe:detail', kwargs={'pk': self.pk})
