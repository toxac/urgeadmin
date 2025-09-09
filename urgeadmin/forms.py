# urgeadmin/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms


class SupabaseAdminAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form that uses Django's authenticate
    which will try all registered backends
    """

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Use Django's authenticate which tries all backends in order
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
