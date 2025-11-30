from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer
from users.permissions import IsAdmin, IsRegularUser

class JobViewSet(viewsets.ModelViewSet):
	queryset = Job.objects.all()
	serializer_class = JobSerializer
	permission_classes = [IsAuthenticated]

	def get_permissions(self):
		if self.action in ['create', 'update', 'partial_update', 'destroy']:
			return [IsAdmin()]
		return [IsAuthenticated()]
from django.shortcuts import render

# Create your views here.
