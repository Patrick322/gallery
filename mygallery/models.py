from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)
    

    def __str__(self):
        return self.location
    class meta:
        ordering =['name']
    
    def save_editor(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =60, default='null')
    post = models.TextField(null=True)
    location = models.ManyToManyField(Location)
    pub_date = models.DateTimeField(default=None)
    image = models.ImageField(upload_to = 'image/')

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return mygallery  

    @classmethod
    def todays_mygallery(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return mygallery
    
    @classmethod
    def days_mygallery(cls,date):
        mygallery = cls.objects.filter(pub_date__date = date)
        return mygallery

    @classmethod
    def todays_mygallery(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return mygallery

    @classmethod
    def days_mygallery(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return mygallery    