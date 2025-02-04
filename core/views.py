from django.shortcuts import render, redirect
from item.models import Item
from .forms import SignupForm
from django.contrib.auth import logout
from django.core.paginator import Paginator

def index(request):
    
    item_list = Item.objects.filter(is_sold=False)
    paginator = Paginator(item_list, 6)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    return render(request, 'core/index.html', {'page_obj': page_obj})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')

def custom_logout(request):
    logout(request)
    return redirect('core:home')

def home(request):
    return render(request, 'core/base.html')
