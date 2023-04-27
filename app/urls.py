from .serializers import *
from .views import *
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
router = routers.DefaultRouter()
router.register(r"Teacher/",TeacherViewSet)
router.register(r"AddStudent/",AddStudentViewSet)
router.register(r"Registration/",RegistrationViewSet)
router.register(r"Course/",CourseViewSet)

urlpatterns = [
    path('',include(router.urls))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
