import time
from django.http import StreamingHttpResponse, HttpResponse

__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, url, include

# App specific
from fabric_interface.formulae.views import (
    FormulaCreateView, FormulaUpdateView
)


from django.views.decorators.http import condition

@condition(etag_func=None)
def stream_response(request):
    resp = HttpResponse(stream_response_generator())
    return resp


def stream_response_generator():
    yield "<html><body>\n"
    for x in range(1,11):
        yield "<div>%s</div>\n" % x
        yield " " * 1024  # Encourage browser to render incrementally
        time.sleep(1)
    yield "</body></html>\n"


urlpatterns = patterns('',
   url(r'^$', stream_response),
   url(r'create/$', FormulaCreateView.as_view(), name='test'),
   url(r'(?P<pk>\d+)/update/$', FormulaUpdateView.as_view(), name='formula_update'),
)