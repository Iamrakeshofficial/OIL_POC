from rest_framework import serializers
from django.contrib.auth.models import User
from .models import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from rest_framework import validators
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from .models import BusDetails,Contact,Route,Destination,Ticket_history,Customer,about,NewUser,Passenger
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _




class RegisterSerializer(serializers.ModelSerializer):


  # email = serializers.EmailField(
  #   required=True,
  #   validators=[UniqueValidator(queryset=User.objects.all())]
  # )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  
  class Meta:
    model = NewUser
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name','mobile_number')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True},
      'email':{'required':True},
    }
  # def validate(self, attrs):
  #   if attrs['password'] != attrs['password2']:
  #       raise serializers.ValidationError(
  #       {"password": "Password fields didn't match."})
  #   return attrs



  def validate(self,attrs):
    email=attrs.get('email','')
    if NewUser.objects.filter(email=attrs['email']).exists():
      raise serializers.ValidationError({'email':('Email is already in Use Please Take Different Email Address.')})

    if attrs['password'] != attrs['password2']:
        raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs

     

  def create(self, validated_data):
    user =NewUser.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      mobile_number=validated_data['mobile_number']
    )

    user.set_password(validated_data['password'])
    user.save()
    return user


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model =NewUser
    fields = ["user_id", "username","first_name", "last_name","email","password","mobile_number"]

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
      label="username",
      write_only=True
    )
    password = serializers.CharField(
      label="Password",
      # This will be used when the DRF browsable API is enabled
      style={'input_type': 'password'},
      trim_whitespace=False,
      write_only=True
    )

    def validate(self, attrs):
      username = attrs.get('username')
      password = attrs.get('password')
      if username and password:
        user = authenticate(request=self.context.get('request'),
                            username=username, password=password)
        print(user,"+++")
        if not user:
          msg = 'Access denied: wrong username  or password.'
          raise serializers.ValidationError(msg, code='authorization')
      else:
        msg = 'Both "username" and "password" are required.'
        raise serializers.ValidationError(msg, code='authorization')
      attrs['user'] = user
      return attrs



class BusDetailsSerializer(serializers.ModelSerializer):
  source = serializers.CharField(source="source.destination")
  destination_one = serializers.CharField(source="destination_one.destination")
  class Meta:
    model=BusDetails
    fields="__all__"

  def create(self, validated_data):
    return BusDetails.objects.create(**validated_data)

class AddBusDetailsSerializer(serializers.ModelSerializer):

  nos =serializers.IntegerField()
  class Meta:
    model=BusDetails
    fields="__all__"

  def create(self, validated_data):
    return BusDetails.objects.create(**validated_data)


class ContactSerializer(serializers.ModelSerializer):
  name=serializers.CharField()
  class Meta:
    model=Contact
    fields="__all__"

class RootSerializer(serializers.ModelSerializer):
  origin=serializers.CharField(source="origin.destination")
  destination_two = serializers.CharField(source="destination_two.destination")
  class Meta:
    model=Route
    fields= "__all__"


  def create(self, validated_data):
    print(validated_data,'-----------------')
    origin = validated_data['origin']['destination']
    print(origin)
    destination_two = validated_data['destination_two']['destination']
    date = validated_data['date']
    print(date)
    origin = Destination.objects.get(destination=origin)
    destination_two = Destination.objects.get(destination=destination_two)
    ab= Route.objects.create(origin=origin,destination_two=destination_two,date=date)
    return ab

class DestinationSerializer(serializers.ModelSerializer):
  class Meta:
    model=Destination
    fields="__all__"

class TicketHistorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Ticket_history
    fields=['name', 'bus_name',  'origin', 'destination','date', 'user']


class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model=Customer
    fields="__all__"

class PassengerSerializer(serializers.ModelSerializer):
  class Meta:
    model=Passenger
    fields="__all__"



class AboutSerializer(serializers.ModelSerializer):
  class Meta:
    model=about
    fields="__all__"


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
      user = self.context['request'].user
      if not user.check_password(value):
        raise serializers.ValidationError(
          _('Your old password was entered incorrectly. Please enter it again.')
        )
      return value

    def validate(self, data):
      if data['new_password1'] != data['new_password2']:
        raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
      password_validation.validate_password(data['new_password1'], self.context['request'].user)
      return data

    def save(self, **kwargs):
      password = self.validated_data['new_password1']
      user = self.context['request'].user
      user.set_password(password)
      user.save()
      return user