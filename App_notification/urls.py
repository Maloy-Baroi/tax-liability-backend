# urls.py
from django.urls import path
from .views import NotificationListView, WarningLetterListCreateView, WarningLetterRetrieveUpdateDestroyView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('warning-letters/', WarningLetterListCreateView.as_view(), name='warning-letter-list-create'),
    path('warning-letters/<int:pk>/', WarningLetterRetrieveUpdateDestroyView.as_view(),
         name='warning-letter-retrieve-update-destroy'),
]
