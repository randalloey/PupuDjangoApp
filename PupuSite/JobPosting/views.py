from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, Http404
import datetime

def current_datetime(request):
    now = datetime.datetime.utcnow()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request, time_offset):
    try:
        offset = int (time_offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return  HttpResponse(html)