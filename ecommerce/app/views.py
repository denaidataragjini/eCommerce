from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import CustomerRegistrationForm,CustomerProfileForm
from .models import Cart, Category, Brand, Customer, Product
from django.db.models import Q
from django.contrib import messages


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
        return render(request, self.template_name, context)


class CustomerRegistrationView(BaseView):
    template_name = "app/register.html"
    def get(self,request):

        context = {
            'form': CustomerRegistrationForm(),
            **get_categories_and_brands(),
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        context = {
            'form': form,
            **get_categories_and_brands(),
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            # return redirect('login')
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,self.template_name,context)


class ProfileView(BaseView):
    template_name = "app/profile.html"

    def get(self, request):
        form = CustomerProfileForm()
        context = {
            'form': form,
            **get_categories_and_brands(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            # Access cleaned_data from the form instance
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            zip_code = form.cleaned_data['zip_code']

            reg = Customer(
                user=user, 
                first_name=first_name, 
                last_name=last_name, 
                email=email,
                phone_number=phone_number, 
                address=address, 
                city=city, 
                state=state, 
                country=country, 
                zip_code=zip_code
            )
            reg.save()
            messages.success(request, "Profile saved successfully!")
        else:
            messages.warning(request, "Invalid input data")
        return render(request, self.template_name, {'form': form})
    
def address(request):
    add = Customer.objects.filter(user= request.user)
    context = {
        'add':add,
        **get_categories_and_brands(),
    }
    return render(request,'app/address.html',context)

class updateAddress(View):
    template_name = 'app/updateAddress.html'
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form= CustomerProfileForm(instance=add)
        context = {
            'add': add,
            'form': form,
            **get_categories_and_brands(),
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.first_name = form.cleaned_data['first_name']
            add.last_name = form.cleaned_data['last_name']
            add.email = form.cleaned_data['email']
            add.phone_number = form.cleaned_data['phone_number']
            add.address = form.cleaned_data['address']
            add.city = form.cleaned_data['city']
            add.state = form.cleaned_data['state']
            add.country = form.cleaned_data['country']
            add.zip_code = form.cleaned_data['zip_code']
            add.save()
            messages.success(request, "Profile updateted successfully!")
        else:
            messages.warning(request, "Invalid input data")
        return redirect('address')

def add_to_cart(request,pk):
    user=request.user
    product= Product.objects.get(id=pk)
    Cart(user=user, product=product).save()
    return redirect('cart')

def show_cart(request):
     user=request.user
     cart= Cart.objects.filter(user=user)
     amount=0
     for p in cart:
         value=0
         if(p.product.discount_price): 
           value= p.quantity * p.product.discount_price
         else:
           value= p.quantity * p.product.price
         amount= amount + value
     totalamount= amount +200
     context = {
            'user':user,
            'cart': cart,
            'amount': amount,
            'totalamount':totalamount,
            **get_categories_and_brands(),
        }
     return render(request, 'app/addtocart.html',context)

class checkout(View):
   def get(self, request):
       user=request.user
       add=Customer.objects.filter(user=user)
       cart_items= Cart.objects.filter(user=user)
       famount=0
       for p in cart_items:
         if(p.product.discount_price): 
           value= p.quantity * p.product.discount_price
         else:
           value= p.quantity * p.product.price
         famount= famount+value
       totalamount=famount+200
       context = {
            'user':user,
            'add': add,
            'cart_items': cart_items,
            'famount':famount,
            'totalamount':totalamount,
            **get_categories_and_brands(),
        }
       return render(request, 'app/checkout.html',context)
      

def plus_cart(request):
    if request.method== "GET":
        prod_id=request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity+=1
        c.save()
        cart= Cart.objects.filter(user=request.user)
        amount=0
        for p in cart:
          value=0
          if(p.product.discount_price): 
           value= p.quantity * p.product.discount_price
          else:
           value= p.quantity * p.product.price
          amount= amount + value
        totalamount= amount +200
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
    return JsonResponse(data)

def minus_cart(request):
    if request.method== "GET":
        prod_id=request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity-=1
        c.save()
        cart= Cart.objects.filter(user=request.user)
        amount=0
        for p in cart:
          value=0
          if(p.product.discount_price): 
           value= p.quantity * p.product.discount_price
          else:
           value= p.quantity * p.product.price
          amount= amount + value
        totalamount= amount +200
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
    return JsonResponse(data)

def remove_cart(request):
    if request.method== "GET":
        prod_id=request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.delete()
        cart= Cart.objects.filter(user=request.user)
        amount=0
        for p in cart:
          value=0
          if(p.product.discount_price): 
           value= p.quantity * p.product.discount_price
          else:
           value= p.quantity * p.product.price
          amount= amount + value
        totalamount= amount +200
        data={
            'amount':amount,
            'totalamount':totalamount
        }
    return JsonResponse(data)