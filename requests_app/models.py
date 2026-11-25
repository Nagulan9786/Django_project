from django.db import models
from django.contrib.auth.models import User


class AccessRequest(models.Model):
    STATUS = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def approve(self):
        self.status = "APPROVED"
        self.save()

    def reject(self):
        self.status = "REJECTED"
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.resource} ({self.status})"