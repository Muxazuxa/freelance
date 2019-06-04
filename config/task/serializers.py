from rest_framework import serializers
from django.db import transaction
from django.db.models import F
from .models import Task
from user.models import UserProfile


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    executor = serializers.ReadOnlyField(source='executor.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'price', 'owner', 'executor']


class OrderSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    executor = serializers.CharField(read_only=True)
    price = serializers.CharField(read_only=True)
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ['owner', 'title', 'description', 'price', 'executor']

    def update(self, instance, validated_data):
        if instance.executor:
            raise serializers.ValidationError(
                'Task already has executor'
            )

        if instance.owner == validated_data['executor']:
            raise serializers.ValidationError(
                'Executor can\'t be Owner'
            )

        if instance.owner.balance < instance.price:
            raise serializers.ValidationError(
                'Owner doesn\'t have enough balance for this operation'
            )
        with transaction.atomic():
            UserProfile.objects.select_for_update().filter(pk=instance.owner.id)\
                .update(balance=F('balance') - instance.price)
            UserProfile.objects.select_for_update().filter(username=validated_data['executor'])\
                .update(balance=F('balance') + instance.price)

        Task.objects.filter(pk=instance.id).update(**validated_data)

        task = Task.objects.get(pk=instance.id)

        return task
