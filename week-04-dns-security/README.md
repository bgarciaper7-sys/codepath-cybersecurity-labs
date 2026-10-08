# Week 4: DNS Security

## Overview

In Unit 4 of CodePath CYB101: Intro to Cybersecurity, I explored Domain Name System (DNS) security and how DNS configuration affects the integrity of network communications.

Through a hands-on Docker lab, I practiced DNS queries, examined resolver behavior, and investigated how DNS responses can be manipulated.

## Topics Covered

- Domain Name System (DNS)
- DNS resolution and queries
- DNS resolvers and configuration
- DNS spoofing and poisoning
- DNS response integrity
- DNS security vulnerabilities
- Defensive DNS configuration

## Tools and Technologies

- Docker Desktop
- Linux Bash terminal
- `dig`
- `dnsmasq`
- DNS configuration files
- Visual Studio Code
- Git and GitHub

## Hands-On Labs and Projects

### DNS Security Lab: Parts 0–2

**Status:** Completed

Completed the CodePath DNS Security Lab using a Docker-based environment.

Activities included:

- Setting up the DNS Security Lab environment
- Querying a local DNS resolver
- Investigating DNS responses
- Examining DNS resolver configuration
- Exploring DNS security weaknesses
- Practicing defensive DNS troubleshooting

[View DNS Security Lab](dns-security-lab.md)

### Project 4: DNS Security Challenge

**Status:** Not started

Part 3 will involve applying the concepts learned in the DNS Security Lab to a new cybersecurity challenge.

Project findings, commands, and results will be documented after completion.

## Key Concepts

### DNS Resolution

DNS translates domain names into IP addresses, allowing devices to locate network services.

### DNS Spoofing

DNS spoofing involves providing false DNS information that may redirect users to unintended destinations.

### DNS Cache Poisoning

DNS cache poisoning occurs when incorrect DNS records are introduced into a resolver's cache, potentially affecting subsequent queries.

### DNS Resolver Security

Secure resolver configuration helps reduce the risk of malicious redirection and unauthorized changes to DNS responses.

## Key Takeaways

- DNS is an essential component of network communication.
- Incorrect DNS responses can redirect users to unintended services.
- Resolver configuration influences how DNS queries are answered.
- DNS security requires attention to trusted responses and configuration.
- DNS troubleshooting tools can help identify suspicious DNS behavior.

## Technical Skills Developed

- DNS query analysis
- Linux command-line troubleshooting
- Docker lab environments
- DNS resolver investigation
- Network security fundamentals
- Technical documentation

## References

- [CodePath DNS Security Lab](https://github.com/codepath/opencyber-dns-lab)

## Progress

- [x] Part 0: Lab Environment Setup
- [x] Part 1: DNS Security Lab
- [x] Part 2: DNS Security Lab
- [ ] Part 3: DNS Security Project
