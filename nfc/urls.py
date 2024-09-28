from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import nfcViewSet, ActualizarDineroView

router = DefaultRouter()
router.register(r'nfc', nfcViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('nfc/<int:pk>/actualizar/<str:tipo>/<int:cantidad>/', ActualizarDineroView.as_view(), name='actualizar_dinero'),
]