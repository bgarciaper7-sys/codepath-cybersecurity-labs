# Week 6 Lab: Beneath the Images

**Course:** CodePath Cybersecurity 101  
**Topic:** Steganography, JPEG Analysis, and Hidden Data  
**Status:** Completed

## Lab Overview

In this lab, I explored how information can be concealed within digital images using file-format manipulation, embedded archives, and steganography techniques.

I used CyberChef to examine JPEG data, investigate hidden content, and extract concealed files. The exercises helped me understand why security analysts need to look beyond what an image displays visually.

## Tools and Technologies

- **CyberChef:** Hexadecimal inspection, data transformation, and file extraction
- **Docker:** Containerized lab environment
- **JPEG:** Image file format investigated during the exercises
- **Hexadecimal analysis:** Examination and modification of file bytes
- **ZIP:** Archive format used to conceal additional information

## Part 0: CyberChef Environment Setup

I prepared the lab environment using Docker and accessed CyberChef to perform image analysis.

This provided a workspace for inspecting file contents, transforming hexadecimal data, and extracting embedded information.

## Part 1: JPEG Structure and Metadata

I examined JPEG files to understand how image data and metadata are organized.

I learned that JPEG files contain structural information that software uses to interpret and display images. This information can also provide useful clues during a digital forensic investigation.

**Key concepts:**

- File headers help software recognize and interpret file formats.
- Metadata can describe attributes of a file without being part of its visible image.
- Hexadecimal representations allow investigators to inspect file bytes.

## Part 2: Hidden Data Investigation

### Challenge 1: Revealing concealed image content

I investigated `hidden.jpg`, a JPEG image containing content that was not initially visible.

Using CyberChef, I examined the image's hexadecimal representation and identified the height information in the JPEG Start of Frame header.

I changed the height value:

```text
Original: 01 3D (317 pixels)
Modified: 01 6F (367 pixels)
```

My CyberChef workflow included:

1. To Hex
2. Find/Replace
3. From Hex
4. Render Image

After modifying the image height, additional content became visible.

**Recovered message:**

```text
You found the secret text! Good job!
```

**What I learned:** Image file structure can affect what information is displayed. Examining file headers can reveal content that ordinary image viewers do not initially show.

### Challenge 2: Extracting an embedded ZIP archive

I investigated `ohNo.jpg`, which contained a concealed ZIP archive.

Using CyberChef's file extraction tools, I located the embedded archive and extracted its contents.

**CyberChef operations used:**

- Extract Files
- Unzip

I then reconstructed the message contained in the extracted material.

The exercise demonstrated that an image file can contain additional data beyond its visible picture.

**What I learned:** Analysts should inspect suspicious files for embedded content rather than relying solely on file extensions or visual appearance.

## Security Analysis

These exercises demonstrated several important differences between related techniques.

| Concept | Meaning |
|---|---|
| Steganography | Concealing information within another file or medium |
| Metadata | Information describing a file or its contents |
| File-format manipulation | Modifying structural information that controls how a file is interpreted |
| Embedded archive | An archive stored within or alongside another file's data |

Finding concealed information does not automatically prove malicious activity. Additional context and evidence are needed to determine whether a file presents a security threat.

## Skills Demonstrated

- JPEG file structure analysis
- Hexadecimal inspection
- CyberChef data transformations
- Embedded file identification and extraction
- Digital forensic reasoning
- Security analysis and documentation

## Reflection

The most interesting part of this lab was discovering that an image can contain information that is not immediately visible.

Before this exercise, I primarily thought of images as visual files. Working with hexadecimal data showed me that understanding file structure is important when investigating potentially concealed information.

I also learned that different concealment techniques require different investigative approaches. Modifying JPEG dimensions revealed hidden pixels, while extracting an embedded ZIP archive required file extraction tools.

This lab strengthened my understanding of how digital forensic investigators examine files beyond their visible contents.

## Related Work

See `../projects/README.md` for my graded steganography project, **The Artist's Message**, where I used ExifTool and Steghide to identify, extract, and embed hidden information.