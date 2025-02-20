from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
# from django.db.models import Q
from django.shortcuts import render, redirect

from register.forms import ProductModelForm, RegisterForm, LoginForm
from register.models import ProductModel


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            change_permission = Permission.objects.get(codename='change_data', content_type__app_label='register')
            view_permission = Permission.objects.get(codename='view_data', content_type__app_label='register')

            user.user_permissions.add(change_permission, view_permission)

            login(request, user)
            return redirect('register:list')

    else:
        form = RegisterForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('register:list')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# @login_required
# def profile_view(request):
#     return render(request, 'profile.html', {'register': request.register})


def logout_view(request):
    logout(request)
    return redirect('register:login')


def get_view(request):
    get_product = ProductModel.objects.order_by('-pk')
    context = {
        'get_product': get_product
    }
    return render(request, 'index.html', context)


def create_product(request):
    form = ProductModelForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('register:list')

    context = {
        'form': form
    }

    return render(request, 'create_product.html', context)
