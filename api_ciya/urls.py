"""
URL configuration for api_ciya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/public/', include('apps.public.src.api.urls')),
    path('api/laboratory/', include('apps.laboratory.src.api.urls')),
    path('api/investigation/', include('apps.investigacion.src.api.urls')),
    path('api/academic/', include('apps.academic.src.api.urls')),
    path('api/bonding/', include('apps.bonding.src.api.urls'))
]
