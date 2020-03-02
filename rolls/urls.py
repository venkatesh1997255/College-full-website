from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'rolls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/votes$',views.vote,name='vote'),

    url('^image_upload/', views.hotel_image_view, name = 'image_upload'),
    url('^display/', views.display_hotel_images, name='display'),


    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)