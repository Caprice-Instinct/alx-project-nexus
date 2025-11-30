from django.urls import path
from .views import AdminOnlyView, RegularUserView

urlpatterns = [
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('regular-user/', RegularUserView.as_view(), name='regular-user'),
]
