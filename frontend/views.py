from django.shortcuts import render
from . models import Product

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


def details(request):
    return render (request,'details.html')
