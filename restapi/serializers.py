from django.contrib.auth.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from rest_framework import serializers
from guardian.shortcuts import assign_perm
from restapi.models import *
from rest_framework.validators import *
#email verification
import hashlib, random
#time
from datetime import *
from django.utils import timezone
#import pytz

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user',)

class UserSerializer(serializers.ModelSerializer):
    #groups = GroupSerializer(many=True, required=False)
    profile = ProfileSerializer(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'email', 'password', 'first_name', 'last_name', 'profile')

    def create(self, validated_data):
        
        #grab validated data
        em = validated_data.pop('email')
        pw = validated_data.pop('password')
        fn = validated_data.pop('first_name')
        ln = validated_data.pop('last_name')
        #group_data = validated_data.pop('groups')
        profile_data = validated_data.pop('profile')

        #create new user
        user = User.objects.create_user(username=em, email=em, password=pw)
        user.first_name = fn
        user.last_name = ln
        user.save()

        #assign groups to user
        #for group in group_data:
        #    g = Group.objects.get(name = group['name'])
        #    g.user_set.add(user)

        #link new profile to user
        #if (profile_data is not None):
        #    Profile.objects.create(user=user, **profile_data)
        #else:
        Profile.objects.create(user=user)

        return user

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='user-detail',
    )

    class Meta:
        model = Challenge
        fields = '__all__'

    def create(self, validated_data):

        usr = self.context['request'].user
        challenge = Challenge.objects.create(user = usr,**validated_data)

        # assign_perm('view_school', usr, school)
        # assign_perm('change_school', usr, school)
        # assign_perm('delete_school', usr, school)

        return challenge
