# Project 3: Password Crack-a-thon

## Project Overview

**Course:** CodePath CYB101 - Intro to Cybersecurity  
**Unit:** 3 - Authentication and Password Security  
**Project:** Password Crack-a-thon  
**Environment:** Docker, Linux, Bash  
**Primary Tool:** John the Ripper

**Source:** https://github.com/codepath/opencyber-password-lab

## Project Objective

Investigate a simulated password breach containing 1,000 password hashes and apply password-cracking techniques to evaluate password security.

The project required cracking at least 250 passwords using wordlists, built-in rulesets, and custom masks.

## Project Results

| Metric | Result |
|---|---|
| Total password hashes | 1,000 |
| Passwords cracked | 262 |
| Percentage cracked | 26.2% |
| Required minimum | 250 |
| Requirement achieved | Yes |

I successfully exceeded the minimum requirement by 12 passwords.

## Tools and Technologies

- Docker Desktop
- Linux Bash
- John the Ripper
- Password wordlists
- Built-in password rulesets
- Custom password masks

## Investigation Methodology

### 1. Environment Setup

Used a Docker container containing John the Ripper and the password security lab files.

```bash
docker run --rm -it -v password-lab-data:/home/student ghcr.io/codepath/opencyber-password-lab:latest
```


### 2. Wordlist Attack

Used the RockYou password wordlist to test common
and previously exposed passwords against the
simulated leaked password database.

**Command used:**

```bash
john --wordlist=wordlists/rockyou.txt part3/password_leak.txt
```

**Explanation:**
- `--wordlist` specifies the password dictionary.
- `rockyou.txt` contains commonly used passwords.
- `part3/password_leak.txt` contains the target hashes.

**Security takeaway:**
Common passwords can be vulnerable to dictionary
attacks, even when stored as hashes.

### 3. Built-in Ruleset Attack

Applied John the Ripper's Jumbo ruleset to
generate password variations from a wordlist.

**Command used:**

```bash
john --wordlist=wordlists/lower.lst --rules=Jumbo part3/password_leak.txt
```

**Explanation:**
- `lower.lst` provides the starting password candidates.
- `--rules=Jumbo` applies a predefined collection
  of password transformation rules.
- The rules generate additional password guesses
  based on the original dictionary entries.

**Security takeaway:**
Simple password modifications may not provide
adequate protection against rule-based attacks.

### 4. Custom Mask Attack

Used a custom mask to target passwords consisting
of exactly five lowercase letters.

**Command used:**

```bash
john --mask=?l?l?l?l?l part3/password_leak.txt
```

**Explanation:**
- `--mask` defines the password structure.
- `?l` represents one lowercase letter.
- Five `?l` placeholders target five-character
  lowercase passwords.

**Security takeaway:**
Short passwords with predictable character
patterns can be systematically guessed.

## Verification

The project uses the following command to display recovered passwords and the total cracked count:

```bash
john --show part3/password_leak.txt
```

**Verified project result:** 262 passwords cracked.

## Security Findings

- Predictable passwords are vulnerable to wordlist attacks.
- Password rules can expand the effectiveness of dictionary attacks.
- Short passwords are easier to target with exhaustive guessing.
- Password complexity requirements alone do not guarantee strong security.
- Password length and unpredictability are important defensive measures.

## Defensive Recommendations

1. Encourage long, unique passwords.
2. Implement multifactor authentication.
3. Use password managers to generate strong passwords.
4. Store passwords using appropriate salted password-hashing algorithms.
5. Screen newly created passwords against known compromised-password lists.

## Personal Reflection

This project provided practical experience using John the Ripper to evaluate password security.

By recovering 262 passwords from a simulated leaked database, I demonstrated how wordlists, rulesets, and password patterns can expose weak credentials.

The project reinforced the importance of secure authentication practices and helped me better understand how password-cracking techniques relate to defensive cybersecurity.

## References

- [CodePath Password Security Lab](https://github.com/codepath/opencyber-password-lab)
- [John the Ripper Documentation](https://www.openwall.com/john/doc/)
