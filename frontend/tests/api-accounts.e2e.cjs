const { test, expect } = require('@playwright/test');

test('Accounts API returns JSON list', async ({ request }) => {
  const response = await request.get('/api/accounts/');
  expect(response.status()).toBe(200);
  const body = await response.json();
  expect(Array.isArray(body)).toBe(true);
});
