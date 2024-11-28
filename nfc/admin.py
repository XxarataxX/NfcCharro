from django.contrib import admin
from .models import Purchase, PurchaseItem, PurchaseLog, nfc

# Registramos el modelo MyModel en el admin
admin.site.register(nfc)
admin.site.register(PurchaseItem)
admin.site.register(Purchase)
admin.site.register(PurchaseLog)