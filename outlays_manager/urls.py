from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('accounts/', include('account.urls')),
    path('categories/', include('category.urls')),
    path('transactions/', include('transaction.urls')),
]
