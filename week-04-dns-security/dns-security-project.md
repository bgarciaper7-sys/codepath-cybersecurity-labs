# DNS Security Project: The Hunt

## Course Information

- **Course:** CodePath CYB101 - Intro to Cybersecurity
- **Unit:** 4 - DNS Security
- **Project:** Project 4, Part 3 - The Hunt
- **Environment:** Docker, Linux, Bash
- **Tools:** dig, grep, awk, cut, CyberChef, dnsmasq
- **Status:** Completed

## Project Objective

Investigate DNS query logs to identify suspicious activity, determine the compromised workstation, verify the command-and-control (C2) domain, and recover data hidden inside DNS queries.

## Investigation Environment

The project simulated a security investigation involving Northwind Bank.

The provided DNS log dataset contained normal network activity, suspicious DNS queries, and a decoy domain.

**DNS log location:**

`/opt/dns-lab/logs/queries.log`

## Step 1: Analyze DNS Query Logs

I investigated DNS queries to identify unusual activity among legitimate network traffic.

Normal DNS queries included services such as:

- duckduckgo.com
- archive.ubuntu.com
- s3.amazonaws.com
- outlook.office365.com

During the investigation, I identified an unusual DNS query originating from `10.10.5.41`.

The query contained an encoded-looking subdomain beneath `sync.cdn-telemetry.test`.

### Commands Used

Filter queries from the suspicious workstation:

```bash
grep 'from 10.10.5.41' /opt/dns-lab/logs/queries.log
```

Filter queries targeting the suspected C2 domain:

```bash
grep 'sync.cdn-telemetry.test' /opt/dns-lab/logs/queries.log
```

## Step 2: Identify Suspicious DNS Patterns

I identified four suspicious DNS queries originating from the same workstation.

| Time | Observation |
|---|---|
| 08:56:21 | First suspicious DNS query |
| 08:57:36 | Second suspicious DNS query |
| 08:59:01 | Third suspicious DNS query |
| 08:59:49 | Fourth suspicious DNS query |

### Indicators of Suspicious Activity

- Repeated DNS queries from the same workstation
- Changing encoded-looking subdomains
- Multiple queries targeting the same parent domain
- Suspicious activity concentrated within a short period

**Compromised workstation:** `10.10.5.41`

**Observed duration:** 3 minutes and 28 seconds

These characteristics suggested a possible DNS data-exfiltration channel.

## Step 3: Verify the C2 Domain

I investigated the suspected command-and-control domain using:

```bash
dig @localhost A sync.cdn-telemetry.test +short
```

**Observed DNS response:**

```text
198.51.100.13
```

I then used CodePath's built-in validator:

```bash
check-c2 sync.cdn-telemetry.test
```

**Verification result:**

```text
CORRECT - that's the C2 domain the compromised client was beaconing to.
```

### Confirmed Findings

- **Compromised workstation:** `10.10.5.41`
- **C2 domain:** `sync.cdn-telemetry.test`
- **C2 IP address:** `198.51.100.13`
- **Suspicious DNS queries:** 4

## Step 4: Extract and Decode Exfiltrated Data

The suspicious DNS queries contained changing subdomain labels that resembled Base32-encoded information.

I extracted the labels using:

```bash
grep 'sync.cdn-telemetry.test' /opt/dns-lab/logs/queries.log | awk '{print $6}' | cut -d. -f1
```

I combined the four encoded chunks in chronological order and used CyberChef's **From Base32** operation to decode the data.

### Recovered Flag

```text
CYB101{dns_exfil_hidden_in_plain_sight!}
```

This confirmed that the simulated DNS queries contained encoded information.

## Step 5: Optional Stretch Challenge

I completed the optional challenge by estimating how long the exfiltration lasted and how much data could have been transferred.

### Duration

- First observed query: 08:56:21
- Last observed query: 08:59:49
- Total observed duration: 3 minutes and 28 seconds

### Estimated Data Size

The four suspicious queries each contained 16 Base32 characters.

```text
4 queries × 16 characters = 64 encoded characters

64 characters × 5 bits = 320 bits

320 bits ÷ 8 = 40 bytes
```

The encoded labels represented approximately 40 bytes of potential payload data. This is an estimate of encoded capacity rather than a measurement of the exact decoded message size.

### Recommended Detection Control

DNS anomaly monitoring could help detect repeated queries containing unusual, changing subdomains from the same workstation to a common parent domain.

This type of behavioral detection could identify suspicious DNS activity even if an attacker changed the C2 destination.

## Security Findings

| Finding | Result |
|---|---|
| Compromised workstation | 10.10.5.41 |
| Verified C2 domain | sync.cdn-telemetry.test |
| C2 IP address | 198.51.100.13 |
| Suspicious DNS queries | 4 |
| Observed duration | 3 minutes, 28 seconds |
| Encoding method | Base32 |
| Validation | check-c2 passed |

## Defensive Recommendations

1. Monitor DNS queries for unusual patterns.
2. Investigate repeated high-entropy subdomains.
3. Establish baselines for normal DNS activity.
4. Restrict unauthorized external DNS resolution.
5. Correlate DNS logs with endpoint security alerts.
6. Investigate suspicious workstation behavior.

## Personal Reflection

This project helped me understand how attackers can exploit the trust computers place in DNS resolvers.

During the lab, I observed how changing a DNS record could redirect a fictional banking domain to a simulated phishing page without changing the hostname.

I also learned how DNS exfiltration can blend into normal network activity.

The most important clue was not a single unusual query, but a repeated pattern of changing, encoded-looking subdomains from the same workstation.

By using grep, dig, check-c2, and CyberChef, I practiced identifying suspicious activity, verifying command-and-control infrastructure, and recovering encoded information.

This project strengthened my understanding of DNS security, threat detection, log analysis, and incident response.

## References

- [CodePath DNS Security Lab](https://github.com/codepath/opencyber-dns-lab)
- [CyberChef](https://gchq.github.io/CyberChef/)
