# Project 7: Threat Analysis and Shodan Automation

## Project Overview

This project was completed as part of CodePath Cybersecurity 101 (CYB101). I conducted passive reconnaissance on five publicly accessible hosts using Shodan InternetDB, researched three Common Vulnerabilities and Exposures (CVEs), and developed a Python script to automate host-information retrieval.

The objective was to understand how publicly available threat intelligence can support vulnerability research, risk assessment, and cybersecurity investigations.

## Tools and Technologies

- Python 3
- Linux (Ubuntu) and Windows PowerShell
- Shodan InternetDB API
- National Vulnerability Database (NVD)
- curl
- Visual Studio Code
- JSON and HTTP

## Part 1: Passive Host Reconnaissance

I investigated five hosts using publicly indexed Shodan InternetDB information.

| Host | IP Address | Findings |
|---|---|---|
| scanme.nmap.org | 45.33.32.156 | Apache HTTP Server, OpenSSH, and multiple associated CVEs |
| testphp.vulnweb.com | 44.228.249.3 | No indexed information available |
| testasp.vulnweb.com | 44.238.29.244 | Microsoft IIS and ASP.NET; one associated CVE |
| scanme2.nmap.org | 50.116.1.184 | Apache HTTP Server, OpenSSH, and multiple associated CVEs |
| demo.testfire.net | 65.61.137.117 | Java and Apache Tomcat identifiers; no CVEs listed |

I examined IP addresses, hostnames, software identifiers, ports, and vulnerability references.

**Important:** Shodan findings represent publicly indexed information. An associated CVE does not necessarily mean a host is currently vulnerable or exploitable.

## Part 2: CVE Research and Risk Analysis

I researched three CVEs using the National Vulnerability Database.

| CVE | Affected Technology | CVSS Score | Severity |
|---|---|---|---|
| CVE-2014-4078 | Microsoft IIS | 5.1 (CVSS v2.0) | Medium |
| CVE-2022-28614 | Apache HTTP Server | 5.3 (CVSS v3.1) | Medium |
| CVE-2021-44790 | Apache HTTP Server | 9.8 (CVSS v3.1) | Critical |

The research included reviewing vulnerability descriptions, affected software, potential security consequences, and severity ratings.

I also examined how vulnerabilities can affect confidentiality, integrity, and availability.

## Stretch Challenge: Python Shodan Automation

I developed `shodan_lookup.py`, a command-line Python script that automatically retrieves information from Shodan InternetDB.

### Features

- Accepts an IP address as a command-line argument
- Retrieves publicly indexed host information
- Displays hostnames and listed ports
- Counts associated CVEs
- Handles HTTP errors and unavailable records

### Example Usage

```bash
python shodan_lookup.py 45.33.32.156
```

### Example Output

```text
IP Address: 45.33.32.156
Hostnames: ['scanme.nmap.org']
Open Ports: [22, 80, 123]
CVE Count: 131
```

Results may change as Shodan updates its data.

### Python Concepts Practiced

- Functions and return values
- Command-line arguments
- HTTP requests and APIs
- JSON parsing
- Dictionaries and lists
- Exception handling
- Debugging and testing

## Key Takeaways

This project strengthened my ability to collect and interpret publicly available cybersecurity information, research vulnerability identifiers, and distinguish potential exposure from confirmed risk.

Developing the automation script also improved my Python programming, Linux command-line, and troubleshooting skills.

## Ethical Considerations

All reconnaissance used passive queries against publicly available Shodan InternetDB records. No exploitation, unauthorized access, or active vulnerability scanning was performed.

## References

- [Shodan InternetDB](https://internetdb.shodan.io/)
- [National Vulnerability Database](https://nvd.nist.gov/)
- [CodePath](https://www.codepath.org/)