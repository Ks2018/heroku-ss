from django.conf.urls import include, url
from django.contrib import admin

import web.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', web.views.index, name='index'),
    url(r'^status', web.views.status, name='status'),
    url(r'^db', web.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]