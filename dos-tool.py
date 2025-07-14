import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

THRESHOLD = 40
print(f"THRESHOLD: {THRESHOLD}")

# Function that runs every time a packet is captured
def packet_callback(packet): 
    src_ip = packet[IP].src  # get the source IP address
    packet_count[src_ip] += 1  # increment count for that IP
    
    current_time = time.time()
    time_interval = current_time - start_time[0]

    if time_interval >= 1:  # if at least 1 second passed
        for ip, count in packet_count.items(): 
            packet_rate = count / time_interval  # calculate packet rate

            if packet_rate > THRESHOLD and ip not in blocked_ips: 
                print(f"Blocking IP: {ip}, packet rate: {packet_rate}")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")  # block using iptables
                blocked_ips.add(ip)

        packet_count.clear()  # reset counts for next second
        start_time[0] = current_time  # reset timer

if __name__ == "__main__":
    # Check for root privileges
    if os.geteuid() != 0:
        print("This script requires root privileges.")
        sys.exit(1)

    packet_count = defaultdict(int)  # stores counts per IP
    start_time = [time.time()]  # list to hold start time (so it can be modified inside function)
    blocked_ips = set()  # stores blocked IPs

    print("Monitoring network traffic...")
    sniff(filter="ip", prn=packet_callback)  # starts sniffing packets, calling packet_callback for each
