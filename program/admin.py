from django.contrib import admin
from .models import (
    Accomplishments, UserAccomplishments, UserBookmarks, UserChallengeProgress,
    UserCheerSquad, UserCheerSquadUpdates, UserNotes, UserOpportunities,
    UserOpportunityComments, UserOpportunitySegments, UserProgress,
    UserQuestions, UserQuestionResponses
)

# Placeholder for a model that is a dependency


@admin.register(Accomplishments)
class AccomplishmentsAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(UserAccomplishments)
class UserAccomplishmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'accomplishment', 'earned_at')
    search_fields = ('user__username', 'accomplishment__id')
    list_filter = ('earned_at',)
    raw_id_fields = ('user', 'accomplishment',)


@admin.register(UserBookmarks)
class UserBookmarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_type',
                    'related_content_id', 'created_at')
    search_fields = ('user__username', 'content_type', 'related_content_id')
    list_filter = ('content_type', 'created_at')
    raw_id_fields = ('user',)


@admin.register(UserChallengeProgress)
class UserChallengeProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'challenge',
                    'completed_at', 'last_step_completed')
    search_fields = ('user__username', 'challenge__title')
    list_filter = ('completed_at', 'last_step_completed')
    raw_id_fields = ('user', 'challenge',)


@admin.register(UserCheerSquad)
class UserCheerSquadAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'relationship', 'status')
    search_fields = ('user__username', 'name', 'email')
    list_filter = ('status', 'relationship')
    raw_id_fields = ('user',)


@admin.register(UserCheerSquadUpdates)
class UserCheerSquadUpdatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cheer_squad',
                    'type', 'status', 'created_at')
    search_fields = ('user__username', 'cheer_squad__name', 'update_text')
    list_filter = ('type', 'status')
    raw_id_fields = ('user', 'cheer_squad',)


@admin.register(UserNotes)
class UserNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content_type', 'updated_at')
    search_fields = ('user__username', 'title', 'content')
    list_filter = ('content_type',)
    raw_id_fields = ('user',)


@admin.register(UserOpportunities)
class UserOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title',
                    'discovery_method', 'status', 'rank')
    search_fields = ('user__username', 'title', 'description')
    list_filter = ('discovery_method', 'status', 'category')
    raw_id_fields = ('user',)


@admin.register(UserOpportunityComments)
class UserOpportunityCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'opportunity', 'comment_type', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('comment_type',)
    raw_id_fields = ('user', 'opportunity',)


@admin.register(UserOpportunitySegments)
class UserOpportunitySegmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'opportunity',
                    'segment_name', 'validation_status')
    search_fields = ('user__username', 'segment_name', 'segment_description')
    list_filter = ('validation_status', 'income_level', 'education_level')
    raw_id_fields = ('user', 'opportunity',)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_title', 'status', 'completed_at')
    search_fields = ('user__username', 'content_title', 'content_slug')
    list_filter = ('status', 'content_type', 'completed_at')
    raw_id_fields = ('user', 'content_meta',)


@admin.register(UserQuestions)
class UserQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'is_public', 'status')
    search_fields = ('user__username', 'title', 'content')
    list_filter = ('is_public', 'status', 'content_type')
    raw_id_fields = ('user',)


@admin.register(UserQuestionResponses)
class UserQuestionResponsesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'feedback_rating', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('feedback_rating', 'created_at')
    raw_id_fields = ('user', 'question',)
