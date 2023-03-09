from rest_framework import serializers

from .models import workerModel

class jugueteSerializer(serializers.ModelSerializer):
    class Meta:
       model = workerModel
       fields = '__all__' 