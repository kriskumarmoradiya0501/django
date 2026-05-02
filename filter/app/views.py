from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Product

from .forms import ProductForm


from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import CategorySerializer


# PRODUCT LIST + FILTER
def product_list(request):

    category_id = request.GET.get('category')

    if category_id:

        products = Product.objects.filter(category_id=category_id)

    else:

        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories
    })


# ADD PRODUCT
def add_product(request):

    form = ProductForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('product_list')

    return render(request, 'add_product.html', {
        'form': form
    })


# PRODUCT DETAIL
def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    return render(request, 'product_detail.html', {
        'product': product
    })


# API LIST CATEGORY
@api_view(['GET'])
def category_list(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


# API CREATE CATEGORY
@api_view(['POST'])
def create_category(request):

    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)


# API SINGLE CATEGORY
@api_view(['GET'])
def category_detail(request, category_id):

    category = Category.objects.get(id=category_id)

    serializer = CategorySerializer(category)

    return Response(serializer.data)


# API UPDATE CATEGORY
@api_view(['PUT'])
def update_category(request, category_id):

    category = Category.objects.get(id=category_id)

    serializer = CategorySerializer(category, data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)