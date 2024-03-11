from django.db import models

from cride.utils.models import CRideModels

class Membership(CRideModels):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    circle = models.ForeignKey('circles.circle', on_delete=models.CASCADE)

    is_admin = models.BooleanField(default=False)

    used_invitations = models.PositiveSmallIntegerField(default=0)
    remaining_invitations = models.PositiveSmallIntegerField(default=0)
    invited_by = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL, related_name='invited_by')

    rides_taken = models.PositiveBigIntegerField(default=0)
    rides_offered = models.PositiveBigIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'@{self.user.username} at # {self.circle.slug_name}'