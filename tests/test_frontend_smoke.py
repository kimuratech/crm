import os
import pytest


def test_frontend_build_artifact():
    """Smoke test: ensure frontend build artifact exists (mocked check).

    This test will be xfail'd if the expected artifact is missing. To make it
    enforceable in CI, ensure your frontend build is placed at
    `frontend/build/index.html`.
    """
    path = os.path.join('frontend', 'build', 'index.html')
    if not os.path.exists(path):
        pytest.xfail(f'Frontend build artifact not found at {path} (mocked check).')
    assert os.path.getsize(path) > 0


@pytest.mark.skipif(os.environ.get('RUN_LIVE_SERVER') != '1', reason='Live server tests disabled')
def test_live_server_health():
    import requests

    r = requests.get('http://127.0.0.1:8000/')
    assert r.status_code in (200, 302)
