# CRM Project

Starter scaffold for a CRM application using Django and Bootstrap.

Quickstart

1. Create a virtualenv and activate it.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations and start the dev server:

```bash
python manage.py migrate
python manage.py runserver
```

Docker

Build and run the image:

```bash
docker build -t crm-app .
docker run -p 8000:8000 crm-app
```

CI

A basic GitHub Actions workflow is available at `.github/workflows/ci.yml` to run migrations and checks on pushes and PRs.

Postman / API

Import `docs/postman_collection.json` into Postman to get basic requests for the Contacts and Accounts APIs.

Create GitHub repo helper

If you'd like to create a remote repo and push from this workspace (requires `gh`):

```bash
chmod +x scripts/create_github_repo.sh
./scripts/create_github_repo.sh my-org-or-username/crm-repo
```

Automation

I added tools to automate local setup and Docker-based dev:

- `scripts/setup_dev.sh` — creates a virtualenv, installs dependencies, runs migrations, and can create a superuser when `CREATE_SUPERUSER=1` and `SUPERUSER_PASSWORD` are provided.
- `Makefile` — convenience targets: `make setup`, `make migrate`, `make run`, `make docker-up`.
- `docker-compose.yml` + `.env.example` — bring up a Postgres DB and web service using the `Dockerfile`.

Example local setup (recommended):

```bash
chmod +x scripts/setup_dev.sh
./scripts/setup_dev.sh
# To create a superuser non-interactively (dangerous in public envs):
CREATE_SUPERUSER=1 SUPERUSER_PASSWORD="yourpassword" ./scripts/setup_dev.sh
```

Or with Makefile:

```bash
make setup
make migrate
make run
```

Or start with Docker Compose:

```bash
cp .env.example .env
docker compose up --build
```

Frontend & Production

This repo includes a simple SPA `frontend/` intended to be built into static assets and served by `nginx` in production. Use the Makefile and Docker Compose targets below.

Makefile quick commands:

```bash
# start dev (interactive compose)
make start-dev

# build production images
make build-prod

# placeholder deploy target
make deploy
```

CI/CD

The GitHub Actions workflow `/.github/workflows/ci.yml` now builds the frontend (`npm ci && npm run build`) if `frontend/package.json` is present, copies built assets into `static/` for Django to collect, then installs Python deps, runs migrations, checks, and tests.


* SPA scaffold: add initial changes
