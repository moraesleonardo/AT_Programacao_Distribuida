from scapy.all import sniff, send, IP, TCP
import threading
import time

capturados = []

def processar_pacote(pacote):
    if IP in pacote:
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst

        protocolo = "TCP" if TCP in pacote else "Outro"

        info = f"{protocolo}: {ip_origem} -> {ip_destino}"
        print("[+] " + info)
        capturados.append(info)

def iniciar_sniffer(interface="lo", quantidade=5):
    print(f"[*] Iniciando captura na interface {interface}...")
    sniff(iface=interface, prn=processar_pacote, count=quantidade)
    print("[*] Captura finalizada.")

def enviar_pacotes_teste(destino="127.0.0.1", quantidade=5):
    time.sleep(1)  # Garante que o sniffer esteja rodando
    for _ in range(quantidade):
        pacote = IP(dst=destino) / TCP(dport=80)
        send(pacote, verbose=0)
        time.sleep(0.2)

def testar_sniffer():
    print("[*] Iniciando teste automatizado...")

    # Thread do sniffer
    thread_sniffer = threading.Thread(target=iniciar_sniffer, kwargs={"interface": "lo", "quantidade": 5})
    thread_sniffer.start()

    # Envia pacotes
    enviar_pacotes_teste()

    # Aguarda o sniffer terminar
    thread_sniffer.join()

    # Validação dos testes
    if len(capturados) == 5:
        print("\nTeste concluído com sucesso! Pacotes capturados corretamente.")
    else:
        print("\nTeste falhou. Pacotes capturados:", len(capturados))

if __name__ == "__main__":
    testar_sniffer()
