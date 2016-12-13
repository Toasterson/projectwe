from registration import signals
from django.dispatch import receiver
from projectwe.models import User as Profile


@receiver(signals.user_registered)
def create_profile(sender, user, request, **kwargs):
    Profile.objects.create(user=user)
