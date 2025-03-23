import pcapy

def packet_handler(header, data):
    print(f"[+] Pacote capturado com {len(data)} bytes")
    print(data.hex())
    print("-" * 40)

def main():
    interfaces = pcapy.findalldevs()
    print("Interfaces disponíveis:")
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")

    index = int(input("Escolha o número da interface: "))
    iface = interfaces[index]
    print(f"[+] Capturando na interface: {iface}")

    cap = pcapy.open_live(iface, 65536, 1, 100)
    cap.setfilter("ip")

    print("[*] Capturando 5 pacotes IP...")
    cap.loop(5, packet_handler)
    print("[✓] Captura finalizada.")

if __name__ == "__main__":
    main()

