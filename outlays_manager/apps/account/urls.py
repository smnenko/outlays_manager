from django.urls import path

from account import views


urlpatterns = [
    path('', views.AccountAPIView.as_view(), name='account_retrieve')
]
