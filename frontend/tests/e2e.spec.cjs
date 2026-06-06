const { test, expect } = require('@playwright/test');

test('SPA root loads and shows title and root element', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/CRM Frontend/);
  const root = await page.locator('#root');
  await expect(root).toBeVisible();
});
