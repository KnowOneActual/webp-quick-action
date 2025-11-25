# macOS WebP Quick Action
![Platform](https://img.shields.io/badge/Platform-macOS-000000?logo=apple&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python_3-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Maintained](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen)

A simple, powerful macOS Quick Action that converts images to WebP format using a right-click context menu.

It uses Python to wrap Google's `cwebp` encoder, allowing for silent background processing, smart skipping of files that are already converted, and automatic handling of Apple's HEIC format.

## Features

* **Context Menu Integration:** Right-click any image in Finder -> Quick Actions -> Convert to WebP.
* **HEIC & HEIF Support:** Automatically handles iPhone/iPad `.heic` images by converting them to WebP (via a temporary internal conversion).
* **Preserves Orientation:** Keeps EXIF metadata intact so portrait photos don't end up rotated 90 degrees sideways.
* **Smart Skipping:** Automatically ignores files that are already `.webp`.
* **Non-Destructive:** Creates a new `.webp` file next to the original; it never overwrites your source images.
* **Silent Operation:** Runs in the background without popping up annoying terminal windows.

---

## Prerequisites

1.  **Install WebP Tools**
    You need the standard WebP libraries installed via Homebrew:
    ```bash
    brew install webp
    ```

2.  **Verify Python 3**
    Ensure you have Python 3 installed (standard on macOS):
    ```bash
    python3 --version
    ```

    *Note: For HEIC support, this tool uses the built-in macOS `sips` command, which comes pre-installed on all Macs.*

---

## Installation

### 1. Clone the Repo
Download this repository to a safe place where you keep your scripts (e.g., `~/scripts/`).

### 2. Create the Quick Action
1.  Open the **Automator** app on your Mac.
2.  Choose **File > New > Quick Action**.
3.  Configure the settings at the top:
    * **Workflow receives current:** `Image files`
    * **in:** `Finder`
    * **Image:** Choose the "Picture" icon (optional).
4.  Add the **Run Shell Script** action from the sidebar.
5.  **Important:** Set "Pass input" to **as arguments**.
6.  Paste the following code into the script box:
    ```bash
    # UPDATE THIS PATH to point to where you saved the script
    SCRIPT_PATH="$HOME/scripts/webp-quick-action/convert_to_webp.py"
    
    /usr/bin/python3 "$SCRIPT_PATH" "$@"
    ```
7.  Save the Quick Action as **"Convert to WebP"**.

---

## Usage

1.  Select one or more images in Finder (JPG, PNG, TIFF, HEIC, etc.).
2.  Right-click and select **Quick Actions > Convert to WebP**.
3.  The converted `.webp` versions will appear in the same folder.

---

## License

MIT License - see [LICENSE](LICENSE) for details.