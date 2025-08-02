import threading
from datetime import datetime, timezone
class URLStore:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}  # short_code -> {original_url, clicks, created_at}

    def add_url(self, short_code, original_url):
        with self.lock:
            self.data[short_code] = {
                "original_url": original_url,
                "clicks": 0,
"created_at": datetime.now(timezone.utc).isoformat()
            }

    def get_url(self, short_code):
        with self.lock:
            return self.data.get(short_code)

    def increment_clicks(self, short_code):
        with self.lock:
            if short_code in self.data:
                self.data[short_code]["clicks"] += 1

    def get_stats(self, short_code):
        with self.lock:
            return self.data.get(short_code)
