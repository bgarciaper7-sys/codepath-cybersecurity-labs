# Week 7: Shodan Reconnaissance | CodePath CYB101

## Project Overview

This lab introduced Shodan, a search engine that indexes publicly accessible internet-connected devices and services. I used Shodan to conduct passive reconnaissance, analyze service banners, identify exposed network ports, and investigate the security implications of publicly discoverable infrastructure.

I also completed two stretch challenges involving custom search filters and industrial control systems.

## Tools and Technologies

- Shodan Search Engine
- Shodan Search Filters and Reports
- HTTP and SSH Service Banners
- OpenSSH
- nginx
- SCADA and Modbus
- IoT and Industrial Control Systems

## Investigations and Findings

### 1. Samsung Smart TV

**Search query:** `Samsung Smart TV`

- Identified 2,688 matching service results.
- South Korea had the highest number of results, with 1,523.
- Port 8001 appeared in 2,611 results.
- Examined HTTP response headers and service information.

**Key takeaway:** Internet-connected devices can expose identifying information through publicly indexed network services.

### 2. Potential Website Defacement

**Search query:** `hacked by`

- Identified 49 matching results.
- Examined an HTTP 401 Unauthorized response containing a message claiming the service had been hacked.
- Learned to distinguish suspicious indicators from confirmed security incidents.

**Key takeaway:** Service banners can contain indicators of possible compromise, but additional evidence is necessary to verify an incident.

### 3. Linksys Video Cameras

**Search query:** `title:"Linksys Compact Wireless"`

- Identified 20 matching results.
- Observed publicly indexed Linksys camera web interfaces.
- Examined HTTP response codes and advertised Boa web-server information.

**Key takeaway:** Publicly discoverable camera interfaces can increase security exposure, but their presence does not prove unauthorized access is possible.

### 4. CodePath Infrastructure Reconnaissance

**Search queries:**
- `codepath.org`
- `hostname:codepath.org product:OpenSSH`

**Findings:**
- 14 matching web-service results.
- Three matching OpenSSH services.
- OpenSSH services advertised version 7.6p1 on Ubuntu.
- The SSH services were associated with Linode hosting in Richardson, Texas.
- The broader web-service report identified nginx and ports 80, 443, and 8080.

**Key takeaway:** Shodan reports help analysts understand publicly visible services, geographic distribution, software versions, and network exposure. Service-result counts do not necessarily equal unique physical hosts.

## Stretch Challenge 1: Custom Search Filters

**Search query:** `product:nginx country:US`

- Identified 15,167,308 matching results.
- Los Angeles had the highest count among the displayed cities.
- Ports 80 and 443 were the most common.

This challenge strengthened my understanding of combining search filters to investigate specific technologies and geographic regions.

## Stretch Challenge 2: Industrial Control Systems

### SCADA Investigation

**Search query:** `SCADA`

- Identified 2,885 matching results.
- China and the United States had the highest counts among the displayed countries.
- Observed a result labeled as a honeypot.

### Modbus Investigation

**Search query:** `Modbus`

- Identified 1,203 matching results.
- Port 502 appeared in 904 results.
- Observed service information identifying industrial equipment, including a power meter.

**Security implications:** Industrial control systems support physical processes and critical infrastructure. Unauthorized access could potentially disrupt operations or manipulate equipment. Strong authentication, network segmentation, access controls, and continuous monitoring are important protective measures.

## Skills Developed

- Passive reconnaissance and OSINT
- Shodan query construction
- Network port and protocol identification
- HTTP and SSH banner analysis
- Internet-facing asset discovery
- IoT security awareness
- Industrial cybersecurity fundamentals
- Security findings documentation

## Reflection

This lab helped me understand how much information about internet-connected systems can be discovered without directly interacting with those systems.

I practiced analyzing network ports, service banners, software versions, and geographic information. I also learned that publicly indexed services are not necessarily vulnerable and that reconnaissance findings must be interpreted carefully.

The industrial control systems stretch challenge was particularly interesting because it demonstrated how cybersecurity risks can extend beyond information systems to physical infrastructure and operational technology.

All investigations were limited to publicly indexed Shodan information. No authentication attempts, exploitation, or direct interaction with third-party devices were performed.

## Screenshots & Evidence

The following screenshots document my Shodan reconnaissance investigations and findings.

### Required Lab Investigations

| Investigation | Evidence |
|---|---|
| Samsung Smart TV | [View Screenshot](screenshots/01-samsung-smart-tv.png) |
| Potential Website Defacement | [View Screenshot](screenshots/02-hacked-websites.png) |
| Linksys Video Cameras | [View Screenshot](screenshots/03-linksys-cameras.png) |
| CodePath OpenSSH Discovery | [View Screenshot](screenshots/04-codepath-openssh.png) |
| CodePath OpenSSH Report | [View Screenshot](screenshots/05-codepath-openssh-report.png) |
| CodePath Infrastructure Report | [View Screenshot](screenshots/06-codepath-full-report.png) |

### Stretch Challenges

| Investigation | Evidence |
|---|---|
| Custom nginx Search Query | [View Screenshot](screenshots/07-custom-nginx-query.png) |
| SCADA Reconnaissance | [View Screenshot](screenshots/08-scada-search.png) |
| Modbus Reconnaissance | [View Screenshot](screenshots/09-modbus-search.png) |

**Note:** These screenshots document publicly indexed Shodan search results collected for educational purposes. The results do not establish that any identified system is vulnerable or compromised.