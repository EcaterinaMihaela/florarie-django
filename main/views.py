from django.shortcuts import render, get_object_or_404,redirect
from .models import Floare, Favorite
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


def about(request,floare_id):
   # return render(request, 'main/about.html')
   floare = get_object_or_404(Floare, id=floare_id)
   return render(request, 'main/detalii_floare.html', {'floare': floare})


def home(request):
    query = request.GET.get('q')
    flori = Floare.objects.filter(nume__icontains=query) if query else Floare.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(user=request.user).values_list('flower_id', flat=True)

    return render(request, 'main/lista_flori.html', {
        'flori': flori,
        'query': query,
        'favorite_ids': favorite_ids
    })

def detalii_floare(request, floare_id):
    floare = get_object_or_404(Floare, id=floare_id)
    return render(request, 'main/detalii_floare.html', {'floare': floare})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contul a fost creat cu succes! Acum te poți autentifica.')
            return redirect('login')  # redirecționează către pagina de login
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def favorites(request):
    if request.user.is_authenticated:
        favorite_entries = Favorite.objects.filter(user=request.user)
        favorite_flori = [fav.flower for fav in favorite_entries]
    else:
        favorite_flori = []
    return render(request, 'main/favorites.html', {'favorite_flori': favorite_flori})


def account(request):
    return render(request, 'main/account.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def toggle_favorite(request, flower_id):
    flower = get_object_or_404(Floare, id=flower_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, flower=flower)
    if not created:
        favorite.delete()  # era deja acolo → îl scoatem
    return redirect('home')

@login_required(login_url='login')  # sau lasă doar @login_required dacă ai setat LOGIN_URL în settings.py
def account(request):
    return render(request, 'main/account.html')


@login_required(login_url='login')
def remove_from_favorites(request, flower_id):
    if request.method == 'POST':
        Favorite.objects.filter(user=request.user, flower_id=flower_id).delete()
    return redirect('favorites')

@login_required(login_url='login')
def add_to_cart(request, flower_id):
    cart = request.session.get('cart', {})

    if str(flower_id) in cart:
        cart[str(flower_id)] += 1
    else:
        cart[str(flower_id)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

@login_required(login_url='login')
def view_cart(request):
    cart = request.session.get('cart', {})
    flowers = Floare.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0
    for floare in flowers:
        quantity = cart[str(floare.id)]
        subtotal = quantity * floare.pret
        total += subtotal
        cart_items.append({
            'flower': floare,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'main/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})
    flowers = Floare.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0
    for floare in flowers:
        quantity = cart.get(str(floare.id), 0)
        subtotal = quantity * floare.pret
        total += subtotal
        cart_items.append({
            'flower': floare,
            'quantity': quantity,
            'subtotal': subtotal
        })

    if request.method == 'POST':
        # Aici faci logica de creare comanda, stocare, etc.
        # După finalizare, golește coșul:
        request.session['cart'] = {}
        return render(request, 'main/checkout_success.html')

    return render(request, 'main/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return redirect('view_cart')