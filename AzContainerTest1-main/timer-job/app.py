import os, datetime, requests

def maybe_call_backend():
    url = os.getenv("BACKEND_URL")
    if not url:
        return "No BACKEND_URL set; skipping call."
    try:
        r = requests.get(url, timeout=10)
        return f"Backend GET {url} -> {r.status_code}, body: {r.text}"
    except Exception as e:
        return f"Backend call failed: {e}"

if __name__ == "__main__":
    now = datetime.datetime.utcnow().isoformat()
    print(f"[timer-job] hello from container apps job at {now}Z")
    print(maybe_call_backend())
    # exit(0) implicitly
