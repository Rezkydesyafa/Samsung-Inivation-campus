# app.py
from flask import Flask, request, make_response
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# --- logging ke file (rotating) ---
handler = RotatingFileHandler("captures.log", maxBytes=2_000_000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

def log_hit(label: str):
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ua = request.headers.get("User-Agent", "-")
    qs = parse_qs(urlparse(request.url).query)
    length = int(request.headers.get("Content-Length", 0) or 0)
    body = request.get_data(as_text=True) if length else ""
    stamp = datetime.utcnow().isoformat()+"Z"

    line = (
        f"[{stamp}] {label} {request.method} {request.path} "
        f"ip={ip} ua={ua!r} qs={qs} body={body[:500]!r}"
    )
    print("\n" + line)
    app.logger.info(line)

def ok(body="OK", code=200, ctype="text/plain"):
    resp = make_response(body, code)
    resp.headers["Content-Type"] = ctype
    return resp

@app.route("/")
def index():
    return ok("Flask listener alive. Use /leak or /pixel")

@app.route("/leak", methods=["GET", "POST"])
def leak():
    log_hit("LEAK")
    # 204 tanpa body juga aman untuk sendBeacon
    return ok("OK", 200)

@app.route("/pixel", methods=["GET"])
def pixel():
    log_hit("PIXEL")
    # 1x1 GIF
    pixel_gif = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00" \
                b"\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00," \
                b"\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
    return ok(pixel_gif, 200, "image/gif")

@app.route("/healthz")
def healthz():
    return ok("ok")

if __name__ == "__main__":
    # dengarkan di semua interface pada port 8080
    app.run(host="0.0.0.0", port=8080, debug=False)
