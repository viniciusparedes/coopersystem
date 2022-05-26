import django_filters

from produtos.models import (Produto, Pedido)


class ProdutoFilter(django_filters.FilterSet):
	nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')
	valor_unitario = django_filters.NumberFilter(field_name='valor_unitario', lookup_expr='exact')
	quantidade = django_filters.NumberFilter(field_name='quantidade', lookup_expr='exact')
	situacao = django_filters.CharFilter(field_name='get_situacao_display', lookup_expr='icontains')

	class Meta:
		model = Produto
		fields = ['id', 'nome', 'valor_unitario', 'quantidade', 'situacao']


class PedidoFilter(django_filters.FilterSet):
	produto = django_filters.CharFilter(field_name='produto__nome', lookup_expr='icontains')
	quantidade = django_filters.NumberFilter(field_name='quantidade', lookup_expr='exact')
	valor_unitario = django_filters.NumberFilter(field_name='valor_unitario', lookup_expr='exact')
	data = django_filters.DateTimeFilter(field_name='data')
	solicitante = django_filters.CharFilter(field_name='solicitante', lookup_expr='icontains')
	solicitante_endereco = django_filters.CharFilter(
		field_name='solicitante_endereco', lookup_expr='icontains'
	)
	despachante = django_filters.CharFilter(field_name='despachante', lookup_expr='icontains')
	situacao = django_filters.CharFilter(field_name='get_situacao_display', lookup_expr='icontains')

	class Meta:
		model = Pedido
		fields = [
			'id', 'produto', 'quantidade', 'valor_unitario', 'data', 'solicitante',
			'solicitante_endereco', 'despachante', 'situacao'
		]
