from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import OrderCreateForm
from .models import Order, OrderItem
from cart.helpers import Cart

# Create your views here.
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'order/order_create.html'
    # success_url = reverse_lazy('shop:product_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        return context


    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()
        order_items = [OrderItem(order=order, 
                                    product=obj['product'],
                                    quantity=obj['quantity']
                                    ) for obj in cart]
        OrderItem.objects.bulk_create(order_items)
        cart.clear()
        return render(self.request, 'order/created.html', {'order': order})
        