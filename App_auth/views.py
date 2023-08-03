from rest_framework import generics

from App_tax_payer.models import TaxPayer
from .jwt_checker.decoder import get_user_id_from_jwt
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user_id = get_user_id_from_jwt(response.data['access'])
            try:
                tax_payer = TaxPayer.objects.get(user=user_id)
                is_tax_payer = True
            except TaxPayer.DoesNotExist:
                is_tax_payer = False

            data = response.data
            data['is_tax_payer'] = is_tax_payer
            return Response(data)

        return response
