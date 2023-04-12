from django.contrib import admin
from django.urls import path, include
from .views import ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', ProductView.as_view(), name='product'),
]
