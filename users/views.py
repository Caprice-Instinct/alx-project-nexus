from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsAdmin, IsRegularUser

class AdminOnlyView(APIView):
	permission_classes = [IsAdmin]
	def get(self, request):
		return Response({"message": "Hello, admin!"})

class RegularUserView(APIView):
	permission_classes = [IsRegularUser]
	def get(self, request):
		return Response({"message": "Hello, regular user!"})
from django.shortcuts import render

# Create your views here.
