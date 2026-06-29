from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ("student","Student"),
        ("developer","Developer"),
        ("professional","Professional"),
    )

    EXPERIENCE_CHOICES = (
        ("beginner","Beginner"),
        ("junior","Junior"),
        ("mid_level","Mid_level"),
        ("senior","Senior"),
    )

    SUBSCRIPTION_CHOICES = (
        ("free","Free"),
        ("premium","Premium"),
    )

    full_name = models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    experience_level =models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="beginner"
    )

    subscription_plan = models.CharField(
        max_length=20,
        choices=SUBSCRIPTION_CHOICES,
        default="free"
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username