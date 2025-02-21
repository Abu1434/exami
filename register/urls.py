from django.contrib.auth.views import LogoutView
from django.urls import path

from register.views import get_view, create_product, register_view, login_view, profile_view

app_name = 'register'

urlpatterns = [
    path('', get_view, name='list'),
    path('reg/', register_view, name='reg'),
    path('create/', create_product, name='create'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('profile/', profile_view, name='profile'),
]
