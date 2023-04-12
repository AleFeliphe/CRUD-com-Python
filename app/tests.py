from django.test import TestCase
from .models import Produtos

class ProdutosTestCase(TestCase):
    def setUp(self):
        self.produto1 = Produtos.objects.create(produto="Produto1", quantidade="10", preco="10.99")
        self.produto2 = Produtos.objects.create(produto="Produto2", quantidade="20", preco="20.99")

    def test_produto_criado(self):
        produto = Produtos.objects.get(produto="Produto1")
        self.assertEqual(produto.quantidade, "10")
        self.assertEqual(produto.preco, "10.99")

    def test_produto_editado(self):
        produto = Produtos.objects.get(produto="Produto1")
        produto.preco = "15.99"
        produto.save()
        produto_atualizado = Produtos.objects.get(produto="Produto1")
        self.assertEqual(produto_atualizado.preco, "15.99")

    def test_produto_removido(self):
        produto = Produtos.objects.get(produto="Produto2")
        produto.delete()
        with self.assertRaises(Produtos.DoesNotExist):
            Produtos.objects.get(produto="Produto2")

    def test_lista_produtos(self):
        response = self.client.get('/produtos/')
        self.assertContains(response, self.produto1.produto)
        self.assertContains(response, self.produto1.quantidade)
        self.assertContains(response, self.produto1.preco)
        self.assertContains(response, self.produto2.produto)
        self.assertContains(response, self.produto2.quantidade)
        self.assertContains(response, self.produto2.preco)

    def test_adicionar_produto(self):
        response = self.client.post('/produtos/add/', {'produto': 'Produto3', 'quantidade': '30', 'preco': '30.99'})
        produto_adicionado = Produtos.objects.get(produto="Produto3")
        self.assertEqual(produto_adicionado.quantidade, "30")
        self.assertEqual(produto_adicionado.preco, "30.99")

    def test_editar_produto(self):
        response = self.client.post(f'/produtos/edit/{self.produto1.pk}/', {'produto': 'Produto1', 'quantidade': '15', 'preco': '15.99'})
        produto_atualizado = Produtos.objects.get(pk=self.produto1.pk)
        self.assertEqual(produto_atualizado.quantidade, "15")
        self.assertEqual(produto_atualizado.preco, "15.99")

    def test_remover_produto(self):
        response = self.client.post(f'/produtos/delete/{self.produto1.pk}/')
        with self.assertRaises(Produtos.DoesNotExist):
            Produtos.objects.get(pk=self.produto1.pk)
