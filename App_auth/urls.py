# userapi/urls.py
from django.urls import path
from .views import CustomUserListCreateView, CustomUserRetrieveUpdateDeleteView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
]
