from django.conf.urls import patterns, include, url
from django.contrib import admin
from RideSharing import views
urlpatterns = patterns('',
    url(r'^rideoffer/$',views.rideOffer),
    url(r'^ridesubmission/$',views.rideSubmission),
    url(r'^ridesearch/$',views.ride_search),
    url(r'^offer/$',views.offer),
    url(r'^rides/(?P<rideid>\w+)/(?P<origin>\w+)/(?P<destination>\w+)/$',views.details),
    # url(r'^rides/(?P<rideid>\w+)/$',views.details),
    # url(r'^messagehost/(?P<unique_id>[0-9]\w+)/$',views.test),
)
