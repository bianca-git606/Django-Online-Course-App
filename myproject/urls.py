"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from adminsite import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='course/<int:course_id>/enroll/', view=views.enroll, name='enroll' ),
    path(route='course/<int:course_id>/', view=views.course_details, name='course_details'),
    path(route='', view=views.popular_course_list, name='popular_course_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


