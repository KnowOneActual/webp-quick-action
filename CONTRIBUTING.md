![Platform](https://img.shields.io/badge/Platform-macOS-000000?logo=apple&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python_3-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Maintained](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen)

# Contributing to WebP Quick Action

Thanks for your interest in improving this tool! 🚀

Whether you're fixing a bug in the Python logic or suggesting a new feature for the workflow, your help is welcome.

## How to Contribute

### 1. Reporting Bugs
If the script fails to convert a file, crashes, or behaves unexpectedly:
* **Check the requirements:** Ensure you have `webp` installed via Homebrew.
* **Open an Issue:** Describe what happened, which OS version you are on, and include any error messages if you ran it from the terminal.

### 2. Suggesting Features
Have an idea to make the compression better or the workflow smoother?
* Open a **Feature Request** issue.
* Explain *why* this change would be useful.

### 3. Submitting Pull Requests
1.  **Fork** the repository.
2.  **Clone** your fork locally.
3.  **Create a branch** for your changes (e.g., `fix-space-in-filenames` or `feat-lossless-option`).
4.  **Test your changes** (see below).
5.  **Push** to your fork and open a **Pull Request**.

---

## Development & Testing

Since the "Quick Action" part is just a wrapper, you should primarily test the Python script directly in your terminal.

### Prerequisites
You will need the `cwebp` tool installed:
```bash
brew install webp
````

### Testing the Script

1.  Grab a few test images (JPG, PNG).
2.  Run the script manually against them:
    ```bash
    # Replace with your actual path
    python3 convert_to_webp.py "path/to/test-image.jpg"
    ```
3.  Verify that:
      * A `.webp` file was created.
      * The script didn't crash.
      * The script gracefully handled files that were *already* WebP (it should skip them).

-----

## Style Guidelines

  * **Python:** We follow standard PEP 8 style. Keep the code readable and clean.
  * **Commits:** Write clear, descriptive commit messages (e.g., "Fix: Handle file paths with multiple spaces" instead of "fixed bug").

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.