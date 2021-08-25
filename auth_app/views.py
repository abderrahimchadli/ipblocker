# Create your views here.
from django.shortcuts import render
from shopify_auth.decorators import login_required
import shopify

@login_required
def home(request, *args, **kwargs):
    with request.user.session:
        products=shopify.Product.find(limit=250)
        
        context={'products': products }
    return render(request, "home.html",context)

@login_required
def settings(request, *args, **kwargs):
    with request.user.session:
        products=shopify.Product.find(limit=250)
        
        context={'products': products }
    return render(request, "settings.html",context)

@login_required
def traffic(request, *args, **kwargs):
    with request.user.session:
        products=shopify.Product.find(limit=250)
        
        context={'products': products }
    return render(request, "traffic.html",context)