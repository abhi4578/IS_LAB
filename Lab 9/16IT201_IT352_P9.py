#!/usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
dst_ip = input("Enter ip address / website url \n")
src_port=2500
dst_port=int(input("Enter the port no.\n"))
conf.verb=0
choice=int(input("1)Tcp connect scanning 2) SYN scanning\n" ))
#print(str(type(tcp_connect_scan_resp)))
print("Checking whether  dstination host is alive....")
ping = sr1(IP(dst = dst_ip)/ICMP(),timeout=5)
flag=0
if(str(type(ping))=="<class 'NoneType'>" or ping.getlayer(ICMP).type==11):
    #print("host not to be found using ping")
    flag=1
else:
    print("Destination Host is alive!!")
seq_k=0
def TCP_CONNECT(dst_port):
    global seq_k,flag
    SYN=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")
    print(" Sending SYN message to ",dst_ip)
    print("TCP header contents")
    SYN.getlayer(TCP).display()
    tcp_connect_scan_resp = sr1(SYN,timeout=10)
    scan_result=""
    conf.verb = 0 

    if(str(type(tcp_connect_scan_resp))=="<class 'NoneType'>"):
        print("No packet recieved from ",dst_ip)
        scan_result="SYN packet was filtered/dropped"

    elif(tcp_connect_scan_resp.haslayer(TCP)):

        print("Packet Recieved!!")
        print("Content of packet recieved from  ",dst_ip)
        tcp_connect_scan_resp.getlayer(TCP).display()
        if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
            scan_result="Port "+str(dst_port)+" is Open"

            if choice==1:
                print("Sending ACK  packet to ",dst_ip,"with content:")
                seq_k+=1
                A=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,ack=1,seq=seq_k,window=229,flags="A")
                
                A.getlayer(TCP).display()
                send_ack = sr(A,timeout=10)

            print("Reseting the connection to ",dst_ip,"with content")
            seq_k+=1
            R=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,seq=seq_k,flags="R")
            R.getlayer(TCP).display()
            send(R)
            

        elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
            scan_result="Port "+str(dst_port)+" is closed"
        
    elif flag==1:
        print("host not to be found")


    return scan_result
scan_result=TCP_CONNECT(dst_port)
print("---------------")
print(scan_result)
print("---------------")
