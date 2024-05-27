from django.shortcuts import render
from django.views import View

from ecommerce.app.forms import CustomerRegistrationForm
from .models import Category, Brand, Product


def get_categories_and_brands():
    return {
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
    }

def get_products_by_category(category_name):
    category = Category.objects.get(slug=category_name)
    return Product.objects.filter(category=category).all()


def get_products_by_brand(brand_name):
    brand = Brand.objects.get(name=brand_name)
    return Product.objects.filter(brand=brand).all()


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
    

class DetailView(BaseView):
    template_name = "app/details.html"
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        
        context = {
            'product':product,
            'pk':pk,
            **get_categories_and_brands(),
        }
        print(product)
        return render(request, self.template_name, context)


class CustomerRegistrationView(View):
    template_name = "app/register.html"
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,self.template_name,locals())
