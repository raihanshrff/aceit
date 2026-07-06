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

    score = models.IntegerField(
        null = True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# question model 
class Question(models.Model):
    interview = models.ForeignKey(
        Interview,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_number = models.IntegerField()

    question_text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Question {self.question_number} - {self.interview.user.username}"
    
# Answer model
class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    answer_text = models.TextField()
    audio_url = models.URLField(
        blank = True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"Answer to Question {self.question.question_number}"
