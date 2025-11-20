#!/usr/bin/env python3
import sys
import os
import subprocess

# Configuration
QUALITY = "80"  # Quality factor 0-100
CWEBP_PATH = "/usr/local/bin/cwebp" # Standard Homebrew path (Intel). 
# If on Apple Silicon (M1/M2/M3), use: "/opt/homebrew/bin/cwebp"

def convert_image(file_path):
    # check if file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    filename, ext = os.path.splitext(file_path)
    
    # Skip if already webp
    if ext.lower() == ".webp":
        print(f"⏭️  Skipping {os.path.basename(file_path)} (already WebP)")
        return

    # Determine output path
    output_path = f"{filename}.webp"
    
    try:
        # Run the cwebp command
        # -q defines quality
        # -quiet suppresses the standard output details
        cmd = [CWEBP_PATH, "-q", QUALITY, file_path, "-o", output_path, "-quiet"]
        subprocess.run(cmd, check=True)
        print(f"✅ Converted: {os.path.basename(output_path)}")
        
    except subprocess.CalledProcessError:
        print(f"⚠️  Error converting: {os.path.basename(file_path)}")
    except FileNotFoundError:
         print(f"❌ Error: cwebp not found at {CWEBP_PATH}. Check your path!")

if __name__ == "__main__":
    # Loop through all arguments passed from Automator
    if len(sys.argv) > 1:
        print("--- Starting WebP Conversion ---")
        for file_arg in sys.argv[1:]:
            convert_image(file_arg)
    else:
        print("No files provided.")