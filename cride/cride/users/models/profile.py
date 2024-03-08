"""Profile model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModels


class Profile(CRideModels):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=501, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveBigIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
