from scapy.all import IP, ICMP, sr1

def main():
    destino = "8.8.8.8"
    print(f"[+] Enviando ICMP (ping) para {destino}...")

    pacote = IP(dst=destino)/ICMP()
    resposta = sr1(pacote, timeout=2, verbose=0)

    if resposta:
        print(f"[✓] Resposta recebida de {resposta.src}")
    else:
        print("[!] Nenhuma resposta recebida.")

if __name__ == "__main__":
    main()
