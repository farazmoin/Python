import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', dest='interface', help='Interface to change the MAC of')
parser.add_argument('-m', '--newMac', dest='new_mac', help='New MAC address')
args = vars(parser.parse_args())

### Should you wish to take user-input separately, uncomment the 2 lines below ###

# interface = input('Enter the interface name: ')
# new_mac = input('Enter the new MAC address: ')

interface = args['interface']
new_mac = args['new_mac']
print('Changing MAC for ', interface, 'to ', new_mac)

### Insecure ###

# subprocess.call(f'ifconfig {interface} down', shell=True)
# subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
# subprocess.call(f'ifconfig {interface} up', shell=True)

### Secure ###

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])


