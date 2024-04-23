from django.shortcuts import render
from django.views import View
from .models import Category, Brand, Product


def get_categories_and_brands():
    return {
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
    }

def get_products_by_category(category_name):
    category = Category.objects.get(slug=category_name)
    return Product.objects.filter(category=category)


def get_products_by_brand(brand_name):
    brand = Brand.objects.get(name=brand_name)
    return Product.objects.filter(brand=brand)


def home(request):
    context = get_categories_and_brands()
    return render(request, "app/home.html", context)


class BaseView(View):
    def get(self, request, val=None):
        context = get_categories_and_brands()
        context['val'] = val
        return render(request, self.template_name, context)


class CategoryView(BaseView):
    template_name = "app/category.html"
    
    def get(self, request, val=None):
        if val is None or val == 'Te gjitha':
            products = Product.objects.all()
        else:
            products = get_products_by_category(val)

        context = {
            'products': products,
            'val': val,
            **get_categories_and_brands(),
        }
        print(products)
        return render(request, self.template_name, context)




class BrandView(BaseView):
    template_name = "app/brand.html"
    def get(self, request, val=None):
        if val is None or val == 'Te gjitha':
            products = Product.objects.all()
        else:
            products = get_products_by_brand(val)
        context = {
            'products': products,
            'val': val,
            **get_categories_and_brands(),
        }
        print(products)
        return render(request, self.template_name, context)
