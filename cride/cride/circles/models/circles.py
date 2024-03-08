"""Circle model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModels


class Circle(CRideModels):
    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/picture', blank=True, null=True)

    members = models.ManyToManyField(
        'users.User',
        through='circles.Membership',
        through_fields=('circle', 'user')
    )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        default=False
    )

    is_public = models.BooleanField(
        default=True
    )

    is_limited = models.BooleanField(
        default=False
    )

    members_limit = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.name

    class Meta(CRideModels.Meta):
        ordering = ['-rides_taken', '-rides_offered']
