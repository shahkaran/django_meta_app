from django.conf.urls import patterns, include, url
from meta.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^$',home),
    url(r'^getinfo/$', getInfo),
    url(r'^saveinfo/$', saveInfo),  
   url(r'^saved/$', saved),  

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

)
