# -*- coding: utf-8 -*-
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, MinLengthValidator
from django.db.models.signals import post_save
from rest_framework.exceptions import ValidationError

from mondoir.utilities.db.models import DataModel


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset()

    def active(self):
        return self.get_queryset().filter(is_active=True)

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username, and password.
        """
        if not username:
            raise ValueError("users most have an username address")
        try:
            self.validate_password_strength(password)
            with transaction.atomic():
                user = self.model(username=username, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password=password, **extra_fields)

    def validate_password_strength(self, password):
        # Example: Checking if the password has at least 8 characters, contains both letters and numbers
        if len(password) < 8 or not any(char.isalpha() for char in password) or not any(
                char.isdigit() for char in password):
            raise ValidationError("Password must be at least 8 characters long and contain both letters and numbers")


# PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin, DataModel):
    username = models.CharField(
        unique=True,
        max_length=18,
        validators=[
            RegexValidator(regex=r'^\w*-*\w*$', message=_('Username must be Alphanumeric'), code='invalid_username'),
            MinLengthValidator(3)
        ],
        verbose_name=_('Username'),
    )
    is_staff = models.BooleanField(default=False, verbose_name=_('Is staff'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "users"
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return '{}'.format(self.username)

    def info(self):
        obj = self.userinformation_set.get_or_create(
            user=self,
            is_staff=self.is_staff,
            is_active=self.is_active
        )
        return obj


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.info()


post_save.connect(post_save_user_model_receiver, sender=User)
