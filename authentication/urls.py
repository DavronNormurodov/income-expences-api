from django.urls import path
from django.utils.http import parse_http_date
from .views import (RegisterView, VerifyEmail, LoginApiView,
 PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView)
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email-ferify/', VerifyEmail.as_view(), name='email-ferify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh token
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete')
]