from playwright.sync_api import sync_playwright

def test_dashboard():

    with sync_playwright() as p:

        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://dashboard.example.com")

        total_members = page.locator("#member-count").inner_text()

        assert int(total_members) > 0