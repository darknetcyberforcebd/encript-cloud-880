import os
import sys
import pyfiglet
from PIL import Image

# === ANSI Color Codes ===
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear')

# === Text to ASCII Art Module ===
def text_to_ascii():
    clear_screen()
    print(f"{CYAN}=== 📝 Text to ASCII Art ==={RESET}\n")
    text = input(f"{GREEN}[?] Enter your text: {RESET}")
    
    print(f"\n{YELLOW}Available Font Styles:{RESET}")
    print("1. Standard  2. Slant  3. 3-D  4. Block  5. Bubble")
    font_choice = input(f"{GREEN}[?] Choose font number (Default: Standard): {RESET}")
    
    fonts = {"1": "standard", "2": "slant", "3": "3-d", "4": "block", "5": "bubble"}
    selected_font = fonts.get(font_choice, "standard")
    
    try:
        ascii_art = pyfiglet.figlet_format(text, font=selected_font)
        print(f"\n{MAGENTA}--- Your ASCII Art ---{RESET}")
        print(f"{GREEN}{ascii_art}{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")
        
    input(f"\n{YELLOW}Press Enter to return to Main Menu...{RESET}")

# === Highly-Clearing Image to ASCII Art Module ===
def image_to_ascii():
    clear_screen()
    print(f"{CYAN}=== 🖼️ Ultra-Clear Image to ASCII Art ==={RESET}\n")
    img_path = input(f"{GREEN}[?] Enter Image Path: {RESET}")
    
    if not os.path.exists(img_path):
        print(f"{RED}[!] Error: File not found! Check the path again.{RESET}")
        input(f"\n{YELLOW}Press Enter to return...{RESET}")
        return

    try:
        img = Image.open(img_path)
        
        # INCREASED WIDTH TO 100 FOR HD-LIKE CLARITY ON DETAILED LOGOS
        width = 100 
        aspect_ratio = img.height / img.width
        # A bit extra vertical scaling to sharpen details
        height = int(width * aspect_ratio * 0.6) 
        img = img.resize((width, height)).convert("L") 
        
        # HIGH-CONTRAST ASCII CHARACTER MAP FOR SHARP OUTLINE
        # This map creates much clearer outlines for complex shapes.
        CHARS = ["@", "#", "8", "&", "o", ":", "*", " ", ".", " "] 
        
        pixels = list(img.getdata())
            
        # PUMPING UP CONTRAST FOR A SHARPER DEFINITION
        # Each pixel now has a clearer mapping, making shapes much crisper.
        ascii_str = "".join([CHARS[int(pixel / 25.6)] for pixel in pixels])
        
        prices_count = len(ascii_str)
        ascii_img = "\n".join([ascii_str[index:(index + width)] for index in range(0, prices_count, width)])
        
        print(f"\n{MAGENTA}--- Your Cleared Image ASCII Art ---{RESET}")
        # PRINTING EVERYTHING IN BRIGHT GREEN AS PER PREVIOUS PREFERENCE
        print(f"{GREEN}{ascii_img}{RESET}")
        
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")
        
    input(f"\n{YELLOW}Press Enter to return to Main Menu...{RESET}")

# === Main Dashboard ===
def main():
    while True:
        clear_screen()
        print(f"{CYAN}===================================={RESET}")
        print(f"{MAGENTA}     🎨 HD ASCII ART TOOL 🎨    {RESET}")
        print(f"{CYAN}===================================={RESET}")
        print(f"{GREEN}1.{RESET} Convert Text to ASCII Art")
        print(f"{GREEN}2.{RESET} Convert Image to ASCII Art")
        print(f"{RED}3.{RESET} Exit Tool")
        print(f"{CYAN}===================================={RESET}")
        
        choice = input(f"{YELLOW}[?] Select an option (1/2/3): {RESET}")
        
        if choice == '1':
            text_to_ascii()
        elif choice == '2':
            image_to_ascii()
        elif choice == '3':
            print(f"\n{YELLOW}Thank you for using ASCII Art Tool. Goodbye!{RESET}\n")
            break
        else:
            print(f"{RED}[!] Invalid choice! Try again.{RESET}")
            os.system('sleep 1')

if __name__ == "__main__":
    main()
