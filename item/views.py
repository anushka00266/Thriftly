from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import JsonResponse
from .models import Item, Order
from .forms import NewItemForm, EditItemForm, ShippingDetailsForm

def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {'items': items, 'query': query})

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {'item': item})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {'form': form, 'title': 'New Item'})

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('item:items')

@login_required
def purchase_item(request, item_id):  
    item = get_object_or_404(Item, pk=item_id)  

    if request.method == 'POST':
        return redirect('item:shipping_details', item_id=item.id)
    
    return render(request, 'item/purchase.html', {'item': item})

@login_required
def shipping_details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':
        form = ShippingDetailsForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                item=item,
                payment_method='COD',
                status='Pending',
            )
            
            order.shipping_full_name = form.cleaned_data['full_name']
            order.shipping_address = form.cleaned_data['address']
            order.shipping_phone_number = form.cleaned_data['phone_number']
            order.shipping_city = form.cleaned_data['city']
            order.shipping_postal_code = form.cleaned_data['postal_code']
            order.save()

            return redirect('item:order_confirmation', order_id=order.id)
    else:
        form = ShippingDetailsForm()

    return render(request, 'item/shipping_details.html', {'form': form, 'item': item})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'item/order_confirmation.html', {'order': order})
