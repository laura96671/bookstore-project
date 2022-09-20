from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser, models.Model):
    your_description = models.TextField(max_length=150, blank=True, default="What's up?")
    pass
