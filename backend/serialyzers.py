from rest_framework import serializers
from .models import Core
class CoreSerialyzer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = ['coins', 'click_power']