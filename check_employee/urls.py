from django.urls import path,include
from rest_framework.routers import DefaultRouter

from.views import DepartmentViewSet,PositionsViewSet,EmployeeViewSet


router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('positions', PositionsViewSet)
router.register('employee', EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls)),

]




