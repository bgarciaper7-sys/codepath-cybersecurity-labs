# DNS Security Lab: DNS Resolution and Resolver Security

## Course Information

- **Course:** CodePath CYB101 - Intro to Cybersecurity
- **Unit:** 4 - DNS Security
- **Lab:** DNS Security Lab, Parts 0–2
- **Environment:** Docker, Linux, Bash
- **Tools:** dig, dnsmasq, curl, grep, tail, Docker
- **Source:** https://github.com/codepath/opencyber-dns-lab

## Objective

Investigate how DNS resolution works, identify how DNS responses can be manipulated, and explore defensive DNS resolver configurations.

## Part 0: Environment Setup

Completed the CodePath DNS Security Lab setup using Docker.

The lab provided a Linux terminal and a local DNS resolver for investigating DNS responses.

### Important Lab Files

| File | Purpose |
|---|---|
| `/opt/dns-lab/dnsmasq.lab.conf` | DNS resolver configuration |
| `/opt/dns-lab/captured.log` | Simulated captured credentials |
| `/opt/dns-lab/logs/queries.log` | DNS query log dataset |

### DNS Query Syntax

```bash
dig @localhost example.com
```

The `dig` utility sends a DNS query to the specified resolver.

## Part 1: Investigating DNS Responses

Investigated how DNS queries are resolved and how an attacker-controlled response could redirect users.

### Lab Domain

```text
login.northwind-bank.test
```

The lab used a simulated banking domain to demonstrate the security implications of DNS manipulation.

### Security Concepts

- DNS translates domain names into IP addresses.
- DNS resolvers return records that clients use to locate services.
- Malicious DNS responses can redirect users to unintended destinations.
- DNS manipulation can support phishing and credential theft.

## Part 2: DNS Resolver Security

Investigated DNS resolver behavior and configuration as part of the defensive exercises.

### DNS Investigation

Used `dig` to inspect responses from the local resolver.

Example command:

```bash
dig @localhost login.northwind-bank.test
```

### DNS Resolver Configuration Analysis

During Part 2, I examined the DNS resolver configuration
file located at:

`/opt/dns-lab/dnsmasq.lab.conf`

The lab simulated DNS poisoning by modifying the DNS
record for a fictional banking login domain.

**Original DNS configuration:**

```bash
host-record=login.northwind-bank.test,203.0.113.10
```

The original record pointed to the simulated legitimate
Northwind Bank login server.

**Modified DNS configuration:**

```bash
#host-record=login.northwind-bank.test,203.0.113.10
host-record=login.northwind-bank.test,127.0.0.1
```

The original DNS record was disabled, and a replacement
record redirected the login domain to the local container.

## Simulated Phishing and Credential Capture

After modifying the DNS resolver configuration, I investigated the simulated banking login page hosted inside the Docker environment.

### HTTP Investigation

Used curl to retrieve the fictional banking login page:

```bash
curl http://login.northwind-bank.test:8080/
```

The command returned HTML content for the simulated Northwind Bank login page.

I also accessed the page through the Docker port mapping:

`http://localhost:8088`

The page contained a login form with a User ID field, password field, and Sign In button.

### Credential Capture Verification

Submitted fictional test credentials through the lab's simulated login page.

Inspected the credential-capture log using:

```bash
cat /opt/dns-lab/captured.log
```

**Observed result:**

- Three simulated credential submissions were recorded.
- The capture log included timestamps and source IP addresses.
- The recorded source address was `172.17.0.1`.

This demonstrated how a deceptive login page can collect submitted credentials.

The browser preview used the Docker port mapping, while the earlier curl request separately confirmed that the modified DNS hostname reached the simulated web server.

## DNS Log Investigation

Investigated DNS resolver activity to identify evidence of the modified DNS response.

### Commands Used

```bash
tail -n 30 /opt/dns-lab/dnsmasq-runtime.log
```

```bash
grep 'login.northwind-bank.test' /opt/dns-lab/dnsmasq-runtime.log
```

```bash
grep '127.0.0.1' /opt/dns-lab/dnsmasq-runtime.log
```

### Incident Timeline

| Time (Oct 8) | Event | Finding |
|---|---|---|
| 19:35:04 | Original DNS response | 203.0.113.10 |
| 19:36:14 | DNS service terminated | SIGTERM |
| 19:36:39 | DNS service restarted | Modified configuration loaded |
| 19:40:03 | Modified DNS response | 127.0.0.1 |
| 19:44:35 | Additional DNS response | 127.0.0.1 |
| 19:54–19:56 | Credential submissions | Three simulated captures |

### Evidence

**Original DNS response:**

```text
config login.northwind-bank.test is 203.0.113.10
```

**Modified DNS response:**

```text
config login.northwind-bank.test is 127.0.0.1
```

The resolver logs confirmed that the same hostname returned different IP addresses before and after the configuration change.

### Security Analysis

This investigation demonstrated how DNS manipulation can redirect network traffic toward an unintended destination.

By comparing resolver logs with credential-capture records, I practiced log correlation and incident timeline reconstruction.

I also learned to distinguish between a DNS query originating from `127.0.0.1` and a DNS response returning `127.0.0.1`.

The unexpected DNS response was the relevant indicator of the simulated DNS hijack.

### DNS Security Findings

| IP Address | Role |
|---|---|
| `203.0.113.10` | Simulated legitimate login server |
| `127.0.0.1` | Local container used for DNS redirection |
| `203.0.113.25` | Simulated mail server |
| `198.51.100.13` | Simulated telemetry destination |

### Attack Explanation

This exercise demonstrated how modifying DNS resolver
configuration can redirect a legitimate-looking domain
to an unintended destination.

The lab's simulated attacker-controlled destination
hosted a lookalike login page on port 8080.

This type of manipulation illustrates how DNS
redirection can contribute to phishing and credential
theft attacks.

### Defensive Lessons

- Protect DNS resolver configuration from unauthorized changes.
- Monitor DNS records for unexpected modifications.
- Verify DNS responses against expected infrastructure.
- Restrict administrative access to DNS services.
- Investigate unexpected redirection of authentication domains.


### DNS Redirection Verification

After modifying the DNS resolver configuration, I verified the DNS response using:

```bash
dig @localhost login.northwind-bank.test +short
```

**Observed output:**

```text
127.0.0.1
```

The result confirmed that the local DNS resolver returned the modified address instead of the simulated legitimate server address (`203.0.113.10`).

This demonstrated how DNS configuration manipulation can redirect a domain to an unintended destination.

## Key Takeaways

- DNS integrity is important for secure network communication.
- DNS troubleshooting requires examining both queries and responses.
- Resolver configuration is an important security control.
- Unexpected DNS results should be investigated before being trusted.
- Defensive verification helps confirm that DNS security changes are effective.

## Personal Reflection

This lab helped me understand how DNS vulnerabilities can be exploited to redirect users toward unintended websites.

By modifying the DNS resolver configuration, I observed how a fictional banking domain could be redirected to a simulated phishing page.

I also investigated credential-capture logs and DNS resolver activity to reconstruct the sequence of events.

One of my biggest takeaways was learning how to distinguish between a DNS query's source IP address and the IP address returned by the resolver.

This exercise strengthened my understanding of DNS security, phishing techniques, log analysis, and incident response.

## References

- [CodePath DNS Security Lab](https://github.com/codepath/opencyber-dns-lab)
