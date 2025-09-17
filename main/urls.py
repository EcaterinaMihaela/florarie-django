from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('despre/', views.about, name='despre'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('floare/<int:floare_id>/', views.detalii_floare, name='detalii_floare'),
    path('register/', views.register, name='register'),

    path('favorites/', views.favorites, name='favorites'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_view, name='logout'),
    path('toggle-favorite/<int:flower_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('floare/<int:floare_id>/', views.detalii_floare, name='detalii_floare'),
    path('remove_favorite/<int:flower_id>/', views.remove_from_favorites, name='remove_favorite'),

    path('adauga-in-cos/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),
    path('cos/', views.view_cart, name='view_cart'),  # dacă ai și pagina coșului

    path('checkout/', views.checkout_view, name='checkout'),
    path('cos/sterge/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
