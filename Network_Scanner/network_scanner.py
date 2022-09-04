import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request = broadcast/arp_request
    answered, unanswered = scapy.srp(broadcast_arp_request, timeout=1)
    print(answered.summary())


scan('192.168.160.1/24')
