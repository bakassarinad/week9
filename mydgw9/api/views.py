from django.shortcuts import render
from api.models import Product, Category
from django.http.response import HttpResponse, JsonResponse
# Create your views here.
def product_list(request):
    try:
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        return  JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({"error": "no product"})
def product_detail(request, productid):
    try:
        product = Product.objects.get(id=productid)
        product_json = product.to_json()
        return JsonResponse(product_json, safe=False)
    except:
        return JsonResponse({"error":"no such product"})
def category_list(request):
    try:
        categories = Category.objects.all()
        categories_json = categories.to_json()
        return JsonResponse(categories_json, safe=False)
    except:
        return JsonResponse({"error":"no categories"})  
def category(request, id):
    try:
        category = Category.objects.get(id = id)
        category_json = category.to_json()
        return JsonResponse(category_json, safe=False)
    except:
        return JsonResponse({"error":"No category"}) 
def products_category(request, id):
    try:
        product_list = Product.objects.filter(category=id)
        products_json = product_list.to_json()
        return JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({"error": "No products in category"})