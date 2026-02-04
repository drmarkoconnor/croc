# PROJECT BRIEF
## Charlotte – Independent Portfolio (CIF-604)

---

## 1. Project Purpose

Build a **professional, industry-facing online portfolio** for Charlotte that satisfies the academic and practical requirements of the CIF-604 Independent Portfolio module.

The system must:
- Support formal assessment requirements
- Present a credible professional identity
- Allow structured, private iteration over time
- Separate infrastructure from creative voice
- Enable evidence-backed critical analysis (written separately)

This document defines **infrastructure and structure only**.  
Charlotte’s creative content will be added later.

---

## 2. Assessment Constraints (Non-Negotiable)

The portfolio must support:

- Portfolio equivalent to ~15 pages of work
- Clear presentation of:
  - Creative work
  - Professional identity / CV
  - Branding and positioning
- Stable URLs accessible at assessment time
- Screenshot-friendly layouts for appendices
- External links to audio/video where appropriate

The **Critical Analysis** (PDF, max 1,800 words) is written separately and links to this site.

Failure to meet structural requirements invalidates the submission.

---

## 3. Technology Stack (Fixed)

### Core Stack
- Static Site Generator: Eleventy (11ty)
- Hosting: Netlify
- Version Control: GitHub
- Database & Authentication: Supabase
- Templating: Nunjucks
- Styling: Minimal CSS (no heavy JS frameworks)

### Architectural Principles
- Static-first
- Content-driven
- Progressive enhancement
- Editorial clarity over technical novelty
- No unnecessary client-side JavaScript

---

## 4. High-Level Site Structure

The system should scaffold the following routes:

/
├── index                (Landing / creative statement)
├── work/
│   ├── index            (Selected works overview)
│   ├── [project-slug]   (Individual project pages)
├── about/
│   ├── index            (Biography + identity)
├── cv/
│   ├── index            (Professional CV)
├── practice/
│   ├── index            (Curated professional practice summary)
│   ├── milestones       (Selected highlights)
├── admin/
│   ├── login
│   ├── dashboard
│   ├── projects
│   ├── practice-log
└── meta/
    └── screenshots      (Assessment evidence support)

---

## 5. Content Model (Supabase)

### Tables

#### projects
- id
- title
- slug
- description
- role
- media_links (array)
- date
- featured (boolean)
- order_index
- visibility (public / private)

#### profile
- biography
- professional_summary
- creative_statement
- location
- contact_email

#### cv_items
- type (experience / education / release / performance)
- title
- organisation
- date_range
- description
- order_index

#### users
- role (admin / editor)
- permissions

---

## 6. Practice & Leadership Log

### Purpose

Provide a **structured, date-based professional practice log** capturing evidence of:
- Initiative
- Leadership
- Collaboration
- Planning and follow-through
- Professional development

This is **not reflective journalling**.  
It is an evidential studio / producer log.

---

## 7. Practice Log Entry Structure

Each entry includes:

### Core Fields
- date
- activity_type (rehearsal, writing, meeting, recording, planning, admin, collaboration)
- participants (names + roles)
- context (why this occurred)
- actions_taken (what was done)
- outcomes (what progressed or changed)
- next_steps (explicit follow-on actions)
- leadership_notes (what Charlotte initiated or decided)
- evidence_links (URLs only)

### Metadata
- visibility (private / reference / public)
- tags (songwriting, collaboration, leadership, planning)
- related_project_id (optional)

---

## 8. Practice Log Database Table

practice_log
- id (uuid)
- date (date)
- activity_type (text)
- participants (text)
- context (text)
- actions_taken (text)
- outcomes (text)
- next_steps (text)
- leadership_notes (text)
- evidence_links (json)
- visibility (enum)
- related_project_id (uuid)
- created_at (timestamp)

---

## 9. Access & Permissions

### Roles

Admin (Mark):
- Full access
- Schema and deployment control
- Visibility moderation

Editor (Charlotte):
- Login-protected access
- Can edit projects and practice log entries
- Cannot alter layout or schema

### Authentication
- Supabase Auth
- Email + password
- Admin-controlled access

---

## 10. Practice Log Integration

Private admin routes:
- /admin/practice-log
- /admin/practice-log/new
- /admin/practice-log/[id]

Public derived views:
- /practice/
- /practice/milestones

Public views must summarise activity and avoid diary tone.

---

## 11. Relationship to Assessment

The practice log:
- Supports accurate dating of professional activity
- Provides evidence for Critical Analysis claims
- Demonstrates leadership, initiative, collaboration, and planning

The log itself is **not submitted**, but underpins credibility.

---

## 12. Visual & UX Principles

- Neutral typography
- Strong hierarchy
- Generous whitespace
- No autoplay media
- Professional restraint

---

## 13. Content Philosophy

The system must:
- Insert placeholders for creative content
- Avoid inventing artistic voice
- Support curation and omission

Use placeholders:
<!-- Charlotte to write -->

---

## 14. Deployment & Workflow

GitHub:
- main branch = production
- Netlify auto-deploy on push

Netlify:
- Environment variables for Supabase keys
- Preview deploys enabled

Local development:
- 11ty dev server
- .env for secrets
- No secrets committed

---

## 15. Deliverables Expected from AI Agent

- Folder structure
- 11ty config
- Base layouts
- Nunjucks templates
- Supabase schema
- Auth scaffolding
- Admin UI skeleton
- Placeholder content
- README

---

## 16. Explicit Non-Goals

The system must not:
- Invent Charlotte’s artistic identity
- Add marketing fluff
- Over-engineer CMS features
- Add heavy JS or animations
- Prematurely optimise SEO

---

## 17. Summary for AI Agent

Build a calm, professional, editable portfolio using 11ty, Netlify, and Supabase.
Separate infrastructure from creative content.
Support evidential professional practice via a structured log.
Prioritise assessment reliability and clarity.
