from django.conf.urls import patterns, include, url
from django.contrib import admin
from usermanagement import urls
from usermanagement.views import home
from RideSharing import urls
from RideSharing.views import rideSubmission
from django.conf import settings
from RideSharing.views import poll


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'itripi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home),
    url(r'^home/$',home),
    # url(r'^profile/$',include('usermanagement.urls')),
    url(r'^usermanagement/',include('usermanagement.urls')),
    url(r'^ridesharing/',include('RideSharing.urls')),

    url(r'^poll/',poll),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    )



# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )