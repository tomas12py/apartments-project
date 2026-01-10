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

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from app_aparments.api.healthcheck.views import Healthcheck
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/clearcache/',include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh-token/",TokenRefreshView.as_view()),  
    path("blacklisting-token/",TokenBlacklistView.as_view()),
    path("api/",include("app_aparments.api.user.urls")),
    path("api/",include("app_aparments.api.aparment.urls")),
    path("api/schema", SpectacularAPIView.as_view(), name='schema'),    
    path("api/schema/swagger-ui/",
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
    path("api/schema/redoc/",
         SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
    path('api/health/',Healthcheck.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

print(settings.STATIC_ROOT)