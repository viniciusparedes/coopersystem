from django.db import models
from .const import *


class Produto(models.Model):
    nome = models.CharField(max_length=124, null=False, blank=False)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    quantidade = models.IntegerField()
    situacao = models.SmallIntegerField(choices=SITUACOES_PRODUTO)

    def get_previous_balance(self):
        try:
            produto = Produto.objects.get(pk=self.pk)
            return produto.quantidade
        except Exception as _:
            return 0

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.quantidade += self.get_previous_balance()
        self.situacao = 0 if self.quantidade < 1 else 1
        super(self).save(force_insert, force_update, using, update_fields)


class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='pedidos')
    quantidade = models.IntegerField(null=False, blank=False)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    data = models.DateTimeField(auto_now_add=True)
    solicitante = models.CharField(max_length=124, null=False, blank=False)
    solicitante_endereco = models.CharField(max_length=360)
    despachante = models.CharField(max_length=124, null=False, blank=False)
    situacao = models.SmallIntegerField(choices=SITUACOES_PEDIDO)

    @property
    def has_stock(self):
        return self.produto.quantidade >= self.quantidade

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.has_stock:
            raise Exception("Este produto não possui o estoque necessário para atender ao pedido.")
        super(self).save(force_insert, force_update, using, update_fields)
