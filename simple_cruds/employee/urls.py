from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = router.urls
