import nmap
import threading
import time

# Função de varredura síncrona
def varredura_sincrona(ip, portas):
    print(f"\n[Sincrono] Iniciando varredura em {ip} nas portas {portas}...")
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, ports=portas, arguments='-sS')

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"Estado: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocolo: {proto}")
            portas = nm[host][proto].keys()
            for porta in sorted(portas):
                estado = nm[host][proto][porta]['state']
                print(f"  Porta: {porta} - Estado: {estado}")

# Função de varredura assíncrona com callback
def varredura_assincrona(ip, portas):
    print(f"\n[Assíncrono] Iniciando varredura em {ip} nas portas {portas}...")
    nm = nmap.PortScannerAsync()

    def callback_resultado(host, scan_result):
        print(f"\n[Callback] Resultado para {host}:")
        for proto in scan_result['scan'][host].get('tcp', {}):
            estado = scan_result['scan'][host]['tcp'][proto]['state']
            print(f"  Porta: {proto} - Estado: {estado}")

    nm.scan(hosts=ip, ports=portas, arguments='-sS', callback=callback_resultado)

    # Aguarda até a varredura assíncrona terminar
    while nm.still_scanning():
        print("  Aguardando resultados...")
        time.sleep(1)

# Função principal de testes
def testar_varreduras():
    alvo = "scanme.nmap.org"  # Domínio de testes públicos do Nmap
    portas = "22,80,443"

    # Executa varredura síncrona
    varredura_sincrona(alvo, portas)

    # Executa varredura assíncrona
    varredura_assincrona(alvo, portas)

if __name__ == "__main__":
    testar_varreduras()
