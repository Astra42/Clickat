from rest_framework import serializers
from .models import Core, Boost
class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = ['coins', 'click_power']

class BoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boost
        fields = '__all__'