# CodePath Cybersecurity Labs & Projects

Hands-on cybersecurity labs, technical investigations, and security projects completed through **CodePath CYB101: Intro to Cybersecurity**.

This repository documents my practical experience with Linux, network security, authentication, cryptography, threat detection, malware analysis, steganography, and defensive security.

## Labs & Projects

| Week | Topic | Documentation |
|---|---|---|
| 1 | Security Mindset & CyberChef | [View Week 1](week-01-security-mindset/) |
| 2 | Encryption & SSH Security | [View Week 2](week-02-encryption/) |
| 3 | Authentication & Password Security | [View Week 3](week-03-authentication/) |
| 4 | DNS & Network Security | [View Week 4](week-04-dns-security/) |
| 5 | Malware Detection & Analysis | [View Week 5](week-05-malware-detection/) |
| 6 | Steganography & Digital Forensics | [View Week 6](week-06-steganography/) |
| 7 | Shodan Reconnaissance & Industrial Security | [View Week 7](week-07-shodan-reconnaissance/README.md) |

## Project Highlights

### Week 1: Security Mindset & CyberChef

Completed introductory cybersecurity exercises involving security analysis, CyberChef, and capture-the-flag (CTF) challenges.

- Practiced identifying security threats, vulnerabilities, and risks.
- Used CyberChef to investigate encoded information.
- Completed 11 CTF challenges involving trivia, reconnaissance, and cryptography.
- Developed foundational cybersecurity investigation and problem-solving skills.

**Documentation**
- [CyberChef Lab](week-01-security-mindset/cyberchef-lab.md)
- [CyberChef CTF Project](week-01-security-mindset/cyberchef-ctf-project.md)

### Week 2: Encryption & SSH Security

Completed a Linux-based security investigation involving SSH authentication logs and suspicious system activity.

- Investigated SSH authentication events and system logs.
- Identified suspicious root login activity from `203.0.113.66`.
- Investigated a malicious `update-agent.sh` script.
- Identified suspicious external communication activity.
- Practiced documenting security findings and incident-response recommendations.

**Documentation**
- [Terminal & SSH Security Lab](week-02-encryption/terminal-ssh-lab.md)

### Week 3: Authentication & Password Security

Completed password security exercises using Docker and John the Ripper.

- Investigated password hashing and password-cracking techniques.
- Practiced dictionary, rule-based, and mask attacks in an authorized environment.
- Analyzed a simulated dataset containing 1,000 password hashes.
- Recovered 262 passwords (26.2%) during the simulated challenge.
- Examined how password complexity and predictable patterns affect security.

**Documentation**
- [Password Cracking Lab](week-03-authentication/password-cracking-lab.md)
- [Password Crackathon Project](week-03-authentication/password-crackathon-project.md)

### Week 4: DNS & Network Security

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

### Week 5: Malware Detection & Analysis

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

### Week 6: Steganography & Digital Forensics

Completed a hands-on steganography lab and graded investigation involving JPEG file analysis, metadata examination, hidden-file extraction, and concealed message embedding.

**Steganography Lab: Beneath the Images**

- Investigated JPEG file structures and hexadecimal representations using CyberChef.
- Examined image metadata and file headers to identify concealed information.
- Modified JPEG height information to reveal previously hidden image content.
- Extracted an embedded ZIP archive from a JPEG and reconstructed a concealed message.
- Explored the differences between steganography, metadata, and file-format manipulation.
- Practiced evidence-based analysis to distinguish hidden information from confirmed malicious activity.

**The Artist's Message: Graded Project**

- Investigated 26 JPEG images using Linux and ExifTool.
- Filtered image metadata to identify relevant files and investigative clues.
- Used Steghide to identify and extract a password-protected hidden file.
- Interpreted concealed instructions and embedded a reply into a designated JPEG.
- Successfully verified the encoded response using the lab's built-in checker.
- Troubleshot Docker image compatibility and Windows/Linux line-ending issues.
- Documented the investigation without publishing graded challenge passwords or solutions.

**Final verification:** `CORRECT: Message encoded successfully. You win!`

**Lab Documentation**
- [Steganography Lab: Beneath the Images](week-06-steganography/labs/README.md)

