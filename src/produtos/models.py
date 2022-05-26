from django.db import models
from .const import SITUACOES


class Produto(models.Model):
    nome = models.CharField(max_length=124, null=False, blank=False)
    valor_unitário = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    quantidade = models.IntegerField()
    situacao = models.SmallIntegerField(choices=SITUACOES)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.situacao = 0 if self.quantidade < 1 else 1
        super(self).save(force_insert, force_update, using, update_fields)
