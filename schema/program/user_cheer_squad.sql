create table public.user_cheer_squad (
  id uuid not null default extensions.uuid_generate_v4 (),
  user_id uuid not null,
  email text not null,
  name text null,
  relationship text null,
  status text null default 'added'::text,
  created_at timestamp with time zone null default now(),
  updated_at timestamp with time zone null default now(),
  constraint user_cheer_squad_pkey primary key (id),
  constraint user_cheer_squad_user_id_fkey foreign KEY (user_id) references auth.users (id)
) TABLESPACE pg_default;

create index IF not exists idx_user_cheer_squad_user_id on public.user_cheer_squad using btree (user_id) TABLESPACE pg_default;