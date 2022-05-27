from django.test import TestCase

from .models import (Produto, Pedido)


class ProdutoPedidoTestCase(TestCase):

    def test_stock_disponivel(self):
        agua = Produto(
            nome="agua",
            valor_unitario=2.0,
            quantidade=3
        )
        agua.save()

        self.assertEqual(agua.get_situacao_display(), 'Disponível')
        self.assertEqual(agua.quantidade, 3)
        self.assertEqual(agua.valor_unitario, 2)

    def test_stock_indisponivel(self):
        agua = Produto(
            nome="agua",
            valor_unitario=2.0,
            quantidade=0
        )
        agua.save()

        self.assertEqual(agua.get_situacao_display(), 'Indisponível')
        self.assertEqual(agua.quantidade, 0)
        self.assertEqual(agua.valor_unitario, 2)


class PedidoTestCase(TestCase):

    def test_order_with_stock(self):
        agua = Produto(
            nome="agua",
            valor_unitario=2.0,
            quantidade=3
        )
        agua.save()

        pedido = Pedido.objects.create(
            produto=agua,
            quantidade=3,
            valor_unitario=2,
            solicitante="José da Silva",
            solicitante_endereco="Avenida São João",
            despachante="Maria de Souza"
        )

        self.assertEqual(pedido.get_situacao_display(), 'Pendente de Envio')

        agua.refresh_from_db()

        self.assertEqual(agua.quantidade, 0)
        self.assertEqual(agua.get_situacao_display(), 'Indisponível')

    def test_order_without_stock(self):
        agua = Produto(
            nome="agua",
            valor_unitario=2.0,
            quantidade=0
        )
        agua.save()

        self.assertEqual(agua.quantidade, 0)
        self.assertEqual(agua.get_situacao_display(), 'Indisponível')

        pedido = Pedido(
            produto=agua,
            quantidade=3,
            valor_unitario=2,
            solicitante="José da Silva",
            solicitante_endereco="Avenida São João",
            despachante="Maria de Souza"
        )

        with self.assertRaises(Exception) as context:
            pedido.save()
            self.assertTrue('Este produto não possui o estoque necessário para atender ao pedido.' in context.exception)
