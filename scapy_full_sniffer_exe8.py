from scapy.all import sniff, IP, TCP, send

# Função para modificar e reinjetar pacotes TCP
def processar_pacote(pacote):
    if IP in pacote and TCP in pacote:
        print("\n[+] Pacote TCP capturado")
        print(f"    De {pacote[IP].src}:{pacote[TCP].sport} → {pacote[IP].dst}:{pacote[TCP].dport}")

        # Clonando e modificando o pacote
        novo_pacote = pacote.copy()
        novo_pacote[IP].src = "192.168.0.123"   # Modifica o IP de origem
        novo_pacote[IP].ttl = 99                # Modifica o TTL
        del novo_pacote[IP].chksum              # Remove checksums para regenerar
        del novo_pacote[TCP].chksum

        # Reinjeção na rede
        send(novo_pacote, verbose=0)
        print("[✓] Novo pacote injetado com IP de origem alterado")

# Captura com filtro TCP
def capturar():
    print("[*] Capturando pacotes TCP na interface enp2s0...")
    sniff(filter="tcp", iface="enp2s0", prn=processar_pacote, count=5)

if __name__ == "__main__":
    capturar()

