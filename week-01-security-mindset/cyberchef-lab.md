# Unit 1 Lab: Introduction to CyberChef

## Overview
**Course:** CodePath CYB101 - Intro to Cybersecurity  
**Unit:** 1 - The Security Mindset  
**Lab:** Introduction to CyberChef  
**Tools:** CyberChef, CrackStation

## Objective
Develop practical skills using CyberChef to investigate encoded data, solve introductory Capture the Flag (CTF) challenges, analyze image files, and explore password hashes.

## Exercise 1: Decode a Simple Cipher

**Objective:** Identify and decode an encoded message.

**Ciphertext:**
```text
Terng wbo qrpbqvat lbhe svefg pvcure!
```

**Technique:** ROT13

**CyberChef operation:** ROT13

**Decoded message:**
```text
Great job decoding your first cipher!
```

**Key takeaway:** ROT13 substitutes letters using a fixed 13-position shift and does not provide modern cryptographic security.

## Exercise 2: Let's Build a Fence!

**Objective:** Decode a hidden key and use it to decrypt a message.

**Ciphertext:**
```text
Acx'vt dhppu dqpzbui! Yhie im br!
```

**Techniques explored:**
- Rail Fence cipher
- Vigenere cipher

**Process:**
1. Investigate the encoded key provided in the challenge.
2. Use a Rail Fence decoding operation to recover the key.
3. Use the decoded key with the Vigenere decoding operation.
4. Examine the resulting plaintext.

**Decoded key:** [Add verified result]

**Decoded message:** [Add verified result]

**Key takeaway:** Some cryptographic challenges require multiple decoding operations performed in the correct order.

## Exercise 3: Is a ROT13 Always a Shift of 13?

**Objective:** Identify the correct Caesar cipher shift.

**Ciphertext:**
```text
Ijhtinsl rjxxfljx nx kzs, gzy bmfy jqxj hfs bj it?!
```

**Technique:** Caesar cipher / ROT shift

**Process:**
1. Enter the ciphertext into CyberChef.
2. Test different rotation values.
3. Identify the shift that produces readable plaintext.

**Correct shift:** [Add verified result]

**Decoded message:** [Add verified result]

**Key takeaway:** Caesar ciphers can use different rotation values, not only 13.

## Exercise 4: Broken Image File

**Objective:** Investigate and repair a corrupted image header.

**Input file:** Lab1_Ex4.png

**Concepts:**
- File signatures
- Magic numbers
- Binary file formats

**Process:**
1. Upload the provided image into CyberChef.
2. Inspect the file's initial bytes.
3. Compare the bytes against known image signatures.
4. Repair the incorrect magic numbers.
5. Check whether the image renders successfully.

**Repair result:** [Add verified observation]

**Key takeaway:** File extensions alone do not determine file type. File signatures help software recognize file formats.

## Exercise 5: Hidden Message

**Objective:** Reveal information hidden within an image.

**Input file:** Lab1_Ex5.png

**Concept:** Hidden data and steganography

**Process:**
1. Load the image into CyberChef.
2. Investigate operations that may reveal hidden text.
3. Examine the output for an embedded message.

**CyberChef operation used:** [Add verified operation]

**Hidden message:** [Add verified result]

**Key takeaway:** Images may contain information beyond what is immediately visible.

## Exercise 6: Hashes Anyone?

**Objective:** Investigate a password hash and use the recovered value to decode a message.

**Ciphertext:**
```text
Qfw ech'uv rkoqb wox huh gruxrfk!
```

**Provided hash:**
```text
8621ffdbc5698829397d97767ac13db3
```

**Tools:** CrackStation and CyberChef

**Process:**
1. Enter the provided hash into CrackStation.
2. Check whether a matching plaintext value is found.
3. Investigate how the recovered value can be used to decode the message.

**Recovered value:** [Add verified result]

**Decoded message:** [Add verified result]

**Key takeaway:** Weak or commonly used passwords can sometimes be recovered from unsalted hashes using precomputed databases.

## Skills Practiced
- CyberChef recipe construction
- ROT13 and Caesar cipher analysis
- Rail Fence and Vigenere cipher decoding
- Image header investigation
- File signature analysis
- Hidden-message investigation
- Password hash lookup
- CTF problem-solving

## Reflection
This lab introduced several techniques for examining encoded and hidden information. It demonstrated how CyberChef combines operations into recipes and how recognizing patterns, file formats, and cipher characteristics can help solve security challenges.

## Lab Results
The exact outputs and observations for Exercises 2-6 will be added from my completed lab work.
