#!/usr/bin/env python3
import sys
import os
import subprocess

# --- CONFIGURATION ---
# Check your path with 'which cwebp' in terminal if this fails
CWEBP_PATH = "/usr/local/bin/cwebp" 
# If using Apple Silicon (M1/M2/M3), uncomment the line below:
# CWEBP_PATH = "/opt/homebrew/bin/cwebp"

def pick_quality():
    """
    Uses AppleScript to show a native popup list to the user.
    Returns the numeric quality string (e.g., "75").
    """
    script = """
    set optionsList to {"100% (Best)", "75% (Default)", "50% (Small)", "25% (Tiny)"}
    set choice to choose from list optionsList with prompt "Select WebP Quality:" default items {"75% (Default)"}
    if choice is false then
        return "CANCEL"
    else
        return item 1 of choice
    end if
    """
    try:
        result = subprocess.check_output(['osascript', '-e', script], text=True).strip()
        
        if result == "CANCEL":
            return None
            
        # Extract just the number (e.g., "75% (Default)" -> "75")
        return result.split('%')[0]
    except Exception:
        # If something breaks (e.g. on Linux), default to 80
        return "80"

def convert_image(file_path, quality):
    if not os.path.exists(file_path):
        return

    filename, ext = os.path.splitext(file_path)
    
    # Skip if already webp
    if ext.lower() == ".webp":
        print(f"Skipping {os.path.basename(file_path)} (already WebP)")
        return

    output_path = f"{filename}.webp"
    
    try:
        # -q defines quality
        cmd = [CWEBP_PATH, "-q", quality, file_path, "-o", output_path, "-quiet"]
        subprocess.run(cmd, check=True)
        
    except subprocess.CalledProcessError:
        print(f"Error converting: {os.path.basename(file_path)}")
    except FileNotFoundError:
         print(f"Error: cwebp not found at {CWEBP_PATH}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 1. Ask the user for quality ONCE
        user_quality = pick_quality()
        
        # 2. If user hit Cancel, stop everything
        if not user_quality:
            sys.exit(0)
            
        # 3. Loop through all files with that quality
        for file_arg in sys.argv[1:]:
            convert_image(file_arg, user_quality)