**Project Documentation**
- [The Artist's Message: Steganography Investigation](week-06-steganography/projects/README.md)
- [Week 6 Overview](week-06-steganography/README.md)

### Week 7: Shodan Reconnaissance & Industrial Security

Completed the CodePath Shodan reconnaissance lab, including both optional stretch challenges, to investigate publicly indexed internet-connected devices, network services, and industrial control systems.

**Shodan Reconnaissance Lab**

- Used Shodan to investigate Samsung Smart TVs, Linksys camera interfaces, and potential website defacement indicators.
- Analyzed HTTP response headers, service banners, IP geolocation, and network ports.
- Investigated CodePath's publicly indexed infrastructure and identified three matching OpenSSH services.
- Examined OpenSSH version information, Ubuntu operating-system details, and cloud-hosting information.
- Generated Shodan reports to analyze service distributions and distinguish indexed service results from unique hosts.
- Practiced interpreting reconnaissance findings without assuming that publicly exposed services were vulnerable.

**Stretch Challenge: Custom Search Queries**

- Constructed a filtered Shodan query using `product:nginx country:US`.
- Analyzed over 15 million matching service results.
- Examined geographic distribution and common web-service ports, including 80 and 443.

**Stretch Challenge: Industrial Control Systems**

- Investigated SCADA and Modbus services using Shodan.
- Identified port 502 as a common Modbus TCP service port.
- Examined publicly indexed industrial equipment descriptions, including power-meter information.
- Identified a honeypot result and learned why search matches do not necessarily represent production systems.
- Evaluated potential cybersecurity risks affecting operational technology and critical infrastructure.

**Key Skills:** OSINT, passive reconnaissance, Shodan search filters, service-banner analysis, OpenSSH, IoT security, SCADA, Modbus, and industrial cybersecurity.

**Lab Documentation**

- [Week 7: Shodan Reconnaissance Lab](week-07-shodan-reconnaissance/README.md)
- [Week 7: Screenshots and Evidence](week-07-shodan-reconnaissance/README.md#screenshots--evidence)

## Technical Skills

| Category | Tools and Skills |
|---|---|
| Security Tools | CyberChef, John the Ripper, VirusTotal, MSFVenom, ExifTool, Steghide, Shodan, DNS investigation tools |
| Operating Systems | Linux (Ubuntu), Windows |
| Development Tools | Docker, Git, GitHub, VS Code, Remote SSH |
| Command Line | Bash, PowerShell, `grep`, `awk`, `cut`, `dig`, `wget`, `ls`, `cat`, `echo`, `sha1sum`, `sha256sum` |
| Network Security | DNS, DNS poisoning, DNS exfiltration, SSH security, command-and-control investigation, network ports and protocols |
| Authentication & Cryptography | Password hashing, encryption concepts, authentication analysis, Base32 decoding |
| Malware Analysis | File signatures, file hashing, antivirus detection, executable formats, encoding concepts |
| Digital Forensics & Steganography | JPEG structure analysis, hexadecimal inspection, metadata filtering, hidden-file extraction, steganographic embedding |
| Reconnaissance & OSINT | Shodan search queries, internet-facing asset discovery, search filters, service-banner analysis, IP geolocation, technology identification |
| Industrial Cybersecurity | SCADA, Modbus TCP, operational technology (OT), industrial control systems (ICS), critical infrastructure security awareness |
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

*These figures reflect the first four graded projects, including extra credit, rather than an overall course grade. Weeks 5 and 6 are not included because their final project scores have not been recorded here.*

## Key Accomplishments

- Earned full credit or higher on the first four graded projects.
- Completed hands-on investigations involving authentication, DNS security, malware detection, and steganography.
- Investigated simulated command-and-control activity and suspicious authentication events.
- Recovered 262 passwords from a simulated password-security dataset.
- Completed the Week 5 Malware Detection Lab and DIY Malware Project.
- Completed the Week 6 Steganography Lab and successfully verified The Artist's Message project.
- Practiced digital forensic techniques using CyberChef, ExifTool, and Steghide.
- Troubleshot Docker container compatibility and cross-platform execution issues.
- Developed technical walkthroughs, reflections, and evidence-based documentation.
- Maintained an organized GitHub portfolio using version control and weekly project folders.
- Completed the Week 7 Shodan Reconnaissance Lab, including both optional stretch challenges involving custom search filters and industrial control systems.
- Conducted passive reconnaissance of internet-facing services, analyzed OpenSSH and HTTP banners, and investigated SCADA and Modbus exposure using Shodan.

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

The repository contains documentation, observations, and permitted screenshots. It does not distribute executable malware samples, raw payloads, sensitive credentials, or graded challenge passwords and solutions.

---

*This portfolio is an ongoing record of my cybersecurity learning and hands-on experience through CodePath CYB101.*git 