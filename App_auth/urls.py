from django.urls import path
from .views import CustomUserListCreateView, CustomUserRetrieveUpdateDeleteView, CustomTokenObtainPairView, UserProfileListCreateView, UserProfileUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileListCreateView.as_view(), name='user_profile'),
    path('profile/<int:pk>/', UserProfileUpdateView.as_view(), name='update_user_profile'),
]
