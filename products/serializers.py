from rest_framework import serializers
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "image"]



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    

    def validate(self, attrs):
        # Get the default validated data (access and refresh tokens)
        data = super().validate(attrs)

        # Include 'is_staff' or 'is_admin' in the response
        user = self.user
        data["isAdmin"] = user.is_staff  # You can also use user.is_superuser if needed

        return data
