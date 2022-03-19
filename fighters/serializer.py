# this will convert to json data

from rest_framework import serializers
from .models import Fighters

class FightersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner_of_contrib', 'name','description', 'create_at', 'updated_at')
        model = Fighters