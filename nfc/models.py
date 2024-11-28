from django.db import models

# Create your models here.
class nfc(models.Model):  # Es recomendable usar PascalCase para los nombres de las clases
    dinero = models.IntegerField()
    idUser = models.IntegerField()
    nombre = models.CharField(max_length=30)  # Corrige 'max_lenght' a 'max_length'
    
    def __str__(self):
        return str(self.pk)  # Convierte 'self.pk' a cadena para evitar errores


class PurchaseItem(models.Model):
    product_name = models.CharField(max_length=255, help_text="Name of the product purchased.")
    product_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the individual product.")
    quantity = models.PositiveIntegerField(default=1, help_text="Quantity of the product purchased.")
    helper = models.CharField(max_length=255, help_text="Helper field to test the model.")

    class Meta:
        verbose_name = "Purchase Item"
        verbose_name_plural = "Purchase Items"

    def __str__(self):
        return f"{self.product_name} (x{self.quantity}) - ${self.product_price}"
    
class Purchase(models.Model):
    item = models.ForeignKey(PurchaseItem, on_delete=models.CASCADE, help_text="The item purchased.")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount of the purchase.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the purchase was made.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the purchase was last updated.")

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Purchase #{self.id} - ${self.total_amount}"
    
class PurchaseLog(models.Model):
    product_name = models.CharField(max_length=255, help_text="Name of the product purchased.")
    product_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the individual product.")
    quantity = models.PositiveIntegerField(default=1, help_text="Quantity of the product purchased.")
    helper = models.CharField(max_length=255, help_text="Helper field to test the model.")

    class Meta:
        verbose_name = "Purchase Log"
        verbose_name_plural = "Purchase Logs"

    def __str__(self):
        return f"{self.product_name} - ({self.quantity} pcs)"