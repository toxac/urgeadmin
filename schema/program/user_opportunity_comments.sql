create table public.user_opportunity_comments (
  id uuid not null default gen_random_uuid (),
  created_at timestamp with time zone not null default (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone null default (now() AT TIME ZONE 'utc'::text),
  title text null,
  content text null,
  comment_type text null,
  opportunity_id uuid null,
  user_id uuid null default gen_random_uuid (),
  constraint user_opportunity_comments_pkey primary key (id),
  constraint user_opportunity_comments_opportunity_id_fkey foreign KEY (opportunity_id) references user_opportunities (id) on delete CASCADE,
  constraint user_opportunity_comments_user_id_fkey foreign KEY (user_id) references auth.users (id) on delete CASCADE
) TABLESPACE pg_default;