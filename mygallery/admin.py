from django.contrib import admin
from .models import Image,Article,tags

admin.site.register(Image)
admin.site.register(Article)
admin.site.register(tags)