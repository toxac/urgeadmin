# urgeadmin/admin.py
from django.contrib.admin import AdminSite


class UrgeAdminSite(AdminSite):
    """
    Custom admin site without Supabase authentication
    """
    site_header = 'Urge Admin'
    site_title = 'Urge Administration'
    index_title = 'Welcome to Urge Admin'


# Instantiate the custom admin site
admin_site = UrgeAdminSite(name='urgeadmin')
