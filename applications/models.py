
from users.models import User  
import uuid
from django.db import models
from jobs.models import JobPosting


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_id = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    applicant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', limit_choices_to={'role': 'applicant'})
    resume_link = models.URLField(max_length=500)  # could also use FileField 
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application by {self.applicant.username} for {self.job.title}"

    class Meta:
        indexes = [
            models.Index(fields=['job_id', 'applicant_id']),
            models.Index(fields=['status']),
        ]