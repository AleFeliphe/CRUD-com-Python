from django.shortcuts import render, redirect
from app.forms import ProductForm
from app.models import Produtos
from django.core.paginator import Paginator
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produtos.objects.filter(produto__icontains=search)
    # if search:
    #     data['db'] = Produtos.objects.filter(id__icontains=search)
    else:
        data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ProductForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form']= ProductForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db']= Produtos.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

