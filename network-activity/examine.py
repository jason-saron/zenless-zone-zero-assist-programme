from scapy.all import sniff

from permission_acquisition.PrivilegeManager import run_as_admin


def packet_callback(packet):
    if packet.haslayer("IP"):
        print(f"网络通信: {packet[IP].src} -> {packet[IP].dst} - 端口: {packet.sport} -> {packet.dport}")

run_as_admin()
# 监听游戏的主要端口
sniff(filter="port 443 or port 54451", prn=packet_callback, store=0)


