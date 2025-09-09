create table public.user_skills (
  id uuid not null default gen_random_uuid (),
  user_id uuid not null,
  name text null,
  category text not null,
  subcategory text not null,
  description text null,
  professional_training text null,
  assessment_market_demand text null,
  assessment_passion_level smallint null,
  project_examples jsonb null,
  created_at timestamp with time zone null default now(),
  updated_at timestamp with time zone null default now(),
  assessment_required_investment text null,
  assessment_status text null,
  assessment_monetization_ideas jsonb[] null,
  assessment_viability jsonb[] null,
  assessment_notes text null,
  frequency_of_use text null,
  proficiency_level text null,
  experience text null,
  is_public boolean null,
  constraint user_skills_pkey primary key (id),
  constraint user_skills_user_id_fkey foreign KEY (user_id) references auth.users (id) on delete CASCADE,
  constraint user_skills_market_demand_check check (
    (
      assessment_market_demand = any (array['low'::text, 'medium'::text, 'high'::text])
    )
  ),
  constraint user_skills_passion_level_check check (
    (
      (assessment_passion_level >= 1)
      and (assessment_passion_level <= 5)
    )
  ),
  constraint valid_skill check (
    (
      (
        (name is not null)
        and (name <> ''::text)
      )
      or (
        (category is not null)
        and (subcategory is not null)
      )
    )
  )
) TABLESPACE pg_default;

create index IF not exists idx_user_skills_user_id on public.user_skills using btree (user_id) TABLESPACE pg_default;

create index IF not exists idx_user_skills_category on public.user_skills using btree (category) TABLESPACE pg_default;