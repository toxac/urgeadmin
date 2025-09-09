# urgeadmin/db_routers.py
class SupabaseRouter:
    """
    A router to control which models use which database
    """
    django_models = {'user', 'group', 'permission',
                     'contenttype', 'session', 'logentry'}

    def db_for_read(self, model, **hints):
        if model._meta.model_name in self.django_models:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name in self.django_models:
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.django_models:
            return db == 'default'
        return None
