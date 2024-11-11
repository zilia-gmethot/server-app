from playwright.sync_api import Playwright


def test_read_root(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="http://localhost:8000")
    res = request_context.get("/")
    assert res.ok
    body = res.json()
    assert body["message"] == "Hello World!"
