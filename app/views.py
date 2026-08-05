from django.shortcuts import render
from store.models import Category , Product , Comment
from django.shortcuts import get_object_or_404
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from store.forms import NameForm , CommentForm
from django.db.models import Q

# Create your views here.
def home_views(request):
    return render(request,"index.html")
def shop_views(request):
    products = Product.objects.filter(status=True)
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, "shop.html", context)
    

def search_views(request):

    query = request.GET.get("q")
    categories = Category.objects.all()
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "shop.html", context)

@login_required
def single_views(request, pid):

    categories = Category.objects.all()

    product = get_object_or_404(
        Product,
        id=pid,
        status=True
    )

    comments = Comment.objects.filter(product=product)


    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.product = product
            comment.user = request.user

            comment.save()

            return redirect("app:single", pid)


    else:
        form = CommentForm()


    context = {
        "categories": categories,
        "product": product,
        "comments": comments,
        "form": form
    }

    return render(request, "single.html", context)
def bestseller_views(request):
    return render(request,"bestseller.html")
def cart_views(request):
    return render(request,"cart.html")
def cheackout_views(request):
    return render(request,"cheackout.html")
def fourzero_views(request):
    return render(request,"404.html")
def contact_views(request):
    return render(request,"contact.html")