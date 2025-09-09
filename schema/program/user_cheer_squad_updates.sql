create table public.user_cheer_squad_updates (
  id uuid not null default extensions.uuid_generate_v4 (),
  user_id uuid not null,
  cheer_squad_id uuid not null,
  type text not null,
  status text null,
  update_text text null,
  update_link text null,
  created_at timestamp with time zone null default now(),
  constraint user_cheer_squad_updates_pkey primary key (id),
  constraint user_cheer_squad_updates_cheer_squad_id_fkey foreign KEY (cheer_squad_id) references user_cheer_squad (id),
  constraint user_cheer_squad_updates_user_id_fkey foreign KEY (user_id) references auth.users (id)
) TABLESPACE pg_default;

create index IF not exists idx_user_cheer_squad_updates_relationships on public.user_cheer_squad_updates using btree (user_id, cheer_squad_id) TABLESPACE pg_default;