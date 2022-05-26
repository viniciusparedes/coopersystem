from rest_framework import (viewsets, permissions)

from coopersystem.filters import (PedidoFilter, ProdutoFilter)
from .serializers import *


class ProdutoViewSet(viewsets.ModelViewSet):
	queryset = Produto.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = ProdutoSerializer
	filter_class = ProdutoFilter


class PedidoViewSet(viewsets.ModelViewSet):
	queryset = Pedido.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PedidoSerializer
	filter_class = PedidoFilter
