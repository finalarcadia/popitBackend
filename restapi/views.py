#models
from django.contrib.auth.models import *
from rest_framework.authtoken.models import Token
from restapi.models import *
#serializers
from restapi.serializers import *
#viewsets
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
#classviews
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route, api_view, authentication_classes, permission_classes
#generic classes
from rest_framework import generics
#authentication
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication
#permissions
from rest_framework import permissions
from restapi.permissions import *
#filters
from rest_framework import filters
#dates
from django.utils import timezone
import datetime
#email
from django.core.mail import send_mail
import hashlib, random
#time
from datetime import *
from django.utils import timezone
#group endpoint
from django.apps import apps

class UserViewSet(viewsets.ModelViewSet):
    #No authentication required
    authentication_classes = ()
    permission_classes = ()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('email', 'first_name', 'last_name')
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ChallengeViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated, IsCreatorCanEdit,)
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer