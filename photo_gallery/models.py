from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    """A tag that can be applied to photos."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    """A photo with title, description, image, tags, and uploader."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')
    tags = models.ManyToManyField(Tag, blank=True, related_name='photos')
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.filter(value='like').count()

    def total_dislikes(self):
        return self.likes.filter(value='dislike').count()


class Like(models.Model):
    """A like or dislike on a photo by a user."""

    LIKE = 'like'
    DISLIKE = 'dislike'
    VOTE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    value = models.CharField(max_length=10, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'photo')

    def __str__(self):
        return f'{self.user.username} — {self.value} — {self.photo.title}'