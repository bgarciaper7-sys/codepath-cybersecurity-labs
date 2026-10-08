# Project 1: CyberChef Capture the Flag (CTF)

## Overview

Course: CodePath CYB101 - Intro to Cybersecurity  
Unit: 1 - The Security Mindset  
Project: CyberChef CTF  
Tools: CyberChef, web research, text editor

## Project Objective

Apply cybersecurity research, critical thinking,
cryptography, and reconnaissance techniques to
solve Capture the Flag challenges.

The project included 11 challenges across three
categories:

- Cybersecurity trivia
- Reconnaissance
- Cryptography

## Challenge Summary

| Category | Challenges | Points |
|----------|------------|--------|
| Trivia | 1-3 | 3 |
| Reconnaissance | 4-6 | 3 |
| Cryptography | 7-11 | 10 |
| Total | 11 | 16 |

All 11 challenges were documented in my submission.

## Cybersecurity Trivia

### Challenge 1: Honesty is Best Policy

Concept: CIA Triad

I researched confidentiality, integrity, and
availability to identify the principle responsible
for preventing unauthorized data modification.

Key learning: Data integrity protects information
against unauthorized or accidental changes.

### Challenge 2: Lots of Jobs!

Concept: Cybersecurity workforce research

I used CyberSeek to compare cybersecurity job
openings across the states listed in the challenge.

Key learning: Researching reliable industry data
is an important cybersecurity skill.

### Challenge 3: Hostage

Concept: Ransomware

I identified ransomware as malware that encrypts
files and demands payment for decryption.

Key learning: Malware can compromise the
availability of critical information.

## Reconnaissance Challenges

### Challenge 4: 11,185,272

Concept: Open-source research

I researched historical Mersenne prime records
to identify the numerical pattern.

Key learning: Search engines and contextual
clues can help uncover unfamiliar information.

### Challenge 5: Read Me

Concept: File inspection

I inspected the supplied README.txt file using
a text editor to locate the challenge flag.

Key learning: Simple file inspection can reveal
important information.

### Challenge 6: Three Even, Two Odd

Concept: Logical deduction

I analyzed numerical clues to eliminate
incorrect digits and determine their positions.

Key learning: Systematic elimination and
pattern recognition support investigations.

## Cryptography Challenges

### Challenge 7: Shifty

Technique: Caesar cipher / ROT shift

I entered the ciphertext into CyberChef and
adjusted the rotation until the message
became readable.

Key learning: Classical substitution ciphers
can be analyzed by testing letter shifts.

### Challenge 8: Encoded Message

Technique: Base64 decoding

I recognized the trailing equals sign as a
possible indicator of Base64 encoding.

CyberChef operation:
From Base64

Key learning: Encoding transforms data
representation but does not provide encryption.

### Challenge 9: Kasiski Who?

Technique: Multi-stage decoding and Vigenere

The challenge involved a key encoded twice.

My decoding workflow:

1. Rail Fence Cipher Decode with 2 rails
2. ROT13 to recover the actual key
3. Vigenere Decode using the recovered key

Key learning: Multiple transformations may
need to be reversed in the correct order.

### Challenge 10: But Are There Eggs?

Technique: Bacon cipher

I researched the historical clue referring
to Francis Bacon and identified the
corresponding cipher.

CyberChef operation:
Bacon Cipher Decode

I adjusted the translation setting to A/B.

Key learning: Historical and contextual clues
can help identify encryption techniques.

### Challenge 11: Arch EXIF!

Technique: Image metadata analysis and Base64

I uploaded the provided image into CyberChef
and used Extract EXIF to examine its metadata.

I discovered an unusual encoded string in
the camera Make field.

I then applied From Base64 to decode it.

Key learning: Image metadata can contain
hidden information that is not visible
when viewing the image normally.

## Skills Demonstrated

- Capture the Flag problem-solving
- CyberChef recipe development
- Classical cipher identification
- Base64 decoding
- Multi-step cryptographic analysis
- Image metadata investigation
- Open-source research
- Logical reasoning
- Technical documentation

## Reflection

This project taught me to approach unfamiliar
cybersecurity problems through investigation
rather than immediately expecting an answer.

I practiced recognizing patterns, researching
unknown concepts, testing different methods,
and adjusting my approach when necessary.

The experience strengthened my analytical
thinking, persistence, and attention to detail.

## Project Outcome

Documented solutions and methods for all
11 CTF challenges, representing 16 available
challenge points.
