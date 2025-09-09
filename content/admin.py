from django.contrib import admin
from .models import Programs, ContentMeta, Challenges, ChallengeSteps, Events, ResourceMeta


@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'mode', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('type', 'mode')


@admin.register(ContentMeta)
class ContentMetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content_type',
                    'sequence', 'program', 'difficulty')
    search_fields = ('title', 'description', 'slug')
    list_filter = ('content_type', 'difficulty', 'program')
    raw_id_fields = ('program', 'milestone', 'accomplishment')


@admin.register(Challenges)
class ChallengesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'program',
                    'difficulty', 'is_open', 'pub_date')
    search_fields = ('title', 'description')
    list_filter = ('difficulty', 'is_open', 'language', 'program')
    raw_id_fields = ('content_meta', 'program', 'milestone')
    filter_horizontal = ('tags',)


@admin.register(ChallengeSteps)
class ChallengeStepsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'challenge', 'sequence')
    search_fields = ('title', 'instructions')
    list_filter = ('challenge',)
    raw_id_fields = ('challenge',)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_time', 'end_time', 'is_paid')
    search_fields = ('title', 'description', 'event_type')
    list_filter = ('event_type', 'event_format', 'is_paid', 'is_member_only')
    raw_id_fields = ('created_by',)


@admin.register(ResourceMeta)
class ResourceMetaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_by')
    search_fields = ('title', 'description', 'slug')
    list_filter = ('status', 'tags', 'categories')
    raw_id_fields = ('created_by',)
    filter_horizontal = ('tags', 'categories',)
