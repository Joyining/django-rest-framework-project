from django.contrib import admin
from django.urls import path, include
from .views import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', Product.as_view(), name='product'),
]
