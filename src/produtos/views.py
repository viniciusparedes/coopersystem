from rest_framework import (viewsets, permissions)
from .serializers import *


class ProdutoViewSet(viewsets.ModelViewSet):
	queryset = Produto.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = ProdutoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
	queryset = Pedido.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PedidoSerializer
