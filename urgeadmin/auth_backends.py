# urgeadmin/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from utils import supabase_client
from users.models import UserRoles


class SupabaseAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        supabase = supabase_client.get_supabase_client()
        try:
            # Step 1: Authenticate the user with Supabase.
            user_response = supabase.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
            user_info = user_response.user
            user_id = user_info.id

            # Step 2: Fetch the user's roles from the Django ORM
            # We query the UserRoles model which is linked to your Supabase table.
            user_roles_query = UserRoles.objects.filter(user_id=user_id)
            roles = [user_role.role_id for user_role in user_roles_query]

            is_admin = 5 in roles or 7 in roles
            is_superadmin = 7 in roles

            # Step 3: Get or create the Django User and set permissions.
            User = get_user_model()
            user, created = User.objects.get_or_create(
                username=user_id, email=user_info.email
            )

            # Update user permissions based on Supabase roles
            user.is_staff = is_admin
            user.is_superuser = is_superadmin
            user.save()

            return user

        except Exception as e:
            # Handle authentication errors from Supabase
            print(f"Supabase authentication failed: {e}")
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
