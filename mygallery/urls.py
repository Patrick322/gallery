from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'Welcome'),
    url('^today/$',views.mygallery_of_day='mygalleryToday')
]