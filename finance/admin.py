from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Discounts, Offerings, UserTransactions


@admin.register(Discounts)
class DiscountsAdmin(ModelAdmin):
    list_display = (
        'code', 'entity_name', 'entity_type', 'value', 'value_type',
        'valid_from', 'valid_until'
    )
    list_filter = ('entity_type', 'value_type', 'currency')
    search_fields = ('code', 'entity_name', 'entity_id')


@admin.register(Offerings)
class OfferingsAdmin(ModelAdmin):
    list_display = (
        'name', 'entity_type', 'base_price_amount', 'is_active',
        'duration_months', 'created_at'
    )
    list_filter = ('entity_type', 'is_active', 'currency')
    search_fields = ('name', 'description')
    readonly_fields = ('related_entity_id',)


@admin.register(UserTransactions)
class UserTransactionsAdmin(ModelAdmin):
    list_display = (
        'id', 'user', 'offering_name', 'status', 'total_amount_paid',
        'created_at'
    )
    list_filter = ('status', 'payment_method', 'offering_type')
    search_fields = ('user__username', 'offering_name',
                     'provider_transaction_id')
    raw_id_fields = ('user', 'discount', 'offering')
