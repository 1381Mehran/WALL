from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserAccountManager

class UserAccount(AbstractUser):
    username = models.CharField(
        max_length=40,
        db_index=True,
        verbose_name=_('username'),
        unique=True
    )
    first_name = None
    last_name = None
    last_login = None
    email = None
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
