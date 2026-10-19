# CodePath Cybersecurity Labs & Projects

Hands-on cybersecurity labs, technical investigations, and security projects completed through **CodePath CYB101: Intro to Cybersecurity**.

This repository documents my practical experience with Linux, network security, authentication, cryptography, threat detection, malware analysis, and defensive security.

## Labs & Projects

| Week | Topic | Documentation |
|---|---|---|
| 1 | Security Mindset & CyberChef | [View Week 1](week-01-security-mindset/) |
| 2 | Encryption & SSH Security | [View Week 2](week-02-encryption/) |
| 3 | Authentication & Password Security | [View Week 3](week-03-authentication/) |
| 4 | DNS & Network Security | [View Week 4](week-04-dns-security/) |
| 5 | Malware Detection & Analysis | [View Week 5](week-05-malware-detection/) |

## Project Highlights

### Week 1 — Security Mindset & CyberChef

Completed introductory cybersecurity exercises involving security analysis, CyberChef, and capture-the-flag (CTF) challenges.

- Practiced identifying security threats, vulnerabilities, and risks.
- Used CyberChef to investigate encoded information.
- Completed 11 CTF challenges involving trivia, reconnaissance, and cryptography.
- Developed foundational cybersecurity investigation and problem-solving skills.

**Documentation**
- [CyberChef Lab](week-01-security-mindset/cyberchef-lab.md)
- [CyberChef CTF Project](week-01-security-mindset/cyberchef-ctf-project.md)

### Week 2 — Encryption & SSH Security

Completed a Linux-based security investigation involving SSH authentication logs and suspicious system activity.

- Investigated SSH authentication events and system logs.
- Identified suspicious root login activity from `203.0.113.66`.
- Investigated a malicious `update-agent.sh` script.
- Identified suspicious external communication activity.
- Practiced documenting security findings and incident-response recommendations.

**Documentation**
- [Terminal & SSH Security Lab](week-02-encryption/terminal-ssh-lab.md)

### Week 3 — Authentication & Password Security

Completed password security exercises using Docker and John the Ripper.

- Investigated password hashing and password-cracking techniques.
- Practiced dictionary, rule-based, and mask attacks in an authorized environment.
- Analyzed a simulated dataset containing 1,000 password hashes.
- Recovered 262 passwords (26.2%) during the simulated challenge.
- Examined how password complexity and predictable patterns affect security.

**Documentation**
- [Password Cracking Lab](week-03-authentication/password-cracking-lab.md)
- [Password Crackathon Project](week-03-authentication/password-crackathon-project.md)

### Week 4 — DNS & Network Security

Completed the DNS Security Lab and Project 4: The Hunt.

- Investigated DNS resolver manipulation and simulated phishing.
- Analyzed DNS logs to identify suspicious activity.
- Verified a simulated command-and-control domain using `dig` and `check-c2`.
- Recovered Base32-encoded information using CyberChef.
- Completed an optional breach-size investigation.
- Recommended defensive DNS monitoring strategies.

**Documentation**
- [DNS Security Lab](week-04-dns-security/dns-security-lab.md)
- [DNS Security Project: The Hunt](week-04-dns-security/dns-security-project.md)

### Week 5 — Malware Detection & Analysis

Completed a malware detection lab and an authorized security-testing project using an Azure Ubuntu virtual machine, Linux command-line tools, MSFVenom, and VirusTotal.

**Malware Detection Lab**

- Investigated four harmless EICAR antivirus test files.
- Generated and compared SHA-1 file hashes.
- Analyzed antivirus detection results across raw, text, ZIP, and nested ZIP samples.
- Observed 62 malicious detections for the original EICAR sample, compared with 11 for ZIP and 16 for nested ZIP.
- Learned how file packaging affects hashes and how antivirus results require contextual interpretation.

**DIY Malware Project**

- Explored single and combined payload formats within an authorized educational environment.
- Investigated polymorphic XOR additive feedback encoding.
- Examined the differences between encoding and encryption.
- Generated SHA-256 fingerprints for lab-generated executable files.
- Investigated antivirus detection through VirusTotal.
- Observed that 58 of 71 security vendors flagged the single-payload executable as malicious.
- Documented technical observations, troubleshooting, and screenshots without distributing executable payloads.

**Lab Documentation**
- [Malware Detection Lab Overview](week-05-malware-detection/labs/malware-detection/README.md)
- [Detailed Malware Detection Lab](week-05-malware-detection/labs/malware-detection/malware-detection-lab.md)
- [Lab Reflection](week-05-malware-detection/labs/malware-detection/reflection.md)

**Project Documentation**
- [DIY Malware Project Overview](week-05-malware-detection/projects/diy-malware/README.md)
- [Detailed DIY Malware Walkthrough](week-05-malware-detection/projects/diy-malware/diy-malware.md)
- [Project Reflection](week-05-malware-detection/projects/diy-malware/reflection.md)

## Technical Skills

| Category | Tools and Skills |
|---|---|
| Security Tools | CyberChef, John the Ripper, VirusTotal, MSFVenom, DNS investigation tools |
| Operating Systems | Linux (Ubuntu), Windows |
| Development Tools | Docker, Git, GitHub, VS Code, Remote SSH |
| Command Line | Bash, PowerShell, `grep`, `awk`, `cut`, `dig`, `wget`, `ls`, `sha1sum`, `sha256sum` |
| Network Security | DNS, DNS poisoning, DNS exfiltration, SSH security, command-and-control investigation |
| Authentication & Cryptography | Password hashing, encryption concepts, authentication analysis, Base32 decoding |
| Malware Analysis | File signatures, file hashing, antivirus detection, executable formats, encoding concepts |
| Security Investigation | Log analysis, suspicious activity investigation, threat identification, technical reporting |
| Professional Skills | Problem-solving, technical documentation, troubleshooting, evidence-based analysis |

## Project Performance

The following scores reflect completed graded projects and earned extra credit.

| Week | Topic | Points Earned | Grade |
|---|---|---:|---:|
| 1 | Security Mindset | 20/12 | 166.7% |
| 2 | Encryption | 23/20 | 115% |
| 3 | Authentication & Password Security | 20/20 | 100% |
| 4 | DNS & Network Security | 23/20 | 115% |
| **Total** | **First Four Graded Projects** | **86/72** | **119.4%** |

*These figures reflect the first four graded projects, including extra credit, rather than an overall course grade. Week 5's project score is not yet included.*

## Key Accomplishments

- Earned full credit or higher on the first four graded projects.
- Completed hands-on investigations involving authentication, DNS security, file signatures, and antivirus analysis.
- Investigated simulated command-and-control activity and suspicious authentication events.
- Recovered 262 passwords from a simulated password-security dataset.
- Completed the Week 5 Malware Detection Lab and DIY Malware Project.
- Developed technical walkthroughs, reflections, and evidence-based documentation.
- Maintained a GitHub portfolio using version control and organized weekly project folders.

## Learning Objectives

Through this repository, I aim to:

- Strengthen practical cybersecurity and Linux command-line skills.
- Understand how vulnerabilities and malicious activity are detected and investigated.
- Apply defensive security principles to realistic scenarios.
- Develop stronger independent troubleshooting and investigation skills.
- Communicate technical findings clearly through professional documentation.
- Build a portfolio demonstrating continued technical development.

## Ethical and Responsible Security Testing

All security exercises were performed in authorized CodePath educational environments.

The repository contains documentation, observations, and permitted screenshots. It does not distribute executable malware samples, raw payloads, or sensitive credentials.

---

*This portfolio is an ongoing record of my cybersecurity learning and hands-on experience through CodePath CYB101.*