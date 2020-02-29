from django.http  import HttpResponse
import datetime as datetime

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my gallery')

def mygallery_of_day(request)
    date =  dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)