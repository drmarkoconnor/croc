# Charlotte – Independent Portfolio (11ty + Supabase)

This repo scaffolds the **infrastructure and structure** for Charlotte’s CIF-604 Independent Portfolio.
It intentionally avoids inventing Charlotte’s artistic voice — content is placeholders.

## Tech

- Static site generator: Eleventy (11ty)
- Templates: Nunjucks
- Hosting: Netlify (recommended)
- Auth + data: Supabase (client-side for now)

## Setup (first time)

### 1) Install dependencies

```bash
npm install
```

### 2) Environment variables

Create a local `.env` file:

```bash
cp .env.example .env
```

Fill in:

- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`

> Never commit `.env`.

### 3) Run locally

```bash
npm run dev
```

Eleventy will serve the site and rebuild on changes.

## Git + GitHub workflow

### Initialize git (if you haven’t already)

```bash
git init
```

### First commit

```bash
git add .
git commit -m "Scaffold 11ty portfolio"
```

### Create a GitHub repo and push

(Example)

```bash
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

## Netlify deploy

1. Create a new site from GitHub.
2. Build command: `npm run build`
3. Publish directory: `_dist`
4. Add environment variables (Site settings → Environment variables):
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`

## Supabase

- The admin area is currently a **UI skeleton** and uses client-side Supabase auth.
- SQL to create tables is in `supabase/schema.sql`.

### Important note on security

Client-side Supabase requires strict **Row Level Security (RLS)** policies.
This scaffold includes a schema starter, but you should review and tighten policies before putting real data in production.

## Content placeholders

Anywhere you see:

```html
<!-- Charlotte to write -->
```

…that’s a deliberate placeholder.
