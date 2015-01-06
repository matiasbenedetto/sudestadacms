from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sudestada.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^redactor/', include('redactor.urls')),

    url(r'^$', 'revista.views.index', name='index'),

    url(r'^articulo/(?P<id_articulo>\d+)/(?P<slug>\w+)/$', 'revista.views.articulo', name='articulo'),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))