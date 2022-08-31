from rest_framework import serializers
from apis import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'done',
        )
        model = models.Todo

class TodoPATCHSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'done',
        )
        model = models.Todo