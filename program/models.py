from django.db import models
from django.conf import settings
from django.db.models import JSONField
import uuid

# Placeholder for the Accomplishments table, which is a dependency.


class Accomplishments(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'accomplishments'
        verbose_name_plural = 'Accomplishments'


class UserAccomplishments(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id',
        blank=True,
        null=True
    )
    accomplishment = models.ForeignKey(
        Accomplishments,
        on_delete=models.DO_NOTHING,
        db_column='accomplishment_id',
        blank=True,
        null=True
    )
    earned_at = models.DateTimeField(blank=True, null=True)
    context_data = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_accomplishments'
        verbose_name_plural = 'User Accomplishments'


class UserBookmarks(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )
    content_type = models.TextField(blank=True, null=True)
    related_content_id = models.UUIDField(blank=True, null=True)
    reference_url = models.TextField(blank=True, null=True)
    reference_table = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bookmarks'
        verbose_name_plural = 'User Bookmarks'


class UserChallengeProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id',
        blank=True,
        null=True
    )
    email = models.TextField(blank=True, null=True)
    challenge = models.ForeignKey(
        'content.Challenges',
        on_delete=models.DO_NOTHING,
        db_column='challenge_id'
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    last_step_completed = models.SmallIntegerField(blank=True, null=True)
    reflections = JSONField(blank=True, null=True)
    feedback_rating = models.SmallIntegerField(blank=True, null=True)
    notification_sent = JSONField(blank=True, null=True)
    feedback_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_challenge_progress'
        verbose_name_plural = 'User Challenge Progress'


class UserCheerSquad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )
    email = models.TextField()
    name = models.TextField(blank=True, null=True)
    relationship = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default='added')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_cheer_squad'
        verbose_name_plural = 'User Cheer Squad'


class UserCheerSquadUpdates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )
    cheer_squad = models.ForeignKey(
        UserCheerSquad,
        on_delete=models.DO_NOTHING,
        db_column='cheer_squad_id'
    )
    type = models.TextField()
    status = models.TextField(blank=True, null=True)
    update_text = models.TextField(blank=True, null=True)
    update_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_cheer_squad_updates'
        verbose_name_plural = 'User Cheer Squad Updates'


class UserNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    related_content_id = models.UUIDField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    reference_url = models.TextField(blank=True, null=True)
    reference_table = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_notes'
        verbose_name_plural = 'User Notes'


class UserOpportunities(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    discovery_method = models.TextField()
    observation_type = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    rank = models.SmallIntegerField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )
    status = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    goal_alignment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_opportunities'
        verbose_name_plural = 'User Opportunities'


class UserOpportunityComments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment_type = models.TextField(blank=True, null=True)
    opportunity = models.ForeignKey(
        UserOpportunities,
        on_delete=models.CASCADE,
        db_column='opportunity_id',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'user_opportunity_comments'
        verbose_name_plural = 'User Opportunity Comments'


class UserOpportunitySegments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    opportunity = models.ForeignKey(
        UserOpportunities,
        on_delete=models.CASCADE,
        db_column='opportunity_id'
    )
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )
    segment_name = models.TextField()
    segment_description = models.TextField()
    age_range_start = models.IntegerField(blank=True, null=True)
    age_range_end = models.IntegerField(blank=True, null=True)
    gender_focus = JSONField(blank=True, null=True)
    income_level = models.TextField(blank=True, null=True)
    education_level = JSONField(blank=True, null=True)
    occupation_types = JSONField(blank=True, null=True)
    family_status = models.TextField(blank=True, null=True)
    geographic_focus = models.TextField(blank=True, null=True)
    psychographic_traits = JSONField(blank=True, null=True)
    specific_needs = JSONField()
    specific_pains = JSONField()
    evidence_type = models.TextField()
    evidence_details = models.TextField()
    evidence_date = models.DateField(blank=True, null=True)
    people_researched = models.IntegerField(blank=True, null=True)
    estimated_segment_size = models.IntegerField(blank=True, null=True)
    accessibility_score = models.SmallIntegerField(blank=True, null=True)
    willingness_to_pay = models.TextField(blank=True, null=True)
    budget_range = models.TextField(blank=True, null=True)
    purchase_frequency = models.TextField(blank=True, null=True)
    validation_status = models.TextField(
        blank=True, null=True, default='identified')
    next_validation_steps = models.TextField(blank=True, null=True)
    outreach_plan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_opportunity_segments'
        verbose_name_plural = 'User Opportunity Segments'


class UserProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id'
    )
    completed_at = models.DateTimeField(blank=True, null=True)
    content_meta = models.ForeignKey(
        'content.ContentMeta',
        on_delete=models.DO_NOTHING,
        db_column='content_meta_id',
        blank=True,
        null=True
    )
    feedback_rating = models.SmallIntegerField(blank=True, null=True)
    feedback_text = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    form_completed = models.BooleanField(blank=True, null=True)
    has_form = models.BooleanField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default='not_started')
    content_title = models.TextField(blank=True, null=True)
    content_slug = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_progress'
        unique_together = (('user', 'content_meta'),)
        verbose_name_plural = 'User Progress'


class UserQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id',
        blank=True,
        null=True
    )
    related_content_id = models.UUIDField(blank=True, null=True)
    reference_url = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    reference_table = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_questions'
        verbose_name_plural = 'User Questions'


class UserQuestionResponses(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='user_id',
        blank=True,
        null=True
    )
    feedback_rating = models.SmallIntegerField(blank=True, null=True)
    question = models.ForeignKey(
        UserQuestions,
        on_delete=models.DO_NOTHING,
        db_column='question_id',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'user_question_responses'
        verbose_name_plural = 'User Question Responses'
