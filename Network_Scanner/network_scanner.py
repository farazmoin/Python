import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request = broadcast/arp_request
    answered = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    print('IP\t\t\tMAC\n++++++++++++')
    for i in answered:
        print(i[1].psrc, '\t', i[1].hwsrc)

scan('192.168.160.1/24')
