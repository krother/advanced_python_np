import playwright
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("timisoara")
    page.get_by_role("link", name="Timișoara City and county").click()

    page.screenshot(path="screenshot.png")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)