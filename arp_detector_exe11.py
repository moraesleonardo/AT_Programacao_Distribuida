from scapy.all import ARP, sniff, sendp, Ether
from collections import defaultdict
import threading
import time

# Tabela que relaciona IPs e os MACs já vistos
tabela_arp = defaultdict(set)
alertas_detectados = []

def detectar_arp_spoof(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:  # ARP reply
        ip = pacote[ARP].psrc
        mac = pacote[ARP].hwsrc

        tabela_arp[ip].add(mac)

        if len(tabela_arp[ip]) > 1:
            alerta = f"[!] Possível ataque ARP spoofing detectado! IP {ip} com múltiplos MACs: {tabela_arp[ip]}"
            print(alerta)
            alertas_detectados.append(alerta)
        else:
            print(f"[+] ARP legítimo: {ip} -> {mac}")

def iniciar_sniffer(interface="lo", duracao=6):
    print(f"[*] Iniciando captura ARP na interface '{interface}' por {duracao} segundos...")
    sniff(iface=interface, filter="arp", store=0, prn=detectar_arp_spoof, timeout=duracao)
    print("[*] Captura finalizada.")

def simular_ataque_arp(ip_alvo="192.168.0.1", mac_legitimo="AA:BB:CC:DD:EE:01", mac_fake="11:22:33:44:55:66"):
    time.sleep(2)  # Espera o sniffer iniciar

    print("[*] Enviando ARP legítimo...")
    arp_legitimo = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=2, psrc=ip_alvo, hwsrc=mac_legitimo)
    sendp(arp_legitimo, iface="lo", verbose=0)

    time.sleep(1)

    print("[*] Enviando ARP falso (spoof)...")
    arp_fake = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=2, psrc=ip_alvo, hwsrc=mac_fake)
    sendp(arp_fake, iface="lo", verbose=0)

def executar_teste():
    print("[*] Iniciando teste automatizado de detecção de ARP spoofing...\n")

    # Inicia o sniffer em uma thread
    sniffer_thread = threading.Thread(target=iniciar_sniffer, kwargs={"interface": "lo", "duracao": 6})
    sniffer_thread.start()

    # Simula ataque ARP
    simular_ataque_arp()

    sniffer_thread.join()

    # Verifica se o alerta foi detectado
    if alertas_detectados:
        print("\nTeste bem-sucedido: ARP spoofing detectado corretamente.")
    else:
        print("\nTeste falhou: Nenhum ARP spoofing detectado.")

if __name__ == "__main__":
    executar_teste()

