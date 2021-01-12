from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm

from . forms import *
from . models import *


def home_page(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'aboutus.html')


def contact_us(request):
    return render(request, 'contactus.html')


# Contact form
#
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            to_email = ['seitakhunova@gmail.com']
            send_mail(subject, message, email, to_email, fail_silently=False)
    return redirect('home_page')


def our_news(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {'page': page, 'posts': posts})


def news_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'news_detail.html', {'post': post})

# Shop


def shop_main(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop.html', {'category': category,
                                         'categories': categories,
                                         'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {'product': product, 'cart_product_form': cart_product_form})



