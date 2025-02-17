from rest_framework import serializers

from api.models import Vehicle

from django.contrib.auth.models import User

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:

        model=Vehicle

        fields="__all__"

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["username","email","password"]

    def create(self,validated_data):

        return User.objects.create_user(**validated_data) 
        