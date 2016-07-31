from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset

from django.template import loader, Context
from django.template.loader import get_template
import datetime
from django.views.decorators.csrf import csrf_exempt
from usermanagement.models import UserNotifications, UserProfile, Messages
# import django.db.models.query.RawQuerySet
from django.template.context import RequestContext

from RideSharing.models import newRide
from usermanagement.forms import ImageUploadForm
from django.db.models import Q

# class LastMessage():

class conversation():
	def __init__(self):
		