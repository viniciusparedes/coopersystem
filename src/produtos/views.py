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
	"""
	retrieve:
		Consulta uma instância de um Produto.
	list:
		Exibe todos os produtos.
	create:
		Cadastra um Produto.
	delete:
		Remove um produto existente.
	partial_update:
		Atualiza um ou mais atributos de um Produto.
	update:
		Atualiza um Produto.
	"""
	queryset = Produto.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = ProdutoSerializer
	filter_class = ProdutoFilter


class PedidoViewSet(viewsets.ModelViewSet):
	"""
		retrieve:
			Consulta uma instância de um Pedido.
		list:
			Exibe todos os pedidos.
		create:
			Cria um Pedido.
		delete:
			Remove um Pedido.
		partial_update:
			Atualiza um ou mais atributos de um Pedido.
		update:
			Atualiza um Pedido.
		"""
	queryset = Pedido.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PedidoSerializer
	filter_class = PedidoFilter
