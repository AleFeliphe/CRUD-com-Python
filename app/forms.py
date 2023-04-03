from django.forms import ModelForm
from app.models import Produtos

# Create the form class.
class ProductForm(ModelForm):
     class Meta:
         model = Produtos
         fields = ['produto', 'quantidade', 'preco']
