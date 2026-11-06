# Project 7: Threat Analysis Reflection

## What I Learned

Through this project, I learned how to use Shodan InternetDB for passive reconnaissance and how to research Common Vulnerabilities and Exposures (CVEs) using the National Vulnerability Database.

I practiced interpreting hostnames, IP addresses, ports, software identifiers, CVSS scores, and potential security impacts.

One important lesson was understanding that publicly indexed CVEs do not automatically confirm that a system is vulnerable.

## Python Automation

For the optional stretch challenge, I created a Python script that retrieves Shodan InternetDB information for a user-provided IP address.

I practiced working with Python functions, JSON, dictionaries, HTTP requests, command-line arguments, and exception handling.

## Challenges and Troubleshooting

While developing the script, I encountered several challenges:

- An HTTP 403 response when using Python's `urllib.request`.
- Python indentation and duplicate-code errors.
- A file-not-found error caused by running the script from the wrong Linux directory.
- An HTTP 404 response when querying an IP address without an available Shodan record.

I resolved these issues by inspecting error messages, testing commands individually, adding an HTTP User-Agent header, correcting indentation, and implementing error handling.

I also successfully tested the completed script on both Ubuntu Linux and Windows PowerShell.

## Key Takeaway

This project helped me connect cybersecurity investigation techniques with practical Python programming. It reinforced the importance of verifying security findings, documenting evidence, and understanding the tools used during an investigation.