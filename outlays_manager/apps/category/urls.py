from rest_framework import routers

from category import views


router = routers.SimpleRouter()
router.register('', views.CategoryViewSet, basename='categories')
urlpatterns = router.urls
