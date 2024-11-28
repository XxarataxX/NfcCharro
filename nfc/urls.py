from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchaseItemListCreateAPIView, PurchaseItemRetrieveUpdateDestroyAPIView, PurchaseListCreateAPIView, PurchaseLogListCreateAPIView, PurchaseLogRetrieveUpdateDestroyAPIView, PurchaseRetrieveUpdateDestroyAPIView, nfcViewSet, ActualizarDineroView

router = DefaultRouter()
router.register(r'nfc', nfcViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('nfc/<int:pk>/actualizar/<str:tipo>/<int:cantidad>/', ActualizarDineroView.as_view(), name='actualizar_dinero'),
    # PurchaseItem endpoints
    path("purchase-items/", PurchaseItemListCreateAPIView.as_view(), name="purchase-item-list-create"),
    path("purchase-items/<int:pk>/", PurchaseItemRetrieveUpdateDestroyAPIView.as_view(), name="purchase-item-detail"),

    # Purchase endpoints
    path("purchases/", PurchaseListCreateAPIView.as_view(), name="purchase-list-create"),
    path("purchases/<int:pk>/", PurchaseRetrieveUpdateDestroyAPIView.as_view(), name="purchase-detail"),

     # Endpoint for listing all purchase logs or creating a new one
    path('purchase-logs/', PurchaseLogListCreateAPIView.as_view(), name='purchase-log-list-create'),
    
    # Endpoint for retrieving, updating, or deleting a specific purchase log
    path('purchase-logs/<int:pk>/', PurchaseLogRetrieveUpdateDestroyAPIView.as_view(), name='purchase-log-detail'),

]