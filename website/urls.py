
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rolls/',include('rolls.urls')),
    url(r'^College/',include('College.urls')),
]

