

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('share2go.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-refresh/', refresh_jwt_token),
    path('token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]

