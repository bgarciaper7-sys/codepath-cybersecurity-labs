# codepath-cybersecurity-labs
Hands-on cybersecurity labs and projects from CodePath CYB101, covering encryption, authentication, network security, threat analysis, and defensive security.

## Projects & Labs

This repository contains hands-on cybersecurity labs, technical investigations, and projects completed as part of CodePath CYB101.

| Week | Topic | Labs & Projects |
|---|---|---|
| 1 | Security Mindset | [View Week 1](week-01-security-mindset/) |
| 2 | Encryption & SSH Security | [View Week 2](week-02-encryption/) |
| 3 | Authentication & Password Security | [View Week 3](week-03-authentication/) |
| 4 | DNS & Network Security | [View Week 4](week-04-dns-security/) |
| 5 | Malware Detection | [View Week 5](week-05-malware-detection/) |

## Project Highlights

### Week 1: Security Mindset & CyberChef

Completed introductory cybersecurity exercises involving security analysis, CyberChef, and capture-the-flag (CTF) challenges.

- Practiced identifying security threats, vulnerabilities, and risks.
- Used CyberChef to investigate encoded information.
- Completed 11 CTF challenges involving trivia, reconnaissance, and cryptography.
- Developed foundational problem-solving and cybersecurity investigation skills.

**Project Documentation:**
- [CyberChef Lab](week-01-security-mindset/cyberchef-lab.md)
- [CyberChef CTF Project](week-01-security-mindset/cyberchef-ctf-project.md)

### Week 2: Encryption & SSH Security

Completed a Linux-based security investigation involving SSH authentication logs and suspicious system activity.

- Investigated SSH authentication events and system logs.
- Identified suspicious root login activity from `203.0.113.66`.
- Investigated the malicious `update-agent.sh` script.
- Identified a suspicious external communication destination.
- Practiced documenting security findings and incident-response recommendations.

**Lab Documentation:**
- [Terminal & SSH Security Lab](week-02-encryption/terminal-ssh-lab.md)

### Week 3: Authentication & Password Security

Completed password security exercises using Docker and John the Ripper.

- Investigated password hashing and password-cracking techniques.
- Practiced dictionary attacks, rule-based attacks, and mask attacks.
- Analyzed a simulated dataset containing 1,000 password hashes.
- Successfully recovered 262 passwords (26.2%) in the simulated password-cracking challenge.
- Explored how password complexity and predictable patterns affect password security.

**Project Documentation:**
- [Password Cracking Lab](week-03-authentication/password-cracking-lab.md)
- [Password Crackathon Project](week-03-authentication/password-crackathon-project.md)

### Week 4: DNS & Network Security

Completed the DNS Security Lab and Project 4: The Hunt.

- Investigated DNS resolver manipulation and simulated phishing.
- Analyzed DNS logs to identify suspicious workstation activity.
- Verified a command-and-control domain using `dig` and `check-c2`.
- Recovered Base32-encoded information using CyberChef.
- Completed an optional breach-size analysis and recommended DNS anomaly monitoring.


**Project Documentation:**
- [DNS Security Lab](week-04-dns-security/dns-security-lab.md)
- [DNS Security Project: The Hunt](week-04-dns-security/dns-security-project.md)

### Week 5: Malware Detection

Completed the Malware Detection Lab using an Azure Ubuntu VM, Linux command-line tools, and VirusTotal.

- Investigated four EICAR antivirus test files.
- Calculated and compared SHA-1 file hashes.
- Analyzed YARA signature matches and VirusTotal reports.
- Compared antivirus detection results for original and compressed files.
- Observed 62 malicious detections for the original EICAR file, compared with 11 for the ZIP archive and 16 for the nested ZIP.
- Learned why antivirus detection counts require context and why fewer detections do not necessarily indicate a safe file.

**Lab Documentation:**
- [Malware Detection Lab](week-05-malware-detection/malware-detection-lab.md)

## Technical Skills

- **Security Tools:** CyberChef, John the Ripper, dnsmasq, dig, VirusTotal CLI, YARA signature analysis
- **Development Tools:** Docker, Git, GitHub, VS Code
- **Command Line:** Linux Bash, PowerShell, SSH, grep, awk, cut, curl, wget, ls, sha1sum
- **Security Concepts:** Cryptography, authentication, password hashing, DNS security, DNS poisoning, DNS exfiltration, command-and-control (C2) detection, incident investigation
- **Security Analysis:** Log analysis, threat detection, incident timeline reconstruction, Base32 decoding, file hashing, malware signature analysis, antivirus detection comparison
- **Documentation:** Technical reporting, security findings, defensive recommendations

## Project Performance

This repository documents my hands-on coursework and cybersecurity projects completed through CodePath CYB101: Intro to Cybersecurity.

| Week | Topic | Project Score | Grade |
|---|---|---:|---:|
| 1 | Security Mindset | 20/12 | 166.7% |
| 2 | Encryption | 23/20 | 115% |
| 3 | Authentication and Password Security | 20/20 | 100% |
| 4 | DNS and Network Security | 23/20 | 115% |
| **Total** | **Completed Graded Projects** | **86/72** | **119.4%** |


**Highlights:**

- Earned full credit or higher on all four graded projects.
- Earned 14 points above the combined maximum through additional credit.
- Completed Week 4's DNS Security Lab and Project 4: The Hunt, including the optional stretch challenge.
- Completed Week 5's Malware Detection Lab, analyzing EICAR test files, SHA-1 hashes, YARA signatures, and VirusTotal detection results.
- Identified and verified a simulated command-and-control domain through DNS log analysis.
- Recovered Base32-encoded information using CyberChef.
- Applied cybersecurity concepts through hands-on investigations, security tools, and technical documentation.

*Project performance reflects points earned on the first four graded assignments, including extra credit, rather than an overall course grade. Week 5's project grade is not yet included.*

## Learning Objectives

Through this repository, I aim to:

- Build practical cybersecurity skills through hands-on labs.
- Understand how attackers exploit security weaknesses.
- Apply defensive security principles to real-world scenarios.
- Strengthen my knowledge of network security, authentication, and cryptography.
- Document technical investigations and communicate security findings clearly.

## About This Repository

This portfolio is an ongoing record of my cybersecurity learning journey through CodePath CYB101: Intro to Cybersecurity.

All security testing is performed in authorized educational lab environments.
