# Week 3: Authentication and Password Security

## Overview

In Unit 3 of CodePath CYB101, I explored password security, authentication, cryptographic hashing, and techniques used to evaluate password strength.

Through hands-on exercises using Docker and John the Ripper, I practiced analyzing password hashes and identifying weaknesses in predictable passwords.

## Topics Covered

- Authentication and password security
- Cryptographic hashing and salts
- Dictionary and wordlist attacks
- Password rules and pattern-based guessing
- Brute-force and mask attacks
- Defensive password security practices

## Tools and Technologies

- Docker Desktop
- Linux Bash terminal
- John the Ripper
- RockYou password wordlist
- Git and GitHub
- Visual Studio Code

## Hands-On Labs and Projects

### Password Security Lab

Practiced password cracking techniques using John the Ripper in a Docker environment.

Activities included:
- Setting up the Docker lab
- Examining password hash files
- Using single-crack mode
- Performing wordlist attacks
- Applying password rules
- Exploring incremental and mask attacks
- Investigating four additional password challenges

[View Password Cracking Lab](password-cracking-lab.md)

### Project 3: Password Crack-a-thon

Investigated a fictional leaked password database containing 1,000 password hashes.

**Project Results:**
- Password hashes cracked: 262
- Percentage cracked: 26.2%
- Required minimum: 250
- Required threshold achieved: Yes

Techniques documented:
- Wordlist attacks using rockyou.txt
- Built-in rulesets using John the Ripper
- Custom mask attacks

[View Password Crack-a-thon Project](password-crackathon-project.md)

## Key Takeaways

- Password hashing avoids storing plaintext passwords.
- Hashes are one-way, but password guesses can be tested against them.
- Predictable passwords are vulnerable to dictionary attacks.
- Salts help protect stored password hashes.
- Password length and unpredictability improve security.
- Wordlists, rules, and masks make cracking more targeted.

## Personal Lab Notes

This unit helped me understand how attackers evaluate password security and why meeting basic password complexity requirements does not necessarily make a password secure.

I was surprised by how effective wordlists and password rules could be against predictable passwords.

During Project 3, I successfully cracked 262 out of 1,000 password hashes, exceeding the required minimum of 250.

The experience strengthened my understanding of authentication security, password hashing, and defensive password policies.

## Technical Skills Developed

- Docker container management
- Linux command-line navigation
- Password hash analysis
- John the Ripper
- Dictionary and wordlist attacks
- Password cracking rulesets
- Custom mask attacks
- Security testing and documentation
  