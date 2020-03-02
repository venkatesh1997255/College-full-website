from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'College'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'student_registration/', views.student_registration, name='registration'),
    url(r'application/', views.application, name='application'),
    url(r'login/', views.user_login, name='user_login'),
    url(r'student_profile/',views.student_profile,name='student_profile'),
    url(r'staff_registration/', views.staff_registration, name='staff_registration'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
