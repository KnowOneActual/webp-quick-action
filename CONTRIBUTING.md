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