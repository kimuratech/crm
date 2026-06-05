# Integration & QA Plan — SPA + API

This document describes manual integration/QA steps and checkpoints for the single-page frontend (SPA) and Django API backend.

Manual UI test flow
- **Prerequisites:** devserver running (backend) and frontend served or built. Create a test user via Django admin if needed.
- **Login:**
  - Open app in browser and log in with a valid account.
  - Check session persistence (close & re-open tab).
- **List view:**
  - Navigate to Accounts and Contacts list pages.
  - Verify list loads and displays items (status 200 on network tab). Check empty-state messaging.
- **Create:**
  - Create a new Account: enter name, industry, submit.
  - Verify new item appears in list and in API (`GET /api/accounts/`).
  - Create a new Contact linked or standalone, verify appearance and API.
- **Edit:**
  - Edit the Account and Contact entries from the UI.
  - Confirm changes persist and API `GET /api/.../<id>/` shows updates.
- **Delete:**
  - Delete created Account/Contact via UI.
  - Confirm removed from list and `GET` returns 404.

Performance checkpoints
- Time-to-interactive: ensure SPA initial load is acceptable (< 2s on CI lab network baseline).
- API latency: list and detail endpoints should respond within target SLA (e.g., < 200ms under light load).

Accessibility checkpoints
- Keyboard navigation: ensure list and forms are operable by keyboard.
- Form labels: all form fields have visible labels or aria-labels.
- Color contrast: verify foreground/background contrast for primary UI elements.
- Basic audit: run Lighthouse accessibility audits on critical pages (login, list, detail).

Note: Automate these manual steps over time using Playwright or Cypress; the repository currently contains pytest-based backend integration smoke tests.
