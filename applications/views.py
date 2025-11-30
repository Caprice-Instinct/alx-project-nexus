from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer
from users.permissions import IsRegularUser, IsAdmin

class ApplicationViewSet(viewsets.ModelViewSet):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = [IsAuthenticated]

	def get_permissions(self):
		if self.action in ['destroy']:
			return [IsAdmin()]
		return [IsAuthenticated()]
from django.shortcuts import render

# Create your views here.
