from django.shortcuts import render
import datetime

def current_datetime(request):
    now = datetime.datetime.utcnow()
    return render(request,'current_datetime.html', {'current_date': now})

def hours_ahead(request, time_offset):
    try:
        offset = int (time_offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return  HttpResponse(html)