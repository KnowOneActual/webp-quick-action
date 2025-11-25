# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-11-24
### Added
- **HEIC Support:** Added automatic conversion for `.heic` and `.heif` files (uses macOS `sips` to create a temporary PNG).
- **Metadata Preservation:** Now passes `-metadata all` to `cwebp` to ensure EXIF data (like orientation) is kept.

### Fixed
- Fixed an issue where portrait photos (especially from iPhones) would rotate 90 degrees incorrectly after conversion.

## [1.0.0] - 2025-11-20
### Added
- Initial release of the WebP conversion script.
- Added Python wrapper for `cwebp`.
- Created Automator workflow instructions.
- Update python script to prompt user for quality (100/75/50/25%).
- Uses osascript for native macOS dialog.
- Defaults to 75% quality for best size/fidelity balance.