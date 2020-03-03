import datetime
from rest_framework import serializers
from smartswitchapi.models import Switchapi


class SwitchapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switchapi
        fields = ['url', 'id', 'name', 'switch0',
                  'switch1', 'switch2', 'switch3', 'phone_no']
