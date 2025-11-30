
from django.db import models
from users.models import User
from jobs.models import Job

class Application(models.Model):
	STATUS_CHOICES = (
		('pending', 'Pending'),
		('reviewed', 'Reviewed'),
		('accepted', 'Accepted'),
		('rejected', 'Rejected'),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
	job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
	resume = models.FileField(upload_to='resumes/')
	cover_letter = models.TextField(blank=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
	applied_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.job.title} ({self.status})"
