from scapy.all import IP, TCP, sr
import sys

def scan_ports(host, ports):
    print(f"\nIniciando escaneamento no host {host}...\n")
    for port in ports:
        pkt = IP(dst=host)/TCP(dport=port, flags="S")
        resp = sr(pkt, timeout=1, verbose=0)[0]
        
        for _, r in resp:
            if r.haslayer(TCP):
                if r[TCP].flags == 18:  # SYN-ACK
                    print(f"Porta {port}: ABERTA")
                elif r[TCP].flags == 20:  # RST-ACK
                    print(f"Porta {port}: FECHADA")
            else:
                print(f"Porta {port}: SEM RESPOSTA")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 port_scan_scapy.py <IP>")
        sys.exit(1)

    target_ip = sys.argv[1]
    portas_para_testar = [21, 22, 23, 80, 443, 8080]

    scan_ports(target_ip, portas_para_testar)
