from django.shortcuts import render
from django.views import View
from .models import Category, Brand


def get_categories_and_brands():
    return {
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
    }


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


class BrandView(BaseView):
    template_name = "app/brand.html"
