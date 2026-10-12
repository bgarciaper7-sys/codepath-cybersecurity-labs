# Week 4: DNS Security

## Course Information

- **Course:** CodePath CYB101 - Intro to Cybersecurity
- **Unit:** 4 - DNS Security
- **Status:** Completed

## Overview

This unit explored how Domain Name System (DNS) resolution works, how attackers can manipulate DNS responses, and how security analysts investigate suspicious DNS activity.

I completed the DNS Security Lab (Parts 0–2) and Project 4: The Hunt (Part 3).

## Completed Activities

### DNS Security Lab: Parts 0–2

- Configured and investigated a DNS resolver using Docker and dnsmasq.
- Analyzed DNS records using dig.
- Simulated DNS redirection involving a fictional banking domain.
- Investigated a simulated phishing page and credential-capture logs.
- Examined DNS resolver logs to identify unexpected responses.
- Reconstructed an incident timeline.

[View DNS Security Lab](dns-security-lab.md)

### Project 4: The Hunt

- Investigated DNS query logs for suspicious activity.
- Identified a compromised workstation.
- Detected repeated queries containing Base32-encoded information.
- Verified the command-and-control domain using dig and check-c2.
- Recovered the encoded flag using CyberChef.
- Completed the optional breach-size analysis.

[View DNS Security Project](dns-security-project.md)

## Technical Skills Developed

- DNS resolution and record analysis
- DNS resolver configuration
- Linux command-line investigation
- Log filtering and correlation
- DNS anomaly detection
- Command-and-control investigation
- Base32 decoding
- Digital forensics
- Incident response

## Tools Used

- Docker
- Linux / Bash
- dnsmasq
- dig
- grep
- awk
- cut
- curl
- CyberChef

## Key Takeaways

DNS is essential to network communication, but attackers can abuse the trust placed in DNS responses.

This unit demonstrated how DNS manipulation can redirect users toward unintended destinations and how encoded data can be hidden inside DNS queries.

By investigating resolver logs, identifying suspicious patterns, and validating findings, I gained practical experience with both DNS attack techniques and defensive security analysis.

## References

- [CodePath DNS Security Lab](https://github.com/codepath/opencyber-dns-lab)
