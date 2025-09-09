from django.db import models
from django.conf import settings
import uuid


class Discounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    entity_name = models.TextField(blank=True, null=True)
    entity_type = models.TextField()
    entity_id = models.UUIDField()
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    value_type = models.TextField()
    currency = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discounts'
        verbose_name_plural = 'Discounts'


class Offerings(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    entity_type = models.TextField(blank=True, null=True)
    related_entity_id = models.UUIDField(blank=True, null=True)
    base_price_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    currency = models.TextField(blank=True, null=True)
    duration_months = models.SmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'offerings'
        verbose_name_plural = 'Offerings'


class UserTransactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    base_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    currency = models.TextField(blank=True, null=True)
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    discount = models.ForeignKey(
        Discounts,
        on_delete=models.DO_NOTHING,
        db_column='discount_id',
        blank=True,
        null=True
    )
    offering = models.ForeignKey(
        Offerings,
        on_delete=models.DO_NOTHING,
        db_column='offering_id',
        blank=True,
        null=True
    )
    offering_name = models.TextField(blank=True, null=True)
    offering_type = models.TextField(blank=True, null=True)
    payment_method = models.TextField(blank=True, null=True)
    payment_provider = models.TextField(blank=True, null=True)
    provider_data = models.JSONField(blank=True, null=True)
    provider_transaction_id = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    tax_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    total_amount_paid = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'user_transactions'
        verbose_name_plural = 'User Transactions'
