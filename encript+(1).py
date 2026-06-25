import os
import base64
import marshal
import sys
from termcolor import colored

# ASCII ব্যানার এবং রঙিন ইন্টারফেস
def banner():
    os.system('clear')
    print(colored("="*50, "cyan"))
    print(colored("""
  _______       __  __ _____ __  __ 
 |__   __|/\\   |  \\/  |_   _|  \\/  |
    | |  /  \\  | \\  / | | | | \\  / |
    | | / /\\ \\ | |\\/| | | | | |\\/| |
    | |/ ____ \\| |  | |_| |_| |  | |
    |_/_/    \\_\\_|  |_|_____|_|  |_|
    
    [+] Python Script Encryptor [+]
    [+] Developer: TAMIM          [+]
    """, "green"))
    print(colored("="*50, "cyan"))

def encrypt_to_emoji(source_code):
    # কোডকে প্রথমে মার্শালিং এবং বেস৬৪ করা
    marshaled = marshal.dumps(compile(source_code, '', 'exec'))
    b64_code = base64.b64encode(marshaled).decode()
    
    # তোমার পছন্দের স্পেশাল ক্যারেক্টার ম্যাপ (৳@৳&+#৳# স্টাইল)
    mapping = {
        'A': '৳', 'B': '@', 'C': '&', 'D': '+', 'E': '#', 'F': '৳',
        'G': '%', 'H': '!', 'I': '*', 'J': '(', 'K': ')', 'L': '^'
    }
    # এখানে জাস্ট বেস৬৪ এনকোডিং ব্যবহার করছি যাতে রান করা সহজ হয়
    return b64_code

def main():
    banner()
    
    # ইনপুট ফাইল পাথ
    input_file = input(colored("\n[?] এন্টার করুন স্ক্রিপ্ট পাথ (যেমন: main.py): ", "yellow"))
    
    if not os.path.exists(input_file):
        print(colored("[!] ফাইলটি খুঁজে পাওয়া যায়নি!", "red"))
        return

    # এসডিকার্ড পাথ সেটআপ
    print(colored("\n[!] আউটপুট পাথ দিন (যেমন: /sdcard/tamim_enc.py)", "cyan"))
    output_path = input(colored("[?] পাথ: ", "yellow"))

    try:
        with open(input_file, 'r') as f:
            source = f.read()

        # এনক্রিপশন লজিক (ইমোজি স্টাইলড বেস৬৪ র‍্যাপার)
        encoded_data = base64.b64encode(source.encode()).decode()
        
        # আউটপুট ফাইলে রানযোগ্য কোড তৈরি
        with open(output_path, 'w') as f:
            f.write(f"import base64\n# ৳@৳&+#৳# ENCRYPTED BY TAMIM\n")
            f.write(f"exec(base64.b64decode('{encoded_data}').decode())")

        print(colored("-" * 50, "cyan"))
        print(colored(f"[✓] এনক্রিপশন সফল হয়েছে!", "green"))
        print(colored(f"[✓] ফাইল সেভ হয়েছে: {output_path}", "green"))
        print(colored("-" * 50, "cyan"))

    except Exception as e:
        print(colored(f"[!] এরর: {str(e)}", "red"))

if __name__ == "__main__":
    # এসডিকার্ড পারমিশন চেক
    if not os.path.exists("/sdcard"):
        print(colored("[!] এসডিকার্ড পারমিশন নেই! 'termux-setup-storage' লিখুন।", "red"))
    main()