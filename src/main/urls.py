# Django specific
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', lambda request: HttpResponse('Hello World')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)