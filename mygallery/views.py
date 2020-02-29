from django.http import HttpResponse

#create your views here
def welcome(request):
    return HttpResponse('Welcome to my gallery')
