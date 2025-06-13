"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
from app_aparments.views import AparmentGeneralMethods,AparmentMethodsById,UserRegister,AparmentFiltering,AparmentPagination
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import include, path
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path("aparment",AparmentGeneralMethods.as_view()), 
    path("aparment/<id>/",AparmentMethodsById.as_view()),
    path("user/",UserRegister.as_view()),
    path("user/<id>/",UserRegister.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("api/schema",SpectacularAPIView.as_view(),name = 'schema'),
    path("api/schema/swagger-ui/",SpectacularSwaggerView.as_view(url_name = 'schema'),name = 'swagger-ui'),
    path("api/schema/redoc/",SpectacularRedocView.as_view(url_name = 'schema'),name = "redoc"),
    path("aparment/",AparmentFiltering.as_view()),
    path("aparment-pagination/",AparmentPagination.as_view())
]
