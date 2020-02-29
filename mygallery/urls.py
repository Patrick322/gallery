from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'Welcome'),
    url('^today/$',views.mygallery_of_day='mygalleryToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_mygallery,name = 'pastmygallery'),
]