import json
import pytest
from django.test import Client


@pytest.mark.django_db
def test_contacts_crud():
    client = Client()

    # Create
    payload = {"first_name": "Jane", "last_name": "Doe", "email": "jane@example.com"}
    resp = client.post('/api/contacts/', data=json.dumps(payload), content_type='application/json')
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert data.get('first_name') == 'Jane'
    pk = data.get('id')
    assert pk is not None

    # Retrieve
    resp = client.get(f'/api/contacts/{pk}/')
    assert resp.status_code == 200
    item = resp.json()
    assert item.get('email') == 'jane@example.com'

    # Update
    resp = client.patch(f'/api/contacts/{pk}/', data=json.dumps({'email': 'jane.doe@example.com'}), content_type='application/json')
    assert resp.status_code in (200, 202)
    item = resp.json()
    assert item.get('email') == 'jane.doe@example.com'

    # Delete
    resp = client.delete(f'/api/contacts/{pk}/')
    assert resp.status_code in (200, 204)
