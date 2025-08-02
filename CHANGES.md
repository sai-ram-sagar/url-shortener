
---

### `CHANGES.md`

```markdown
# CHANGES.md

## v1.0 - Initial Release (August 2025)

### 🔧 Refactoring & Improvements
- Restructured legacy monolithic Python code into modular Flask app:
  - Introduced `main.py` for route handling
  - Split logic into `models.py` (storage) and `utils.py` (helpers)
- Made app package-importable with `__init__.py`
- Ensured all functions are clearly separated by responsibility

### 🔐 Security & Stability
- Added URL validation using `urlparse`
- Implemented error handling for:
  - Invalid URLs
  - Missing short codes
- Made storage thread-safe using `threading.Lock`

### 🚦 Functionality Added
- `/shorten` endpoint: Accepts a valid URL, returns shortened version
- `/stats/<code>`: Returns JSON analytics (clicks, original URL, timestamp)
- Redirect via `/<short_code>`

### 🧪 Testing
- Added 6 Pytest test cases:
  - Valid URL shortening
  - Redirection
  - Stats retrieval
  - Invalid URL input
  - Non-existent short code
  - Repeat shortening

---

## Notes
- Chose in-memory storage per assignment spec (no DB)
- Used only standard Python libraries (no external services or ORMs)
- Tested on Python 3.13
