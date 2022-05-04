from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem 
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'paid', 'postal_code', 'created_at', 'get_total_cost']
    list_display_link = ['id', 'created_at']
    list_filter = ['paid', 'city']
    inlines = [OrderItemInline]

    def get_total_cost(self, field):
        return field.get_total_cost()

admin.site.register(Order, OrderAdmin)