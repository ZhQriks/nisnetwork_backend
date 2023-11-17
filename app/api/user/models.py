import uuid
from enum import Enum

from django.contrib.auth.models import (AbstractUser, Group, Permission,
                                        UserManager)
from django.db import models

from app.utils.base_model import BaseModel
from app.utils.error_message_formatter import format_error_message


class UserGroups(str, Enum):
    Admin = "admin"
    Staff = "moderator"


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(
                format_error_message("exception", "User must have an email")
            )

        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(
                format_error_message("exception", "User must have an email")
            )
        if not password:
            raise ValueError(
                format_error_message("exception", "User must have a password")
            )

        user = self.model(email=self.normalize_email(email))
        user.username = email
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        group, created = Group.objects.get_or_create(name=UserGroups.Admin)
        group.user_set.add(user)

        print("Created superuser")
        print(user)
        print(group)

        return user



class User(AbstractUser, BaseModel):
    objects = CustomUserManager()

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    grade = models.IntegerField(blank=True, null=True)
    grade_letter = models.CharField(max_length=1, blank=True)
    major1 = models.CharField(max_length=254, blank=True)
    major2 = models.CharField(max_length=255, blank=True)
    standard = models.BooleanField(default=False)
    group = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "grade", "grade_letter"]

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
