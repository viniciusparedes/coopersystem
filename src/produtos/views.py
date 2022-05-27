from rest_framework import (viewsets, permissions)
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import (SwaggerUIRenderer, OpenAPIRenderer)

from coopersystem.filters import (PedidoFilter, ProdutoFilter)
from .serializers import *


schema_view = get_schema_view(
	title='CooperSystem Produtos & Pedidos Manager',
	renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


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
