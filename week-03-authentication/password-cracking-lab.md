# Password Security Lab: John the Ripper

## Course Information

- **Course:** CodePath CYB101 - Intro to Cybersecurity
- **Unit:** 3 - Authentication and Password Security
- **Lab:** Password Cracking with John
- **Environment:** Docker, Linux, Bash
- **Source:** https://github.com/codepath/opencyber-password-lab

## Objective

Understand how password hashes work and practice evaluating password strength using John the Ripper.

## Tools and Technologies

- Docker Desktop
- Linux Bash terminal
- John the Ripper
- Password wordlists
- GitHub

## Part 0: Environment Setup

The lab uses a Docker container with John the Ripper and supporting utilities preinstalled.

```bash
docker run --rm -it -v password-lab-data:/home/student ghcr.io/codepath/opencyber-password-lab:latest
```

The named Docker volume allows password-cracking progress to persist between sessions.

## Part 1: Password Cracking 101

This section introduces password hashes and three password-cracking approaches.

### Single-Crack Mode

Single-crack mode generates candidate passwords using information associated with user accounts.

### Wordlist Mode

Wordlist attacks compare password hashes against guesses from a dictionary or password list.

### Incremental Mode

Incremental mode generates password guesses systematically rather than relying exclusively on a wordlist.

### Lab Verification

The exercises use three provided files:

- `part1/crack_a.txt`
- `part1/crack_b.txt`
- `part1/crack_c.txt`

Example verification command:

```bash
john --show part1/crack_c.txt
```

## Part 2: Crack a Small File

This challenge provides four password hashes with different difficulty levels.

| Account | Difficulty |
|---|---|
| Birb | Easy |
| Pupper | Medium |
| Kitty | Hard |
| Doggo | Impossible (challenge label) |

The goal is to apply password-cracking techniques with less guidance.

Verification command:

```bash
john --show part2/crack_challenge.txt
```

### My Results

- **Passwords cracked:** To verify from lab output
- **Methods used:** To document from completed lab
- **Observations:** To add from lab notes or screenshots

## Key Takeaways

- Password hashes are not the same as encrypted passwords.
- Hash cracking generally involves generating candidate passwords and comparing their hashes.
- Wordlists can quickly identify common passwords.
- Password rules help generate variations of known words.
- Incremental attacks can be more computationally expensive.
- Longer, unpredictable passwords are harder to guess.

## Security Implications

This lab demonstrates why password reuse and predictable password patterns create security risks.

Defensive practices include using unique passwords, multifactor authentication, appropriate password hashing algorithms, and secure password storage.

## References

- [CodePath Password Security Lab](https://github.com/codepath/opencyber-password-lab)
- [John the Ripper Documentation](https://www.openwall.com/john/doc/)
  