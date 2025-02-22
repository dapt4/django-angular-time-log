from rest_framework import serializers

from timelog.models import CheckIn


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['user', 'date', 'start', 'end']
