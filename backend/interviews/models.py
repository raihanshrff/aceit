from django.db import models
from accounts.models import User

# Create your models here.
class Interview(models.Model):
    ROLE_CHOICES = (
        ("backend", "Backend Developer"),
        ("python","Python Developer"),
        ("fullstack","Full Stack Developer"),
        ("frontend","Frontend Developer"),
    )

    DIFFICULTY_CHOICES = (
        ("beginner","Beginner"),
        ("intermediate","Intermediate"),
        ("advanced","Advanced"),
    )

    STATUS_CHOICES = (
        ("active","Active"),
        ("pending","Pending"),
        ("completed","Completed"),
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="interviews",
    )

    role = models.CharField(
        max_length=30,
        choices = ROLE_CHOICES,
    )

    difficulty = models.CharField(
        max_length=30,
        choices=DIFFICULTY_CHOICES,
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="pending",
    )

    score = models.CharField(
        null = True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"