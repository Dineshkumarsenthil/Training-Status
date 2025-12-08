## Advanced API & Networking Concepts (Python)
---

## Rate Limiting Concepts

### What is Rate Limiting

`Rate limiting` is how an API controls how many requests you can send in a given time window.

Examples:

- 100 requests per minute
- 1000 requests per day
---

### Throttling

`Throttling` means the server actively slows or blocks your requests when you hit a limit.

Common behaviors:

- API starts returning error codes (often `429 Too Many Requests`).
- API adds delays or forces you to wait before you can call again.

APIs often send rate-limit info in header,

- `X-RateLimit-Limit` – max requests allowed
- `X-RateLimit-Remaining` – remaining requests in this window
- `X-RateLimit-Reset` – when the limit resets

---

### HTTP 429 (Too Many Requests)

`HTTP 429` :

> You sent too many requests in a short time; please back off.

Sometimes the server also sends:

- `Retry-After: 10`

which means:

> Wait 10 seconds before retrying.

Your client should:

- Detect `429` responses.
- Pause for the suggested time.
- Retry the request later.

---

### Retry Strategies

When you see temporary errors (`429`, `500`, `502`, `503`), you often want to `retry`.

Typical strategies:

1. `Fixed delay`
   - Always wait the same time between retries.
   - Example: wait 5 seconds every time.

2. `Exponential backoff`
   - Increase wait time after each failure.
   - Example: 1s → 2s → 4s → 8s → 16s.

3. `Backoff with jitter`
   - Exponential backoff + some randomness.
   - Avoids many clients retrying at exactly the same time.

Simple Python example using exponential backoff:

```python
import time
import requests

url = "https://api.example.com/data"
max_retries = 5
backoff = 1  

for attempt in range(1, max_retries + 1):
    resp = requests.get(url)

    if resp.status_code == 200:
        print("Success:", resp.json())
        break

    if resp.status_code == 429:
        retry_after = resp.headers.get("Retry-After")
        wait = int(retry_after) if retry_after else backoff
        print(f"Rate limited. Waiting {wait}s (attempt {attempt})")
        time.sleep(wait)
        backoff *= 2
    else:
        print(f"Error {resp.status_code}. Retrying in {backoff}s...")
        time.sleep(backoff)
        backoff *= 2
else:
        print("Failed after max retries.")
---
