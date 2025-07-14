# Simple DoS Monitoring & Blocking Tool

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

# Usage

## 1. Run the Blocker (Requires root)

```bash
sudo python3 dos_monitor_blocker.py


2. Run the Tester

    Edit configuration in dos_tester.py:
    python

TARGET_IP = "192.168.1.100"  # Target server IP
INTERFACE = "eth0"           # Network interface

Execute:
bash

    python3 dos_tester.py

## Testing Setup

Successful tests were performed using two virtual machines:

| Role               | Environment      |
|--------------------|------------------|
| Monitoring/Blocking | Ubuntu 22.04 LTS |
| Traffic Generator   | Kali Linux       |
