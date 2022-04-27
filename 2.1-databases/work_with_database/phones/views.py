from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get('sort')
    template = 'catalog.html'
    if sort_param == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort_param == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort_param == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {
        'phone': phone_object
    }
    return render(request, template, context)
