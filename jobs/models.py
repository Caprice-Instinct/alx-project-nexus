
from django.db import models
from categories.models import Category
from users.models import User

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	company = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title} at {self.company}"
