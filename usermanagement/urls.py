from django.conf.urls import patterns, include, url
from django.contrib import admin
from usermanagement import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'itripi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$',views.user_login),
    url(r'^logout/',views.user_logout),
    url(r'^newaccount/$',views.newUser),
    url(r'^userexists/$',views.userNameAvailable),
    url(r'^profile/$',views.userProfile),
   
 

    url(r'^userloginstatus/$',views.user_login_status),
    url(r'^profilepostal/$',views.userPostal),
    url(r'^workprofile/$',views.workProfile),
    url(r'^mailbox/$',views.mailbox),
    url(r'^messages/(?P<cus_url>\w+)/$',views.messages),
    url(r'^rideapproval/(?P<cus_url>\w+)/$',views.rideApproval),
    url(r'^imageupload/$',views.imageuploader),
    url(r'^transportimageuploader/$',views.transportadder)

    # url(r'^usermanagement$/',include(usermanagement.urls))
)
