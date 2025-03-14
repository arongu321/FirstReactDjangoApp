"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend_api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# The urlpatterns list routes URLs to views.
# The 'admin/' URL is for the Django admin interface.
# The 'backend_api/user/register/' URL is for user registration.
# The 'backend_api/token/' URL is for obtaining a JWT token.
# The 'backend_api/token/refresh/' URL is for refreshing the JWT token.
# The 'backend_api-auth/' URL includes the default authentication URLs provided by Django REST framework.
# The 'backend_api/' URL includes the URLs from the url patterns folder from backend_api app.
urlpatterns = [
    path('admin/', admin.site.urls),
    path("backend_api/user/register/", CreateUserView.as_view(), name="register"),
    path("backend_api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("backend_api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("backend_api-auth/", include("rest_framework.urls")),
    path("backend_api/", include("backend_api.urls")),
]

