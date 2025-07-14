# DoS Monitoring & Blocking Tool

This repository contains two Python scripts for monitoring and mitigating DoS attacks:

## Scripts

### `dos_monitor_blocker.py`
- Monitors network traffic in real-time
- Blocks IP addresses exceeding specified packet rate threshold (default: 40 packets/second)
- Uses `iptables` for blocking
- Requires root privileges

### `dos_tester.py`
- Generates TCP packets to simulate DoS attacks
- Used for testing the blocker script
- Configurable target IP and network interface

## Requirements
```bash
pip install scapy
