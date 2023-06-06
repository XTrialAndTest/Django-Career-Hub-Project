from django.db import models
from users.models import Employer


# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=200,
    )
    slug = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Job(models.Model):
    positions = (
        ("junior", "junior"),
        ("intermediate", "intermediate"),
        ("senior", "senior"),
        ("expart", "expart"),
    )
    contaract_types = (
        ("remote", "remote"),
        ("part-time", "part-time"),
        ("full-time", "full-time"),
        ("negotiations", "negotiations"),
    )

    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="jobs"
    )
    job_category = models.ForeignKey(
        Category,
        related_name="jobs",
        on_delete=models.CASCADE,
    )
    job_title = models.CharField(
        max_length=200,
    )
    slug = models.CharField(max_length=200, null=True)
    job_location = models.CharField(max_length=200)
    contract_type = models.CharField(max_length=200, choices=contaract_types)
    position = models.CharField(max_length=200, choices=positions)
    job_description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.job_title
