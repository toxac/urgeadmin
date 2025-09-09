# users/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.conf import settings
import uuid


class Roles(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Tells Django this table is not managed by migrations
        db_table = 'roles'
        verbose_name_plural = 'Roles'


class UserRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField(default=uuid.uuid4, null=True)
    role_id = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, db_column='role_id')
    role_name = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'
        verbose_name_plural = 'User Roles'


class Leads(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    # The 'programs' model is not defined yet, so we use a string reference
    program = models.ForeignKey(
        'content.Programs',
        on_delete=models.DO_NOTHING,
        db_column='program_id',
        blank=True,
        null=True
    )
    source = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default='lead')
    notes = models.TextField(blank=True, null=True)
    opt_newsletter = models.BooleanField(blank=True, null=True)
    opt_updates = models.BooleanField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    segment = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    other_details = models.JSONField(blank=True, null=True)
    source_details = models.JSONField(blank=True, null=True)
    communications = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'
        verbose_name_plural = 'Leads'


class UserEnrollments(models.Model):
    id = models.BigAutoField(primary_key=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id',
        blank=True,
        null=True
    )
    program = models.ForeignKey(
        'content.Programs',
        on_delete=models.DO_NOTHING,
        db_column='program_id',
        blank=True,
        null=True
    )
    program_name = models.TextField(blank=True, null=True)
    transaction_id = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_enrollments'
        verbose_name_plural = 'User Enrollments'


class UserMemberships(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    offering = models.ForeignKey(
        'finance.Offerings',
        on_delete=models.DO_NOTHING,
        db_column='offering_id',
        blank=True,
        null=True
    )
    transaction = models.ForeignKey(
        'finance.UserTransactions',
        on_delete=models.DO_NOTHING,
        db_column='transaction_id',
        blank=True,
        null=True
    )
    status = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_memberships'
        verbose_name_plural = 'User Memberships'


class UserProfiles(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    username = models.TextField(unique=True)
    bio = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    social_links = JSONField(blank=True, null=True)
    last_active_at = models.DateTimeField(blank=True, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='user_id'
    )
    gender = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    profile_picture = models.TextField(blank=True, null=True)
    age_group = models.TextField(blank=True, null=True)
    interests = JSONField(blank=True, null=True)
    employment = JSONField(blank=True, null=True)
    motivations = JSONField(blank=True, null=True)
    education = JSONField(blank=True, null=True)
    address = JSONField(blank=True, null=True)
    myths = JSONField(blank=True, null=True)
    settings = JSONField(blank=True, null=True)
    preferences = JSONField(blank=True, null=True)
    motivation_statement = models.TextField(blank=True, null=True)
    motivation_emotions = models.JSONField(blank=True, null=True)
    motivation_perfect_day = models.TextField(blank=True, null=True)
    motivation_deal_breakers = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    activations = models.JSONField(blank=True, null=True)
    roles = models.JSONField(blank=True, null=True)
    entrepreneurial_assessment = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profiles'
        verbose_name_plural = 'User Profiles'


class UserSkills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id'
    )
    name = models.TextField(blank=True, null=True)
    category = models.TextField()
    subcategory = models.TextField()
    description = models.TextField(blank=True, null=True)
    professional_training = models.TextField(blank=True, null=True)
    assessment_market_demand = models.TextField(blank=True, null=True)
    assessment_passion_level = models.SmallIntegerField(blank=True, null=True)
    project_examples = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    assessment_required_investment = models.TextField(blank=True, null=True)
    assessment_status = models.TextField(blank=True, null=True)
    assessment_monetization_ideas = models.JSONField(blank=True, null=True)
    assessment_viability = models.JSONField(blank=True, null=True)
    assessment_notes = models.TextField(blank=True, null=True)
    frequency_of_use = models.TextField(blank=True, null=True)
    proficiency_level = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_skills'
        verbose_name_plural = 'User Skills'


class NewsletterSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )
    status = models.TextField(blank=True, null=True, default='')

    class Meta:
        managed = False
        db_table = 'newsletter_subscriptions'
        verbose_name_plural = 'Newsletter Subscriptions'
