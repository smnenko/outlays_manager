from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views


urlpatterns = [
    path('signup/', views.UserCreateAPIView.as_view(), name='user_create'),
    path('<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
