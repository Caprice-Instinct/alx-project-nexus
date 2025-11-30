
from django.db import models
from categories.models import Category
from users.models import User

class Job(models.Model):
	title = models.CharField(max_length=255, db_index=True)
	description = models.TextField()
	company = models.CharField(max_length=255)
	location = models.CharField(max_length=255, db_index=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs', db_index=True)
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		indexes = [
			models.Index(fields=['title']),
			models.Index(fields=['location']),
			models.Index(fields=['category']),
		]

	def __str__(self):
		return f"{self.title} at {self.company}"
