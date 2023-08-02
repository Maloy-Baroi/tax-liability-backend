from django.urls import path

from App_tax_inspector.views import WarningLetterListCreateView, WarningLetterRetrieveUpdateDestroyView

urlpatterns = [
    path('warning-letters/', WarningLetterListCreateView.as_view(), name='warning-letter-list-create'),
    path('warning-letters/<int:pk>/', WarningLetterRetrieveUpdateDestroyView.as_view(),
         name='warning-letter-retrieve-update-destroy'),
]
