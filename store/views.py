from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from store.models import Products 
from store.models import Category 
from store.models import Customer
from store.models import Order
from store.models import Payment

class Test(View):
    def get(self):
        return HttpResponse("Hello World")
    def store(request):
        products = Products.get_all_products()
        print(products)
        data = {}
        data['products'] = products
        return render(request, 'store.html', data)

# View for displaying all product
class ProductListView(View):
    def get(self, request):
        products = Products.get_all_products()
        print(products)
        data = {}
        data['products'] = products
        return render(request, 'index.html', data)
    
# View for displaying product details
class ProductDetailView(View):
    def get(self, request, id):
        product = Products.get_product_by_id(id)
        print(product)
        return render(request, 'productdetail.html', {'product':product})

# View for unlocking a video
# class UnlockVideoView(View):
#     def get(self, request, id):
#         product = Products.set_is_paid(id)