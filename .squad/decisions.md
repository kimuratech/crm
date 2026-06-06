---
title: Decisions
---

2026-06-05 — SPA Kick-off (merged from inbox)

Decision: Adopt a Single Page Application (SPA) front-end paired with the existing Django backend.

Architecture summary
--------------------
- Frontend: React + TypeScript + Vite.
- Backend: Django REST Framework exposing `/api/v1/` endpoints.
- Auth: JWT (djangorestframework-simplejwt) with optional server sessions for admins.
- Delivery: static assets served via Django staticfiles or CDN; Docker multi-stage builds for production images.

Owners & tasks
--------------
- Frontend scaffold: frontend-team
- API & auth: backend-team
- CI/CD & deployment: devops
- UX & product: product/UX

Reference inbox: [.squad/decisions/inbox/spa-kickoff-2026-06-05.md](.squad/decisions/inbox/spa-kickoff-2026-06-05.md)
# Decisions

This file is the canonical decision ledger for the squad. Agents write proposed decisions to `.squad/decisions/inbox/` and Scribe will merge them.
# Squad Decisions

## Active Decisions

No decisions recorded yet.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
