const { test, expect } = require('@playwright/test');

test('SPA accounts page loads', async ({ page }) => {
  await page.goto('/accounts/');
  // ensure navigation succeeded (URL contains /accounts)
  await expect(page).toHaveURL(/\/accounts/);
});
