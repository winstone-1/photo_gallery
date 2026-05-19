from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class CustomUser(AbstractUser):
    """Extended user model with bio and profile picture."""

    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.username