import asyncio
import logging
from typing import Optional

from playwright.async_api import async_playwright

from open_webui.env import SRC_LOG_LEVELS

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MAIN"])


async def visit_as_admin(
    *,
    chat_id: str,
    base_url: str,
    admin_email: str,
    admin_password: str,
    ws_url: Optional[str],
    timeout_ms: int,
) -> None:
    login_url = f"{base_url.rstrip('/')}/auth"
    target_url = f"{base_url.rstrip('/')}/s/{chat_id}"

    async with async_playwright() as playwright:
        if ws_url:
            browser = await playwright.chromium.connect_over_cdp(ws_url)
        else:
            browser = await playwright.chromium.launch(headless=True)

        try:
            context = await browser.new_context()
            page = await context.new_page()
            page.set_default_timeout(timeout_ms)

            log.info("Report bot: logging in as admin at %s", login_url)
            await page.goto(login_url, wait_until="domcontentloaded")
            await page.fill("input[name='email']", admin_email)
            await page.fill("input[name='current-password']", admin_password)
            await page.click("button[type='submit']")
            await page.wait_for_load_state("networkidle")
            log.info("Report bot: login complete")

            log.info("Report bot: visiting %s", target_url)
            await page.goto(target_url, wait_until="domcontentloaded")
            await page.wait_for_load_state("networkidle")
            page_title = await page.title()
            log.info("Report bot: visit complete %s (title=%s)", page.url, page_title)
            await asyncio.sleep(2)
        finally:
            await browser.close()
