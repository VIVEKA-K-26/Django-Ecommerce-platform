from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product,Category

def product_list(request):
    """
    Displays all products with dynamic pricing based on visit count
    """
    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits

    products = Product.objects.select_related('category').all()
    categories=Category.objects.all()

    # Apply dynamic pricing (do NOT save to DB)
    for product in products:
        if visits > 5:
            product.display_price = round(product.price * 0.95, 2)  # 5% discount
        else:
            product.display_price = product.price

    context = {
        'products': products,
        'visits': visits,
        'categories':categories
    }

    return render(request, 'product_list.html', context)


def product_detail(request, product_id):
    """
    Shows single product details
    """
    product = get_object_or_404(Product, id=product_id)

    visits = request.session.get('visits', 0)
    if visits > 5:
        product.display_price = round(product.price * 0.95, 2)
    else:
        product.display_price = product.price

    return render(request, 'product_detail.html', {
        'product': product
    })


def search(request):
    """
    Search by name, category, price range
    """
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category_id=request.GET.get('category')

    products = Product.objects.select_related('category').all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )

    if category_id:
        products = products.filter(category__id=category_id)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    # Dynamic pricing also applied here
    visits = request.session.get('visits', 0)
    for product in products:
        if visits > 5:
            product.display_price = round(product.price * 0.95, 2)
        else:
            product.display_price = product.price

    categories=Category.objects.all()

    context = {
        'products': products,
        'query': query,
        'categories':categories,
        'selected_category':category_id
    }

    return render(request, 'search.html', context)
