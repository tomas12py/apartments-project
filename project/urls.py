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
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('admin/clearcache/',include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path("api/v1/login/", TokenObtainPairView.as_view()),
    path("api/v1/tokens/refresh/",TokenRefreshView.as_view()),  
    path("api/v1/blacklist-token/",TokenBlacklistView.as_view()),
    path("api/v1/",include("app_aparments.api.user.urls")),
    path("api/v1/",include("app_aparments.api.aparment.urls")),
    path("api/schema", SpectacularAPIView.as_view(), name='schema'),    
    path("api/v1/schema/swagger-ui/",
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
    path("api/v1/schema/redoc/",
         SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
    path('api/v1/health/',Healthcheck.as_view()) 

]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
