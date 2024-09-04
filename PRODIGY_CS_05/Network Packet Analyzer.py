import socket
import struct
import textwrap

print("\n")
print(30 * "=")
print("   NETWORK PACKET ANALYZER")
print(30 * "=")

def eth_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[0:14])
    return get_mac(dest_mac), get_mac(src_mac), socket.htons(proto), data[14:]

def get_mac(bytes_addr):
    str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(str).upper()
    return mac_addr

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
    Pcount = 1
    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, proto, data = eth_frame(raw_data)
        print("\n")
        print(13 * "*")
        print(" Packet : ", Pcount)
        print(13 * "*")
        print('\nEthernet Frame : ')
        print(' Source : {}, Destination : {}, Protocol : {}'.format(dest_mac, src_mac, proto))

        if proto == 8:
            version, header_length, ttl, proto, src, dest, data = ipv4_packet(data)
            print('IPv4 : ')
            print('Version : {}, Header Lenght : {}, TTL : {}'.format(version, header_length, ttl))
            print('Protocol : {}, Source : {}, Destination : {}'.format(proto, src, dest))

            if proto == 1:
                icmp_type, code, checksum, data = ICMP_packet(data)
                print('\nICMP Packet : ')
                print('Type : {}, Code : {}, Checksum : {}'.format(icmp_type, code, checksum))
                print('Data : ')
                print(format_multiline('\t', data))

            elif proto == 6:
                src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_seg(data)
                print('\nTCP : ')
                print('Source Port : {}, Destination Port : {}'.format(src_port, dest_port))
                print('Sequence : {}, Acknowledgement : {}'.format(seq, ack))
                print('Source Port : {}, Destination Port : {}'.format(src_port, dest_port))
                print('Flags : ')
                print('URG : {}, ACK : {}, PSH : {}, RST : {}, SYN : {}, FIN : {}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
                print('Data : ')
                print(format_multiline('\t', data))

            elif proto == 17:
                src_port, dest_port, length, data = udp_seg(data)
                print('\nUDP : ')
                print('Source Port : {}, Destination Port : {}, Length : {}'.format(src_port, dest_port, length))
                print('Data : ')
                print(format_multiline('\t', data))
            
            else:
                print('\nData : ')
                print(format_multiline('\t', data))

        else:
            print('\nData : ')
            print(format_multiline('\t', data))
        Pcount += 1

def ipv4_packet(data):
    version_lenght = data[0]
    version = version_lenght >> 4
    header_length = (version_lenght & 15) * 4
    ttl, proto, src_ip, des_ip = struct.unpack('! 8x B B 2s 4s', data[:16])
    return version, header_length, ttl, proto, ipv4(src_ip), ipv4(des_ip), data[header_length:]

def ipv4(addr):
    return '.'.join(map(str, addr))

def ICMP_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

def tcp_seg(data):
    src_port, dest_port, seq, ack, off_res_flag = struct.unpack('! H H L L H', data[0:14])
    off = (off_res_flag >> 12) * 4
    flag_urg = (off_res_flag & 32) >> 5
    flag_ack = (off_res_flag & 16) >> 4
    flag_psh = (off_res_flag & 8) >> 3
    flag_rst = (off_res_flag & 4) >> 2
    flag_syn = (off_res_flag & 2) >> 1
    flag_fin = off_res_flag & 1
    return src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[off:]

def udp_seg(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[0:8])
    return src_port, dest_port, size, data[8:]

def format_multiline(prefix, string, size = 80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size%2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


main()