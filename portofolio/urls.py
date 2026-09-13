"""
URL configuration for myportofolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
<<<<<<< Updated upstream
from django.urls import path

from portofolio.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
=======
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from mdeditor import views as mdeditor_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
<<<<<<< Updated upstream
    path("mdeditor/", include("mdeditor.urls")),
=======
    path('mdeditor/uploads/', mdeditor_views.upload_image, name='mdeditor_upload_image'),
>>>>>>> Stashed changes
>>>>>>> Stashed changes
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
