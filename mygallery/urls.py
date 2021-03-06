from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^today/$',views.mygallery_of_day,name='mygalleryToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_mygallery,name = 'pastmygallery'),
    url(r'^search/', views.search_results, name='search_results'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)