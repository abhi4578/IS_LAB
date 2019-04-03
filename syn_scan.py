#!/usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys 
dst_ip = input("Enter ip address / website url:")

src_port = RandShort()
dst_port=80
conf.verb=0

print("Checking whether host is alive....")
ping = sr1(IP(dst = dst_ip)/ICMP(),timeout=5)
    
if(str(type(ping))=="<class 'NoneType'>"):
    print("host is dead, cannot conduct port scaninng")
    print("Exiting...")
    sys.exit(1)

print("Host is alive!!")

def SYN_SCAN(dst_port):
    scan_result=""
    SYN=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")
    print("Sneding SYN to ",dst_ip,"with contents")
    SYN.getlayer(TCP).display()
    stealth_scan_resp = sr1(SYN,timeout=10)
    scan_result=""

    if(str(type(stealth_scan_resp))=="<class 'NoneType'>"):
        print("No packets recieved from ",dst_ip)
        scan_result="Filtered / dropped"

    elif(stealth_scan_resp.haslayer(TCP)):
        print("Packet recieved from ",dst_ip," with contents:")
        stealth_scan_resp.getlayer(TCP).display()

        if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
            scan_result="Port "+str(dst_port)+" is open"
            RST=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R")
            print("Reseting Connection with ",dst_ip,"with contents:")
            RST.getlayer(TCP).display()
            send(RST)
            

        elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
            scan_result="Port "+str(dst_port)+" is Closed"
    
    return scan_result

scan_result=SYN_SCAN(dst_port)
print("---------------")
print(scan_result)
print("---------------")