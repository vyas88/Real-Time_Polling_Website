from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import NewsletterSubscription
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, "Username Or Password is incorrect!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'accounts/login.html')
def logout_user(request):
    logout(request)
    return redirect('home')
def create_user(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if password1 != password2:
                check1 = True
                messages.error(request, 'Password doesn\'t matched',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if check1 or check2 or check3:
                messages.error(
                    request, "Registration Failed", extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                messages.success(
                    request, f'Thanks for registering {user.username}!', extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Checking if the email already exists in the database:
        if not NewsletterSubscription.objects.filter(email=email).exists():
         NewsletterSubscription.objects.create(email=email)
         messages.success(request, 'Subscribed successfully!')
    else:
        messages.warning(request, 'This email is already subscribed.')
        pass
        return redirect('home')  # Redirect back to the home page.

    return render(request, 'home.html')
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Checking if the email already exists?
        if not NewsletterSubscription.objects.filter(email=email).exists():
            NewsletterSubscription.objects.create(email=email)
            messages.success(request, 'Subscribed!')
        else:
             messages.warning(request, 'Email is already subscribed.')
        return redirect('home')
    return render(request, 'home.html')
#homepage html connect links.
def about_us(request):
    return render(request, 'static_pages/about_us.html')
def our_services(request):
    return render(request, 'static_pages/our_services.html')
def privacy_policy(request):
    return render(request, 'static_pages/privacy_policy.html')
def contact(request):
    return render(request, 'accounts/contact.html')
