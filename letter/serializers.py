from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.HyperlinkedModelSerializer):

    
    class Meta:
        model = Students
        fields = ('id', 'initials', 'location', 'letter',)
