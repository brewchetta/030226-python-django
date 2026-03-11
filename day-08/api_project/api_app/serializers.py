from rest_framework import serializers
from .models import MarsRoverPart


class MarsRoverPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarsRoverPart
        fields = '__all__'

class MarsRoverPartSerializerLowDetails(serializers.ModelSerializer):
    class Meta:
        model = MarsRoverPart
        # what to include when we send data
        fields = ['name', 'purpose', 'serial_number']

# {
#     "name": "Alien Catcher",
#     "purpose": "To catch little green men",
#     "serial_number": 12345
# }

from .models import Rover

class RoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rover
        fields = '__all__'