# SPA Architecture — CRM (Vite + React)

## Executive summary

Chosen stack: Vite + React (TypeScript optional) for the frontend, Django REST Framework (DRF) on the backend with djangorestframework-simplejwt for JWT auth. The frontend lives in `frontend/` and is buildable with `npm run build`. Backend keeps minimal runtime deps beyond DRF and SimpleJWT.

## Goals
- Provide a responsive single-page application (SPA) CRM UI.
- Keep backend lightweight and API-first (JSON over HTTPS).
- Make incremental migration from server-rendered templates possible.
- CI + Docker-based deployments for reproducible environments.

## Frontend tech
- Scaffold: Vite + React + TypeScript (recommended). Use React Router for navigation.
- HTTP client: Axios (or fetch) with a small wrapper for token handling.
- Data fetching: SWR or React Query (optional) — start with simple Axios + hooks.
- Styling: Tailwind CSS or plain CSS modules (team choice).
- Directory: `frontend/` (source) -> `frontend/dist/` (produced build).

Package.json scripts (recommended):
- `npm run dev` — start Vite dev server
- `npm run build` — produce production build to `dist/`
- `npm run preview` — locally preview built assets

## Data flow

- Single-page app loads index.html and JS bundle from `frontend/dist/`.
- Client authenticates using JWT access/refresh tokens issued by backend.
- Client sends `Authorization: Bearer <access>` header for protected API calls.
- When access token expires, client calls refresh endpoint (or uses refresh cookie) to get a new access token.
- All data exchanged as JSON via REST endpoints under `/api/`.

Example request flow:
- User logs in -> POST `/api/auth/login/` -> backend returns access + refresh (refresh in httpOnly cookie recommended).
- Client stores access token in memory (or secure storage) and uses it for calls.
- On 401 due to expired access -> call `/api/auth/refresh/` -> retry original request.

## Auth
- Use `djangorestframework-simplejwt` on backend.
- Endpoints (DRF standard):
  - `POST /api/token/` — obtain access + refresh
  - `POST /api/token/refresh/` — refresh access
  - `POST /api/token/verify/` — verify token (optional)
- For better XSS/CSRF protection: return the refresh token as an `HttpOnly` cookie from a login endpoint; keep access token in memory.
- Protect API views with `IsAuthenticated` or custom permissions.

## API endpoints (initial set)

- `POST /api/auth/login/` — wrapper to issue access + refresh (sets refresh cookie)
- `POST /api/auth/logout/` — clear refresh cookie / revoke refresh
- `GET /api/users/me/` — current user profile
- `GET/POST/PUT/PATCH/DELETE /api/accounts/`
- `GET/POST/PUT/PATCH/DELETE /api/contacts/`
- `GET/POST/PUT/PATCH/DELETE /api/companies/`
- `GET/POST/PUT/PATCH/DELETE /api/opportunities/`
- Search endpoints: `GET /api/search/?q=` (or expand per-resource filters)

Notes: Keep serializers focused and use viewsets + routers for consistent routing.

## Static assets strategy
- Development: Vite dev server serves the frontend on a separate port (e.g. 5173). Use CORS for local dev or a reverse-proxy.
- Production: Build frontend into static files (`frontend/dist/`). Serve via a small `nginx` container configured to serve `/` and proxy `/api/` to the Django backend. Alternative: use Django `collectstatic` to serve built assets (simpler but less performant).

Directory suggestions:
- `frontend/` — Vite source
- `nginx/` — production nginx config (optional)
- `docker/` — Dockerfiles and compose overrides

## Deployment approach

- Use Docker for reproducible builds:
  - `web` service: Django + Gunicorn (backend)
  - `db` service: Postgres (replace SQLite)
  - `static`/`frontend` service: nginx serving `frontend/dist/`
  - `worker` (optional): Celery if background jobs added later
- CI (GitHub Actions):
  1. Run Python tests (unit + DRF tests)
  2. Build frontend (`npm ci && npm run build`) and run frontend tests/lints
  3. Build Docker images and push to registry
  4. Deploy (staging -> production) using `docker-compose` or Kubernetes manifests

## Incremental migration strategy
- Keep existing Django templates and pages functional while rolling out SPA routes.
- Start by mounting the SPA on a subset of routes (e.g. `/app/` or `/crm/`) while keeping legacy pages unchanged.
- Provide a small API surface first (accounts, contacts) and iterate.

## Security considerations
- Use HTTPS in all environments. Enforce secure cookies and HSTS in production.
- Use `HttpOnly` + `Secure` flag for refresh cookies.
- Rate-limit authentication endpoints.

## Observability
- Add request logging middleware on the backend and centralize logs.
- Export basic metrics and health endpoints for Docker orchestration.

## File & task targets (first iteration)

- Backend (Keaton):
  - Add token endpoints and small auth wrappers: [apps/accounts/api.py](apps/accounts/api.py)
  - Add `users/me` view: [apps/accounts/views.py](apps/accounts/views.py)
  - Add router entries: [crm_project/urls.py](crm_project/urls.py)
  - Update settings for SimpleJWT and CORS: [crm_project/settings.py](crm_project/settings.py)

- Frontend (Dallas):
  - Scaffold Vite app: `frontend/package.json`, `frontend/src/main.tsx`
  - Add auth service and login screen: `frontend/src/services/auth.ts`
  - Add pages: `frontend/src/pages/Dashboard.tsx`, `frontend/src/pages/Contacts.tsx`

- Tester (Hockney):
  - Create backend API contract tests: `tests/test_api_auth.py` and `tests/test_contacts_api.py`
  - Create simple E2E smoke (optional): `frontend/test/smoke.test.js` or Cypress skeleton

- DevOps (Gordon):
  - Add `frontend` build step to CI workflow: `.github/workflows/ci.yml`
  - Add production nginx config: `nginx/default.conf` and `docker-compose.prod.yml`
  - Update `Dockerfile` or add `Dockerfile.frontend` to build and copy `frontend/dist`

## Per-agent first-commit tasks (1–2 day each)

- Backend / Keaton — Task KB1 (1 day):
  - Create DRF endpoints for auth wrapper and `users/me`.
  - Files: update [apps/accounts/api.py](apps/accounts/api.py), [apps/accounts/serializers.py](apps/accounts/serializers.py), [crm_project/urls.py](crm_project/urls.py), [crm_project/settings.py](crm_project/settings.py).

- Frontend / Dallas — Task DL1 (1–2 days):
  - Scaffold `frontend/` with Vite + React + TypeScript, add `npm run build` script, implement a Login page and basic routing.
  - Files: create `frontend/package.json`, `frontend/src/main.tsx`, `frontend/src/App.tsx`, `frontend/src/pages/Login.tsx`, `frontend/src/services/auth.ts`.

- Tester / Hockney — Task HK1 (1 day):
  - Add API contract tests for auth and `users/me`. Create test data fixtures and CI test step.
  - Files: `tests/test_api_auth.py`, `tests/conftest.py` (fixtures).

- DevOps / Gordon — Task GD1 (1–2 days):
  - Add CI job to build frontend and copy artifacts into a production `nginx` image; add `docker-compose.prod.yml` example.
  - Files: `.github/workflows/ci.yml`, `Dockerfile.frontend`, `nginx/default.conf`, `docker-compose.prod.yml`.

## Next steps
- Approve architecture decision and run a 2-week sprint to build base auth, contacts CRUD and a basic SPA shell. Iterate on data-fetch layer and state management in sprint 2.

---
Generated: 2026-06-05
