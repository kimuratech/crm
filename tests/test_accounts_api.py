import json
import pytest
from django.test import Client


@pytest.mark.django_db
def test_accounts_crud():
    client = Client()

    # Create
    payload = {"name": "TestCo", "industry": "Software"}
    resp = client.post('/api/accounts/', data=json.dumps(payload), content_type='application/json')
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert data.get('name') == 'TestCo'
    pk = data.get('id')
    assert pk is not None

    # List
    resp = client.get('/api/accounts/')
    assert resp.status_code == 200
    items = resp.json()
    assert any(item.get('id') == pk for item in items)

    # Update (partial)
    resp = client.patch(f'/api/accounts/{pk}/', data=json.dumps({'industry': 'Finance'}), content_type='application/json')
    assert resp.status_code in (200, 202)
    updated = resp.json()
    assert updated.get('industry') == 'Finance'

    # Delete
    resp = client.delete(f'/api/accounts/{pk}/')
    assert resp.status_code in (200, 204)
