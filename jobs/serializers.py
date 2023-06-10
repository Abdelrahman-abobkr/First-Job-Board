from .models import Job
from rest_framework import serializers



class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'