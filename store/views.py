from django.shortcuts import render
import requests

from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    related_products = []
    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        for id in request.session['recently_viewed']:
            related_products.append(Product.objects.get(id=id))

        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 6:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True

    context = {
        'product': product,
        'related_products': related_products[:5],
    }

    return render(request, 'store/product.html', context)


def load_products(request):
    # r = requests.get('https://fakestoreapi.com/products')
    # print(r.json())
    # for p in r.json():
    #     product = Product(
    #         title = p['title'],
    #         price = p['price'],
    #         description = p['description'],
    #         image_url = p['image'])
    #     product.save()

    return render(request, 'store/index.html')

# data = {'id': 1,
#         'title': 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',
#         'price': 109.95,
#         'description': 'Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday',
#         'category': "men's clothing",
#         'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png',
#         'rating': {
#             'rate': 3.9,
#             'count': 120
#             }
#         }
