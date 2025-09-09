create table public.user_opportunities (
  id uuid not null,
  created_at timestamp with time zone not null default now(),
  discovery_method text not null,
  observation_type text null,
  category text null,
  rank smallint null,
  user_id uuid null,
  status text null,
  updated_at timestamp with time zone null default now(),
  title text null,
  description text null,
  goal_alignment text null,
  constraint user_opportunities_pkey primary key (id),
  constraint user_opportunities_user_id_fkey foreign KEY (user_id) references auth.users (id) on delete CASCADE
) TABLESPACE pg_default;