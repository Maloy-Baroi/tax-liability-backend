# urls.py
from django.urls import path
from .views import NotificationListView, UserHomeData, NotificationCountData, NotificationData

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('user-home-data/', UserHomeData.as_view(), name='user-home-data'),
    path('notification-data/', NotificationCountData.as_view(), name='notification-data'),
    path('notification-list/', NotificationData.as_view(), name='notification-list'),
]
