from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields ='__all__'
		ordering = ['order_num']

class TodoOrder(serializers.Serializer):
    order = serializers.ListField(child=serializers.IntegerField())