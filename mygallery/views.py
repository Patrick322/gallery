from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.
def mygallery_today(request):
    date = dt.date.today()
    images=Images.objects.all()
    return render(request,'welcome.html',{'date': date,"images":images})



def past_days_mygallery(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.days_news(date)
    return render(request, 'my-gallery/past-gallery.html', {"date":date,"mygallery":mygallery})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_Image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'my-gallery/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my-gallery/search.html',{"message":message}) 

def image(request,article_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"my-gallery/image.html", {"image":image})

def welcome(request):
    images = Image.objects.all()
    
    return render(request,'welcome.html',{"images":images})


def mygallery_of_day(request):

    return render(request,"today-gallery.html")   
