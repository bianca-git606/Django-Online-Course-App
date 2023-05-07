from django.urls import path, include
from adminsite import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='course/<int:course_id>/enroll/', view=views.EnrollView.as_view(), name='enroll' ),
    path(route='course/<int:course_id>/', view=views.CourseDetailsView.as_view(), name='course_details'),
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


