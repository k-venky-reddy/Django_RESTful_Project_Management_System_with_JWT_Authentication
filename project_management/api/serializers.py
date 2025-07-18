from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project
# Converts Django Models To JSON For API Responces
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
# Project Serializer has user_ids for assigning users 
class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    user_ids = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, write_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'client', 'users', 'user_ids', 'start_date', 'end_date']

    def create(self, validated_data):
        user_ids = validated_data.pop('user_ids')
        project = Project.objects.create(**validated_data)
        project.users.set(user_ids)
        return project

    def update(self, instance, validated_data):
        user_ids = validated_data.pop('user_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if user_ids is not None:
            instance.users.set(user_ids)
        return instance
