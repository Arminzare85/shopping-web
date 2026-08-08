from django.shortcuts import render
from store.models import Category , Product , Comment
from django.shortcuts import get_object_or_404
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from store.forms import NameForm , CommentForm
from django.db.models import Q
from django.core.paginator import Paginator
from app.forms import contactForm as ContactForm

# Create your views here.
def home_views(request ):
    products = Product.objects.filter(status=True)
    categories = Category.objects.all()
    sort = request.GET.get("sort")

    if sort == "new":
        products = products.order_by("-created_at")

    # elif sort == "top":
    #     products = products.order_by("-sales")   

     
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, "index.html", context)
    
def shop_views(request):
    products = Product.objects.filter(status=True)

    category = request.GET.get("category")

    if category:
        products = products.filter(category_id=category)

    paginator = Paginator(products, 6)

    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories
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
@login_required
def cart_views(request):

    cart = request.session.get("cart", {})

    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id,
            status=True
        )

        item_total = product.price * quantity

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "total": item_total,
        })

        total_price += item_total

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total_price": total_price,
    })

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        status=True
    )

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("app:cart")

@login_required
def remove_from_cart(request, product_id):

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("app:cart")

def remove_all_from_cart(request):
    request.session["cart"] = {}
    request.session.modified = True

    return redirect("app:cart")
def cheackout_views(request):
    return render(request,"cheackout.html")
def fourzero_views(request):
    return render(request,"404.html")

def contact_views(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("app:contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form
    })