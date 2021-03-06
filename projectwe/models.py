from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from django_countries.fields import CountryField


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(blank=True, upload_to='user_images')
    country = CountryField()

    def __str__(self):
        return self.get_display_name()

    def get_display_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    members = models.ManyToManyField(User, blank=True, related_name='member_of_projects')
    created_by = models.ForeignKey(User, related_name='founded_projects')
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

    def is_member_or_founder(self, profile):
        if self.created_by == profile:
            return True

        if self.members.filter(pk=profile.id).exists():
            return True

        return False
