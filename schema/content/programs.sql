create table public.programs (
  id uuid not null default gen_random_uuid (),
  created_at timestamp with time zone not null default now(),
  name text not null,
  description text null,
  type text null,
  mode text null,
  price jsonb null,
  updated_at timestamp with time zone null,
  constraint programs_pkey primary key (id)
) TABLESPACE pg_default;