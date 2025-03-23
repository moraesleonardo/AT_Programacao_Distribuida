import dns.resolver
import time

def consulta_basica(dominio):
    print(f"\nConsultando registros DNS para: {dominio}")
    tipos = ['A', 'NS', 'MX', 'TXT']
    for tipo in tipos:
        try:
            respostas = dns.resolver.resolve(dominio, tipo)
            for r in respostas:
                print(f"[{tipo}] {r.to_text()}")
        except Exception as e:
            print(f"[{tipo}] Erro: {e}")

def brute_force_subdominios(dominio):
    print(f"\nIniciando brute force de subdomínios para: {dominio}")
    subdominios_comuns = ["www", "mail", "ftp", "vpn", "intranet"]
    encontrados = []

    for sub in subdominios_comuns:
        subdominio = f"{sub}.{dominio}"
        try:
            resposta = dns.resolver.resolve(subdominio, "A")
            for r in resposta:
                print(f"Encontrado: {subdominio} -> {r}")
                encontrados.append(subdominio)
        except:
            print(f"Não encontrado: {subdominio}")
        time.sleep(0.3)

    return encontrados

def testar_programa():
    dominio_teste = "zonetransfer.me"
    print("Iniciando varredura DNS com dnspython\n")

    consulta_basica(dominio_teste)

    subdoms = brute_force_subdominios(dominio_teste)
    print(f"\nTotal de subdomínios encontrados: {len(subdoms)}")

    print("\nExecução finalizada.")

if __name__ == "__main__":
    testar_programa()
