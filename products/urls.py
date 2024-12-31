from django.urls import path
from .views import product_list, product_detail, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("access/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", product_list, name="product-list"),
    path("<int:pk>/", product_detail, name="product-detail"),
]
