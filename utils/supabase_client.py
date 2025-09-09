# utils/supabase_client.py
import os
from supabase import create_client, Client


def get_supabase_client() -> Client:
    """Returns a new Supabase client instance."""
    url: str = os.environ.get("PUBLIC_SUPABASE_URL")
    service_role_key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

    return create_client(url, service_role_key)
