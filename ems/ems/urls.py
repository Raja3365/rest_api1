
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from employee.views import EmployeeViewset
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'emp', EmployeeViewset)

schema_view = get_swagger_view(title='EMS API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger-docs/', schema_view),
]
