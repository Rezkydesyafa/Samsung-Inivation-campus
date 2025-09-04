# solve_flag_roundmapped.py — menangkap prompt tanpa newline & map per-ronde
import socket, sys, re
from math import gcd

ANSI = re.compile(r'\x1b\[[0-9;]*m')
PROMPT_RX = re.compile(r'Enter guess for round\s+(\d+)\s*/\s*(\d+)\s*>>')
BANNER_RX = re.compile(r'Round\s+(\d+)\s*/\s*(\d+)')

def strip(s): return ANSI.sub('', s)

def recover_s_candidates(N, c, f, U1, max_try=256):
    X  = U1 % N
    K  = ((U1 - X) // N) % N
    EM = (f - c) % N
    R  = (EM * X) % N
    g  = gcd(K, N)
    if g == 1:
        return [ (R * pow(K, -1, N)) % N ]
    # Reduksi ke N' = N/g (sangat jarang terjadi, tapi tetap kita sediakan)
    Np = N // g
    Kp = (K // g) % Np
    Rp = (R // g) % Np
    s0 = (Rp * pow(Kp, -1, Np)) % Np
    upto = min(g, max_try)
    return [ (s0 + t * Np) % N for t in range(upto) ]

def solve(host, port):
    with socket.create_connection((host, port), timeout=70) as sock:
        sock.settimeout(70)  # server total TIME=72s
        print(f"[+] Connected to {host}:{port}")

        buf = ""               # buffer mentah (untuk cari prompt tanpa newline)
        linebuf = ""           # buffer baris (untuk parsing N,c,f,U1 per newline)
        cur_round = None
        rounds = {}            # rounds[i] = {"N":..,"c":..,"f":..,"U1":..}
        sent_rounds = set()    # ronde yang sudah dikirim

        def have_all(i):
            d = rounds.get(i, {})
            return all(k in d for k in ("N","c","f","U1"))

        while True:
            chunk = sock.recv(65536).decode(errors="ignore")
            if not chunk:
                print("[!] Server closed connection.")
                break

            sys.stdout.write(chunk); sys.stdout.flush()
            buf += chunk
            linebuf += chunk

            # 1) PARSE per-baris untuk N,c,f,U1 dan banner
            while True:
                pos = linebuf.find("\n")
                if pos == -1: break
                line = strip(linebuf[:pos+1]).strip()
                linebuf = linebuf[pos+1:]

                if line.startswith("===") and "Round" in line:
                    m = BANNER_RX.search(line)
                    if m:
                        cur_round = int(m.group(1))
                        rounds.setdefault(cur_round, {})
                    continue
                if line.startswith("N ="):
                    rounds.setdefault(cur_round, {})["N"] = int(line.split("=",1)[1])
                elif line.startswith("c ="):
                    rounds.setdefault(cur_round, {})["c"] = int(line.split("=",1)[1])
                elif line.startswith("f ="):
                    rounds.setdefault(cur_round, {})["f"] = int(line.split("=",1)[1])
                elif line.startswith("U1 ="):
                    rounds.setdefault(cur_round, {})["U1"] = int(line.split("=",1)[1])

                # flag?
                if "flag{" in line.lower():
                    print("\n[+] FLAG received!")
                    return

            # 2) DETEKSI PROMPT tanpa newline langsung dari buffer mentah
            for m in list(PROMPT_RX.finditer(buf)):
                i = int(m.group(1))  # ronde yang diminta
                if i in sent_rounds:
                    continue  # sudah kirim (jaga-jaga)
                if not have_all(i):
                    # Data round i belum lengkap → tunggu chunk berikutnya
                    continue

                d = rounds[i]
                cands = recover_s_candidates(d["N"], d["c"], d["f"], d["U1"], max_try=256)
                # Kirim kandidat pertama; jika server balas "Wrong/Fail", sesi memang akan ditutup.
                s_val = cands[0]
                sock.sendall((str(s_val) + "\n").encode())
                sent_rounds.add(i)
                print(f"\n[+] Sent s for round {i}: {s_val}\n")

            # 3) early-flag scan juga di buf
            if "flag{" in buf.lower():
                print("\n[+] FLAG received!")
                return

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "20.6.89.33"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8055
    solve(host, port)
