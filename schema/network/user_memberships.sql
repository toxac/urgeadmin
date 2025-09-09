create table public.user_memberships (
  id uuid not null default gen_random_uuid (),
  created_at timestamp with time zone not null default now(),
  valid_until timestamp with time zone null,
  offering_id bigint null,
  transaction_id uuid null,
  status text null,
  user_id uuid null default gen_random_uuid (),
  updated_at timestamp with time zone null,
  constraint user_memberships_pkey primary key (id),
  constraint user_memberships_offering_id_fkey foreign KEY (offering_id) references offerings (id),
  constraint user_memberships_transaction_id_fkey foreign KEY (transaction_id) references user_transactions (id),
  constraint user_memberships_user_id_fkey foreign KEY (user_id) references auth.users (id) on delete CASCADE
) TABLESPACE pg_default;