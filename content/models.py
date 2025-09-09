from django.db import models
from django.db.models import JSONField
from django.conf import settings
import uuid


class Programs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    mode = models.TextField(blank=True, null=True)
    price = JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programs'
        verbose_name_plural = 'Programs'


class ContentMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(blank=True, null=True)
    content_type = models.TextField()
    sequence = models.SmallIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    related_content = JSONField(blank=True, null=True)
    milestone = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        db_column='milestone_id',
        blank=True,
        null=True
    )
    program = models.ForeignKey(
        Programs,
        on_delete=models.DO_NOTHING,
        db_column='program_id',
        blank=True,
        null=True
    )
    slug = models.TextField(blank=True, null=True)
    difficulty = models.TextField(blank=True, null=True)
    has_form = models.BooleanField(blank=True, null=True, default=False)
    content = models.TextField(blank=True, null=True)
    accomplishment = models.ForeignKey(
        'program.UserAccomplishments',
        on_delete=models.DO_NOTHING,
        db_column='accomplishment_id',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'content_meta'
        verbose_name_plural = 'Content Meta'


class Challenges(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content_meta = models.ForeignKey(
        ContentMeta,
        on_delete=models.DO_NOTHING,
        db_column='content_meta_id',
        blank=True,
        null=True
    )
    program = models.ForeignKey(
        Programs,
        on_delete=models.DO_NOTHING,
        db_column='program_id',
        blank=True,
        null=True
    )
    title = models.TextField()
    subtitle = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    updated_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    is_open = models.BooleanField(blank=True, null=True, default=False)
    difficulty = models.TextField(blank=True, null=True)
    badges = JSONField(blank=True, null=True)
    cover_image = JSONField(blank=True, null=True)
    language = models.TextField(default='en')
    version = models.IntegerField(blank=True, null=True)
    archived = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    milestone = models.ForeignKey(
        ContentMeta,
        on_delete=models.DO_NOTHING,
        db_column='milestone_id',
        related_name='challenges_milestone',
        blank=True,
        null=True
    )
    tags = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenges'
        verbose_name_plural = 'Challenges'


class ChallengeSteps(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    challenge = models.ForeignKey(
        Challenges,
        on_delete=models.DO_NOTHING,
        db_column='challenge_id',
        blank=True,
        null=True
    )
    sequence = models.SmallIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    reflection_questions = JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenge_steps'
        verbose_name_plural = 'Challenge Steps'


class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    event_type = models.TextField()
    event_format = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    online_link = models.TextField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_member_only = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.TextField(blank=True, null=True, default='USD')
    capacity = models.IntegerField(blank=True, null=True)
    featured_image_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='created_by',
    )
    location = JSONField(blank=True, null=True)
    sessions = JSONField(blank=True, null=True)
    exhibits = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'
        verbose_name_plural = 'Events'


class ResourceMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        db_column='created_by',
        blank=True,
        null=True
    )
    status = models.TextField(blank=True, null=True)
    tags = JSONField(blank=True, null=True)
    categories = JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_meta'
        verbose_name_plural = 'Resource Meta'
