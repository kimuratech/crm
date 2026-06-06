const { test, expect } = require('@playwright/test');

test('Create lead via API and verify in list', async ({ request }) => {
  // register a user and obtain token
  const reg = await request.post('/api/auth/register/', {
    data: { username: 'leadtester', email: 'leadtester@example.com', password: 'Test1234!' },
  });
  // allow 201 (created) or 400 (already exists) and proceed to obtain token
  expect([201, 400]).toContain(reg.status());

  const tokenResp = await request.post('/api/token/', {
    data: { username: 'leadtester', password: 'Test1234!' },
  });
  expect(tokenResp.status()).toBe(200);
  const tokenBody = await tokenResp.json();
  const access = tokenBody.access;
  const auth = { headers: { Authorization: `Bearer ${access}` } };

  // create a lead
  const create = await request.post('/api/leads/', {
    data: { name: 'Delta Inc', email: 'delta@example.com', status: 'new' },
    ...auth,
  });
  expect(create.status()).toBe(201);

  // list leads and verify presence
  const list = await request.get('/api/leads/', auth);
  expect(list.status()).toBe(200);
  const leadsBody = await list.json();
  const leads = Array.isArray(leadsBody) ? leadsBody : leadsBody.results || [];
  const found = leads.find((l) => l.name === 'Delta Inc');
  expect(found).toBeTruthy();
});
