from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
# router.register('students', viewset=views.StudentViewSet, basename='students')

urlpatterns = router.urls
# urlpatterns = [
#     path('', include(router.urls)),
# ]
