from rest_framework import routers

from transaction import views


router = routers.SimpleRouter()
router.register('', views.TransactionViewSet, basename='transaction')
urlpatterns = router.urls
