from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    tasks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    executor = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model=UserProfile
        fields = ['id', 'username', 'email', 'balance', 'password', 'tasks', 'executor']

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user