from playwright.sync_api import sync_playwright

def test_vendor_api():

    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.get("https://api.vendor.com/members")

        assert response.status == 200

        data = response.json()

        print("Records returned:", len(data))