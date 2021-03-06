from utils.serializers import CustomSerializer
from .models import (Produto, Pedido)


class ProdutoSerializer(CustomSerializer):
	class Meta:
		model = Produto
		fields = '__all__'
		extra_fields = ['get_situacao_display']
		read_only_fields = ['situacao']


class PedidoSerializer(CustomSerializer):
	class Meta:
		model = Pedido
		fields = '__all__'
		extra_fields = ['get_situacao_display']
		read_only_fields = ['situacao']
