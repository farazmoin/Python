import subprocess
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Interface to change the MAC of')
    parser.add_argument('-m', '--newMac', dest='new_mac', help='New MAC address')
    args = vars(parser.parse_args())
    if not args['interface']:
        parser.error('Did you specify an interface?')
    elif not args['new_mac']:
        parser.error('Did you specify a MAC')
    return args

### Secure ###
def mac_changer(interface, new_mac):
    print('Changing MAC for ', interface, 'to ', new_mac)

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

### Insecure ###

# subprocess.call(f'ifconfig {interface} down', shell=True)
# subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
# subprocess.call(f'ifconfig {interface} up', shell=True)

### Should you wish to take user-input separately for interface, MAC, uncomment the 2 lines below ###

# interface = input('Enter the interface name: ')
# new_mac = input('Enter the new MAC address: ')

argument = get_args()
mac_changer(argument['interface'], argument['new_mac'])
