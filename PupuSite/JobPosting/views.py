from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hi Milky")

def current_datetime(request):
    now = datetime.datetime.now()
    html ="<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

