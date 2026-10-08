# Terminal + SSH Security Lab

## Course Information
- Course: CodePath CYB101 - Intro to Cybersecurity
- Unit: 2
- Lab: Terminal + SSH
- Environment: Docker, Linux, Bash
- Source: https://github.com/codepath/opencyber-terminal-lab

## Objective

Develop hands-on experience navigating Linux systems,
authenticating through SSH, investigating suspicious
activity, and performing basic incident response.

## Tools and Technologies

- Docker Desktop
- Linux / Bash
- OpenSSH
- GitHub
- Linux command-line utilities

## Part 0: Environment Setup

The lab used a disposable Docker container to simulate
a Linux workstation and two SSH-accessible server
accounts.

Lab initialization command:

```bash
docker run -it --rm ghcr.io/codepath/opencyber-terminal-lab:latest
```

The environment provided a student workstation,
SSH authentication keys, and simulated servers.

## Part 1: Linux Fundamentals and SSH

### Linux Commands

| Command | Purpose |
|---------|---------|
| whoami | Identify the current user |
| id | Display user and group information |
| pwd | Display the working directory |
| ls -la | List files, including hidden files |
| cd | Navigate directories |
| cat | Read file contents |
| tree | Display directory structure |
| grep -rn | Search files for text |
| find | Locate files |
| sudo | Run commands with elevated privileges |

### SSH Key Authentication

The lab demonstrated public-key authentication
for remote access.

Example:

```bash
ssh -i ~/keys/webadmin_key webadmin@localhost
```

Key-based authentication allows an authorized user
to connect without entering an account password.

Security lesson:
Private keys must be protected, and unnecessary
password authentication should be disabled.

## Part 2: Server Investigation and Triage

### Investigation

The webadmin exercise involved examining an
unfamiliar Linux environment and identifying
potentially suspicious files and activity.

Investigation techniques included:

1. Inspecting directory structures.
2. Examining hidden files.
3. Reading configuration and log files.
4. Investigating suspicious scheduled tasks.
5. Correlating indicators across files and logs.
6. Documenting findings before removing threats.

### Suspicious Scheduled Task

The exercise described a malicious cron job
disguised as a routine update check.

The job contacted an external IP address
at regular intervals.

This demonstrated how scheduled tasks can be
abused to establish persistence.

### Incident Response Principles

- Preserve evidence before deleting files.
- Correlate suspicious activity with logs.
- Investigate indicators of compromise.
- Use administrative privileges carefully.
- Verify the system state after remediation.

## Part 3: Independent Security Challenge

### Scenario

The deploy server contained a suspicious file
disguised as a legitimate helper script.

The objective was to investigate the server,
identify the threat, document evidence, and
remove the malicious artifact.

### Finding

Suspected malicious file:

`update-agent.sh`

Evidence examined:
- Script behavior
- References to an external address
- Authentication logs
- Related system files

The investigation linked suspicious script
behavior to evidence found elsewhere on the box.

### Security Analysis

The lab demonstrated the importance of examining
scripts before execution and correlating evidence
from multiple sources.

An unfamiliar script should not be trusted solely
because its filename resembles a legitimate
administrative tool.

### Remediation

The intended response was to document the
malicious artifact and its associated indicator
before removing the file.

Verification status:
To confirm from original lab results.

## Skills Developed

- Linux command-line navigation
- SSH public-key authentication
- Filesystem investigation
- Log analysis
- Indicator-of-compromise correlation
- Suspicious script identification
- Basic incident response
- Security documentation

## Key Takeaways

This lab strengthened my understanding of how
security analysts investigate unfamiliar systems.

I learned the importance of examining evidence
before making changes, identifying suspicious
behavior across multiple files, and documenting
findings during incident response.

## Future Improvements

- Practice reviewing Linux authentication logs.
- Learn additional persistence mechanisms.
- Explore SSH hardening techniques.
- Practice writing structured incident reports.


## Verified Investigation Findings

### Initial Access

Analysis of auth.log revealed:
- A failed root password authentication attempt
- A successful root password login from the same IP
- Source IP: 203.0.113.66

This indicated that the attacker obtained root access
through password-based SSH authentication.

### Malicious File Identified

File: update-agent.sh

Indicator of compromise:
cdn-analytics.top

The script repeatedly downloaded content from:

http://cdn-analytics.top/collect

It then piped the downloaded content directly
into a shell for execution.

### Evidence Correlation

I searched for the suspicious domain using:

```bash
grep -rn "cdn-analytics.top" .
```

The search identified matching references in:
- update-agent.sh
- logs/access.log

The access log contained repeated requests at
one-minute intervals, supporting the conclusion
that the script executed periodically.

### Challenge Verification

The lab's built-in verification confirmed:

CORRECT - 'update-agent.sh' is the malicious file.

I documented the filename and associated domain
in my investigation findings.

### SSH Key Authentication Challenge

I also completed the optional challenge to
generate and configure my own SSH key pair.

Commands used:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

After configuring the keys, I successfully
authenticated to the deploy account using
the new private key without a password.

### Security Recommendations

1. Disable SSH password authentication.
2. Restrict direct root login.
3. Require public-key authentication.
4. Monitor authentication logs.
5. Investigate unauthorized scripts and tasks.
6. Apply least-privilege access controls.

## Project Outcome

Completed the required investigation and
optional SSH key challenge.

Demonstrated practical experience in Linux
security, SSH authentication, log analysis,
threat identification, and incident response.


## Defensive Recommendations
- Review unexpected scripts and scheduled tasks.
- Monitor authentication logs for unauthorized access.
- Restrict SSH access to authorized users.
- Apply least-privilege permissions.
- Investigate suspicious outbound connections.
