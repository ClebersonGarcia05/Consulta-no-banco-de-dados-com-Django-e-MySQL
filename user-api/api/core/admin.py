from django.contrib import admin

from .models import Order, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at', 'updated_at')
    list_filter = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'item_price', 'item_quantity', 'user_id', 'total_value')
    list_filter = ('user_id', )