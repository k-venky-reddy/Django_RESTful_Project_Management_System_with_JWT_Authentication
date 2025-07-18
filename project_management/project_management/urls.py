from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Main Routing Files
urlpatterns = [
    path('admin/', admin.site.urls), # Register Admin Portal
    path('api/', include('api.urls')),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Get Tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh Token
]
