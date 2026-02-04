-- Supabase schema starter (review + adjust before production)
-- Tables per PROJECT_BRIEF.md

-- Enable extension for UUIDs if needed
-- create extension if not exists "uuid-ossp";

-- projects
create table if not exists public.projects (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  slug text not null unique,
  description text,
  role text,
  media_links jsonb default '[]'::jsonb,
  date date,
  featured boolean default false,
  order_index int default 0,
  visibility text default 'public' check (visibility in ('public','private')),
  created_at timestamptz default now()
);

-- profile (single row pattern)
create table if not exists public.profile (
  id int primary key generated always as identity,
  biography text,
  professional_summary text,
  creative_statement text,
  location text,
  contact_email text,
  updated_at timestamptz default now()
);

-- cv_items
create table if not exists public.cv_items (
  id uuid primary key default gen_random_uuid(),
  type text not null check (type in ('experience','education','release','performance')),
  title text not null,
  organisation text,
  date_range text,
  description text,
  order_index int default 0,
  created_at timestamptz default now()
);

-- practice_log
create table if not exists public.practice_log (
  id uuid primary key default gen_random_uuid(),
  date date not null,
  activity_type text,
  participants text,
  context text,
  actions_taken text,
  outcomes text,
  next_steps text,
  leadership_notes text,
  evidence_links jsonb default '[]'::jsonb,
  visibility text default 'private' check (visibility in ('private','reference','public')),
  tags text[],
  related_project_id uuid references public.projects(id),
  created_at timestamptz default now()
);

-- Basic RLS posture: enable but no policies by default.
-- Add policies explicitly after deciding editor/admin roles strategy.

alter table public.projects enable row level security;
alter table public.profile enable row level security;
alter table public.cv_items enable row level security;
alter table public.practice_log enable row level security;
