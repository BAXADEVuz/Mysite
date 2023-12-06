from django.shortcuts import render
from django.views import View
from . models import Product
from django.db.models import Count
from . forms import CustomerRegistrationFrom
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")


class CategoryView(View):
        def get(self,request,val):
            product = Product.objects.filter(category=val)
            title = Product.objects.filter(category=val).values('title')
            return render(request,"core/category.html",locals())


class CategoryTitle(View):
        def get(self,request,val):
            product = Product.objects.filter(title=val)
            title = Product.objects.filter(category=product[0].category).values('title')
            return render(request,"core/category.html",locals())


class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"core/productdetail.html",locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationFrom
        return render(request,'core/customerregistration.html',locals())
    def post(self, request):
        form = CustomerRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations! User Register Successfully')
        else:
            messages.warning(request,'Invalid Input Data')
        return render(request,'core/customerregistration.html',locals())




