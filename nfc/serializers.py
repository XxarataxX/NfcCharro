from rest_framework import serializers
from .models import Purchase, PurchaseItem, PurchaseLog, nfc

class nfcSerializer(serializers.ModelSerializer):
    class Meta:
        model = nfc
        fields = '__all__'
class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"  # Include all fields of the model

class PurchaseSerializer(serializers.ModelSerializer):
    item = PurchaseItemSerializer()  # Include the nested serializer for `item`

    class Meta:
        model = Purchase
        fields = "__all__"

    def create(self, validated_data):
        # Extract the nested `item` data
        item_data = validated_data.pop('item')

        # Create the `PurchaseItem` object
        item = PurchaseItem.objects.create(**item_data)

        # Create the `Purchase` object
        purchase = Purchase.objects.create(item=item, **validated_data)

        return purchase

class PurchaseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLog
        fields = "__all__"