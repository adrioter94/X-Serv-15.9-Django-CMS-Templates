from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    url(r'^annotated/$', 'templates.views.show_all'),
    url(r'^annotated/(.*)$', 'templates.views.processCMS_Templates'),
    url(r'^(.*)', "templates.views.processCMS_Users"),
)
