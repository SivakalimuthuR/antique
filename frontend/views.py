from django.shortcuts import render,redirect, get_object_or_404
from . models import Product
from .forms import ProductForm
from django.contrib import messages
# products=[
#         {'name':'Rolex watch', 'description': 'More stylish', 'Baseprice': '10,000', 'Currentprice': '15,000',},
#         {'name':'MRF bat', 'description': 'This is the bat used by MSD', 'Baseprice': '100000', 'Currentprice': '1,50000'},
#         {'name':'MobilePhone', 'description': '4GB RAM 128 ROM', 'Baseprice': '15000', 'Currentprice': '17054'},
#         {'name':'Laptop', 'description': 'Ryen 5500 series', 'Baseprice': '45000', 'Currentprice': '47000'},
#         {'name':'Android TV', 'description': 'Indias n0.1 TV brand', 'Baseprice': '35000', 'Currentprice': '40000'},
#         {'name':'Keyboard', 'description': 'Long lastin', 'Baseprice': '15000', 'Currentprice': '40500'},
#         {'name':'Wall clock', 'description': 'More durable', 'Baseprice': '25000', 'Currentprice': '40060'}
#     ]

def home(request):
    products = Product.objects.all()
    return render (request,'home.html', {"products":products})

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'detail.html', {'product': product})


def details(request):
    products = Product.objects.all()
    return render (request,'details.html', {"products":products})

def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.posted_by = request.user
            product.save()
            messages.success(request,'product posted sucessfully')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "There is an error in this form")
    else:
        form = ProductForm()
    return render(request, 'post_product.html', {'form': form})
