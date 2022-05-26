import django_filters
from django.db import models

from produtos.const import SITUACOES_PRODUTO
from produtos.models import (Produto, Pedido)


class ProdutoFilter(django_filters.FilterSet):
	situacao = django_filters.ChoiceFilter(choices=SITUACOES_PRODUTO)

	class Meta:
		model = Produto
		fields = {
			'id': ['exact'],
			'nome': ['icontains'],
			'valor_unitario': ['exact', 'gt', 'gte', 'lt', 'lte'],
			'quantidade': ['exact', 'gt', 'gte', 'lt', 'lte'],
		}


class PedidoFilter(django_filters.FilterSet):
	produto = django_filters.CharFilter(field_name='produto__nome', lookup_expr='icontains')
	situacao = django_filters.CharFilter(field_name='get_situacao_display', lookup_expr='icontains')

	class Meta:
		model = Pedido
		fields = {
			'id': ['exact'],
			'quantidade': ['exact', 'lt', 'lte', 'gt', 'gte'],
			'valor_unitario': ['exact', 'lt', 'lte', 'gt', 'gte'],
			'data': ['exact', 'lt', 'lte', 'gt', 'gte'],
			'solicitante': ['icontains'],
			'solicitante_endereco': ['icontains'],
			'despachante': ['icontains']
		}
