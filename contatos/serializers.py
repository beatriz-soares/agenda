from django.contrib.auth.models import User, Group
from rest_framework import serializers
from contatos.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
