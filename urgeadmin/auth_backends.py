# urgeadmin/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from utils import supabase_client
from users.models import UserRoles


class SupabaseAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()

        # First, try Django's built-in authentication for superusers
        try:
            user = User.objects.get(email=email)
            if user.has_usable_password() and user.check_password(password):
                print(f"Django user authenticated: {email}")
                return user
        except User.DoesNotExist:
            pass  # User doesn't exist in Django, try Supabase

        # If not a Django user, try Supabase authentication
        supabase = supabase_client.get_supabase_client()
        try:
            user_response = supabase.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
            user_info = user_response.user
            user_id = user_info.id

            # Fetch user roles
            user_roles_query = UserRoles.objects.filter(user_id=user_id)
            roles = [user_role.role_id for user_role in user_roles_query]

            is_admin = 5 in roles or 7 in roles
            is_superadmin = 7 in roles

            # Get or create Django User
            user, created = User.objects.get_or_create(
                username=user_id,
                email=user_info.email,
                defaults={
                    'is_staff': is_admin,
                    'is_superuser': is_superadmin,
                    'password': '!',  # Set unusable password
                }
            )

            if not created:
                user.is_staff = is_admin
                user.is_superuser = is_superadmin
                user.save()

            print(f"Supabase user authenticated: {user_info.email}")
            return user

        except Exception as e:
            print(f"Supabase authentication failed: {e}")
            # If Supabase auth fails, return None to let other backends try
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
