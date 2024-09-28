from rest_framework import serializers
from .models import nfc

class nfcSerializer(serializers.ModelSerializer):
    class Meta:
        model = nfc
        fields = '__all__'