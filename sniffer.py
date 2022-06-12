#! /usr/bin/env python3
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 


import socket
import struct
import textwrap
import os

def main():
	loop = True
	connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	while loop:
		try:
			raw_data, address = connection.recvfrom(65536)
			dst_mac, src_mac, eth_prot, data = ethernet_frame(raw_data)
			if eth_prot == 8:
				(version, header_length, ttl, protocol, source, target, data) = ipv4_packet(data)
				print("IPv4 Packet ~> " + str(src_mac) + " ==> " + str(dst_mac))
				print("\tProtocol: {}, Source: {}, Target: {}".format(protocol, source, target))
				get_domain("\tSource ~> ", "{}".format(source))
				get_domain("\tTarget ~> ", "{}".format(target))
				
				seperator()
		except KeyboardInterrupt:
			loop = False

def seperator():
	os.system("sep -l 1 -s '-'")

def get_domain(tp, data):
	cmd = "whois "
	cmd += data
	cmd += " | grep OrgName"
	name = os.popen(cmd).read()
	name = name.rstrip("\n")
	if name != "":
		print(str(tp) + str(name))

def get_mac_addr(bytes_address):
	bytes_string = map("{:02x}".format, bytes_address)
	return ":".join(bytes_string).upper()

def ethernet_frame(data):
	dst_mac, src_mac, protocol = struct.unpack("! 6s 6s H", data[:14])
	return get_mac_addr(dst_mac), get_mac_addr(src_mac), socket.htons(protocol), data[14:]

def ipv4_packet(data):
	version_header_length = data[0]
	version = version_header_length >> 4
	header_length = (version_header_length & 5) * 4
	ttl, proto, src, target = struct.unpack("! 8x B B 2x 4s 4s", data[:20])
	return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

def ipv4(addr):
	return ".".join(map(str, addr))

def icmp_packet(data):
	icmp_type, code, checksum = struct.unpack("! B B H", data[:4])
	return icmp_type, code_checksum, data[4:]

def tcp_segment(data):
	(scr_port, dest_port, sequence, acknowledgement, offset_reserved_flags) = struct.unpack("! H H L L H", data[:14])
	offset = (offset_reserved_frags >> 12) * 4
	flag_urg = (offset_reserved_flags & 32) >> 5
	flag_ack = (offset_reserved_flags & 16) >> 4
	flag_psh = (offset_reserved_flags & 8) >> 3
	flag_rst = (offset_reserved_flags & 4) >> 2
	flag_syn = (offset_reserved_flags & 2) >> 1
	flag_fin = offset_reserved_flags & 1
	return src_port, dest_port, sequence, acknowledgement, flag_usr, flag_ack, flag_pshm, flag_rst, flag_syn, flag_fin, data[offset:]

if __name__ == "__main__":
    main()
