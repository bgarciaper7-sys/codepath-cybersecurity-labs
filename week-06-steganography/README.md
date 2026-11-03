# Week 6: Steganography and Hidden Data Analysis

## Project Overview

During Week 6 of CodePath Cybersecurity 101, I investigated how information can be concealed inside digital images using steganography, file metadata, and embedded archives.

The lab involved examining JPEG file structures, identifying hidden content, extracting concealed messages, and embedding a password-protected message into an image.

For the graded project, **The Artist's Message**, I analyzed a collection of JPEG images, identified the correct file using metadata clues, extracted secret instructions, and successfully encoded a reply.

## Tools and Technologies

- **CyberChef:** Hexadecimal analysis, file extraction, and image manipulation
- **Docker:** Containerized lab environment
- **Linux Bash:** File navigation, inspection, and command-line operations
- **ExifTool:** Image metadata analysis
- **Steghide:** Extracting and embedding hidden files in JPEG images
- **VS Code:** Terminal access and documentation
- **PowerShell:** Docker setup and Git operations

## Lab Activities

### JPEG Structure and Metadata Analysis

- Examined JPEG file headers and hexadecimal data.
- Investigated image metadata to identify useful clues.
- Modified JPEG height information to reveal concealed image content.
- Extracted a hidden ZIP archive and reconstructed its message.

### The Artist's Message: Graded Project

- Investigated 26 JPEG images using ExifTool.
- Filtered images using author metadata and image dimensions.
- Examined image titles to identify an unusual clue.
- Tested a candidate passphrase using Steghide.
- Extracted and examined a concealed instruction file.
- Created a reply and embedded it into the designated JPEG.
- Verified the completed challenge using the lab's built-in checker.

**Final verification:** `CORRECT: Message encoded successfully. You win!`

Specific challenge filenames, passphrases, and concealed messages have been omitted to preserve the graded exercise.

## Skills Demonstrated

- Digital image and metadata analysis
- Steganography detection and extraction
- Hidden-file embedding
- Linux command-line operations
- Docker troubleshooting
- File-format investigation
- Technical documentation and problem-solving

## Key Takeaways

This lab demonstrated that information can be hidden inside seemingly ordinary image files without being visible when the images are opened normally.

I learned that metadata can provide investigative clues, but those clues must be validated using appropriate tools. Identifying unusual information does not automatically mean that a file is malicious.

The project strengthened my ability to investigate unfamiliar files, troubleshoot technical issues, and verify findings using command-line tools.

## Documentation

- [Hands-on Steganography Lab](labs/README.md)
- [The Artist's Message Graded Project](projects/README.md)

## Evidence

Screenshots documenting my investigation and successful project verification are organized in the `screenshots/` directory.