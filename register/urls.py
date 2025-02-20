from django.contrib.auth.views import LogoutView
from django.urls import path

from register.views import get_view, create_product, login_view, register_view  # profile_view

app_name = 'register'

urlpatterns = [
    path('', get_view, name='list'),
    path('create/', create_product, name='create'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    # path('profile/', profile_view, name='profile'),
]
