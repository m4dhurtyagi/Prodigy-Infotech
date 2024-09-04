## Network Packet Analyzer in Python
This repository contains a Python script for analyzing network packets at a low level. The script captures and interprets Ethernet frames, IPv4 packets, and their associated protocols (TCP, UDP, ICMP). It provides detailed insights into the structure and contents of network packets, making it a useful tool for network analysis and debugging.

# Features
* Ethernet Frame Analysis: Extracts and displays source and destination MAC addresses, as well as the protocol type.
* IPv4 Packet Analysis: Parses IPv4 headers to display version, header length, TTL (Time to Live), and protocol information.
* ICMP Packet Analysis: Interprets ICMP packets to show type, code, and checksum values.
* TCP Segment Analysis: Breaks down TCP segments to reveal source and destination ports, sequence and acknowledgment numbers, and various flags.
* UDP Segment Analysis: Extracts information from UDP segments including source and destination ports, and packet length.
* Data Formatting: Formats and displays packet data in a readable multi-line format.
