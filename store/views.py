from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Product, Wishlist
# Create your views here.
@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        wishlist_item.delete()

    return redirect("app:shop")

def delete_wishlist(request, product_id):

    wishlist_item = get_object_or_404(
        Wishlist,
        user=request.user,
        product_id=product_id
    )

    wishlist_item.delete()

    return redirect("store:wishlist")