import scapy.all as scapy
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', '--ipaddress', help='IP address or range', dest='ip')
    args = vars(parser.parse_args())
    return args


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request = broadcast/arp_request
    answered = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]

    clients_list = list()
    for i in answered:
        client_dictionary = {'ip': i[1].psrc, 'mac': i[1].hwsrc}
        clients_list.append(client_dictionary)
        # print(i[1].psrc, '\t', i[1].hwsrc)
    return clients_list


def print_results(lst):
    print('IP\t\t\tMAC\n__________________________________')
    for client in lst:
        print(client['ip'], '\t', client['mac'])


args = get_args()
lst = scan(args['ip'])
print_results(lst)
