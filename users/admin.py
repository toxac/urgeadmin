from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Roles, UserRoles, Leads, UserEnrollments, UserMemberships, UserProfiles, UserSkills, NewsletterSubscriptions

# Register your models here.


@admin.register(Roles)
class RolesAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(UserRoles)
class UserRolesAdmin(ModelAdmin):
    list_display = ('id', 'user_id', 'role_id', 'role_name', 'created_at')
    search_fields = ('user_id',)
    list_filter = ('role_name',)


@admin.register(Leads)
class LeadsAdmin(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'status', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('status', 'source', 'created_at')


@admin.register(UserEnrollments)
class UserEnrollmentsAdmin(ModelAdmin):
    list_display = ('id', 'user', 'program', 'enrolled_at')
    search_fields = ('user__username', 'program_name')
    list_filter = ('enrolled_at', 'program_name')


@admin.register(UserMemberships)
class UserMembershipsAdmin(ModelAdmin):
    list_display = ('id', 'user', 'offering', 'status',
                    'created_at', 'valid_until')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')


@admin.register(UserProfiles)
class UserProfilesAdmin(ModelAdmin):
    list_display = ('user', 'username', 'first_name',
                    'last_name', 'last_active_at')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('last_active_at', 'gender')
    # Use a custom fieldset to organize the JSON fields for better readability
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'username', 'first_name', 'last_name', 'bio', 'profile_picture')
        }),
        ('Contact & Social', {
            'fields': ('website', 'social_links')
        }),
        ('Demographics', {
            'fields': ('gender', 'age_group', 'country', 'city')
        }),
        ('User Data', {
            'fields': (
                'interests',
                'employment',
                'motivations',
                'education',
                'address',
                'myths',
                'settings',
                'preferences',
                'entrepreneurial_assessment'
            ),
            'classes': ('collapse',),  # This makes the section collapsible
        }),
        ('Motivation & Details', {
            'fields': (
                'motivation_statement',
                'motivation_emotions',
                'motivation_perfect_day',
                'motivation_deal_breakers'
            ),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'last_active_at')
        })
    )

    # Make JSON fields read-only to prevent direct editing through the admin, as it can be complex.
    readonly_fields = (
        'activations',
        'roles',
        'interests',
        'employment',
        'motivations',
        'education',
        'address',
        'myths',
        'settings',
        'preferences',
        'entrepreneurial_assessment'
    )


@admin.register(UserSkills)
class UserSkillsAdmin(ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'category', 'subcategory', 'proficiency_level',
        'created_at'
    )
    list_filter = (
        'category', 'subcategory', 'assessment_status', 'proficiency_level',
        'is_public'
    )
    search_fields = ('user__username', 'name', 'description')
    raw_id_fields = ('user',)
    readonly_fields = (
        'project_examples', 'assessment_monetization_ideas',
        'assessment_viability',
    )


@admin.register(NewsletterSubscriptions)
class NewsletterSubscriptionsAdmin(ModelAdmin):
    list_display = ('email', 'user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('email',)
    raw_id_fields = ('user',)
