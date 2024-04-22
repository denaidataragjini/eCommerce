from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    return render(request,"app/home.html")

# There are two ways to render the page, by class and by function
class CategoryView(View):
    def get(self,request):
        return render(request,"app/category.html")

class BrandView(View):
    def get(self,request):
        return render(request,"app/brand.html")