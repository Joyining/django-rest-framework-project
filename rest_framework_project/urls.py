from django.contrib import admin
from django.urls import path, include
from .views import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', User.as_view(), name='user'),
]
