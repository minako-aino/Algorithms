
import argparse
from scapy.all import *


def tcp_scan(ip, ports):
    try:
        syn = IP(src="192.168.10.2", dst=ip) / TCP(dport=ports, flags="S")
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(ip))

    ans, unans = sr(syn, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        if received[TCP].flags == "SA":
            result.append(received[TCP].sport)

    return result


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        dest="command", help="Command to perform.", required=True
    )

    tcp_subparser = subparsers.add_parser(
        'TCP', help='Perform a TCP scan using SYN packets.'
    )
    tcp_subparser.add_argument('IP', help='An IP address or hostname to target.')
    tcp_subparser.add_argument(
        'ports', nargs='+', type=int,
        help='Ports to scan, delimited by spaces'
    )
    tcp_subparser.add_argument(
        '--range', action='store_true',
        help='Specify a range of ports'
    )

    args = parser.parse_args()

    if args.range:
        ports = tuple(args.ports)
    else:
        ports = args.ports

    try:
        result = tcp_scan(args.IP, ports)
    except ValueError as error:
        print(error)
        exit(1)

    for port in result:
        print('Port {} is open.'.format(port))


if __name__ == '__main__':
    main()
