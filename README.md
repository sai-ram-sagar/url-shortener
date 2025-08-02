# Flask URL Shortener

This is a simple URL shortener service built with Python and Flask. It allows users to shorten long URLs, redirect using the short code, and view basic analytics such as click count and creation time.

---

## 🚀 Features

- Shorten any valid URL into a 6-character alphanumeric code
- Redirect to the original URL using the short code
- View analytics: original URL, creation timestamp, click count
- URL validation and basic error handling
- In-memory storage (no external DB)
- Thread-safe operations
- Includes unit tests using `pytest`

---


---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python -m flask --app app.main run

# Running Tests
pytest

```