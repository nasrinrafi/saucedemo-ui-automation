import pytest

@pytest.fixture(scope="session")
def api_config():
    """
    این فیکسچر تنظیمات پایه برای اتصال به API را فراهم می‌کند.
    scope=session باعث می‌شود این تنظیمات در طول اجرای تمام تست‌ها فقط یک‌بار ساخته شوند.
    """
    return {
        "base_url": "https://httpbin.org",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Content-Type": "application/json"
        }
    }