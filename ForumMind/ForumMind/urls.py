"""ForumMind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('visualiser/', include('visualiser.urls')),
    path('api/', include('api.urls')),
    #redirect the home or weird links to visualiser file upload page.
    re_path(r'^.*$', RedirectView.as_view(url='/visualiser/', permanent=False)),
]
