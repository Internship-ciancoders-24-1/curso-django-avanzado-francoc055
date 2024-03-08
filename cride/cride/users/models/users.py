"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModels


class User(CRideModels, AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={'unique': 'A user with that email already exists.'}
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$'
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        default=True,
    )

    is_verified = models.BooleanField(
        default=False
    )

    def __str__(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username
