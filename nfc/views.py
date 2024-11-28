from rest_framework import viewsets
from .models import Purchase, PurchaseItem, PurchaseLog, nfc
from .serializers import PurchaseItemSerializer, PurchaseLogSerializer, PurchaseSerializer, nfcSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework import generics

class nfcViewSet(viewsets.ModelViewSet):
    queryset = nfc.objects.all()
    serializer_class = nfcSerializer

class ActualizarDineroView(APIView):
    @transaction.atomic
    def post(self, request, pk, tipo, cantidad):
        try:
            # Buscar el objeto NFC por su ID (pk)
            #nfc_obj = nfc.objects.get(pk=pk)
            nfc_obj1 = nfc.objects.get(pk=1)  # Buscar el objeto con ID 1
            nfc_obj2 = nfc.objects.get(pk=2)  # Buscar el objeto con ID 2
        except nfc.DoesNotExist:
            return Response({'error': 'Objeto NFC no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Ajustar la cantidad según el tipo para todos los objetos
        if tipo == 'p':  # Si es positivo
            #nfc_obj.dinero += cantidad
            nfc_obj1.dinero += cantidad
            nfc_obj2.dinero += cantidad
        elif tipo == 'n':  # Si es negativo
            #nfc_obj.dinero -= cantidad
            nfc_obj1.dinero -= cantidad
            nfc_obj2.dinero -= cantidad
        else:
            return Response({'error': 'Tipo inválido, use "p" para positivo o "n" para negativo'}, status=status.HTTP_400_BAD_REQUEST)

        # Guardar los cambios en la base de datos
        #nfc_obj.save()
        nfc_obj1.save()
        nfc_obj2.save()

        # Responder con los nuevos datos de los objetos actualizados
        return Response({
            'dinero_actualizado_id1': nfc_obj1.dinero,
            'dinero_actualizado_id2': nfc_obj2.dinero
        }, status=status.HTTP_200_OK)

class PurchaseItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer


class PurchaseItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer


class PurchaseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
class PurchaseLogListCreateAPIView(generics.ListCreateAPIView):
    """
    API View for listing all purchase logs or creating a new one.
    """
    queryset = PurchaseLog.objects.all()
    serializer_class = PurchaseLogSerializer


class PurchaseLogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View for retrieving, updating, or deleting a specific purchase log.
    """
    queryset = PurchaseLog.objects.all()
    serializer_class = PurchaseLogSerializer