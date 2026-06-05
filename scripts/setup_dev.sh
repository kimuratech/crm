#!/usr/bin/env bash
set -euo pipefail

# setup_dev.sh - create venv, install deps, run migrations, and optionally create a superuser

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/venv"

echo "[setup] ROOT_DIR=$ROOT_DIR"

if [ ! -d "$VENV_DIR" ]; then
  echo "[setup] Creating virtualenv at $VENV_DIR"
  python3 -m venv "$VENV_DIR"
fi

echo "[setup] Activating virtualenv"
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

echo "[setup] Upgrading pip and installing requirements"
python -m pip install --upgrade pip
pip install -r "$ROOT_DIR/requirements.txt"

echo "[setup] Running migrations"
python "$ROOT_DIR/manage.py" migrate --noinput

if [ "${CREATE_SUPERUSER:-}" = "1" ]; then
  USERNAME=${SUPERUSER_USERNAME:-admin}
  EMAIL=${SUPERUSER_EMAIL:-admin@example.com}
  PASSWORD=${SUPERUSER_PASSWORD:-password}
  echo "[setup] Creating superuser $USERNAME (non-interactive)"
  python - <<PY
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${USERNAME}').exists():
    User.objects.create_superuser('${USERNAME}', '${EMAIL}', '${PASSWORD}')
    print('superuser created')
else:
    print('superuser exists')
PY
fi

echo "[setup] Done. To start the dev server: source venv/bin/activate && python manage.py runserver"
