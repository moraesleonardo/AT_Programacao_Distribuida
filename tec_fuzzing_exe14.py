import requests
import time

def carregar_palavras_chave():
    # Lista reduzida de diretórios/endpoints comuns (pode ser substituída por um dicionário maior)
    return [
        "admin", "login", "dashboard", "test", "backup", "old", "dev", "config", "phpinfo", "server-status"
    ]

def fuzzing_url(base_url, palavras):
    print(f"\nIniciando fuzzing em: {base_url}\n")
    encontrados = []

    for palavra in palavras:
        url = f"{base_url}/{palavra}"
        try:
            resposta = requests.get(url, timeout=5)
            if resposta.status_code < 400:
                print(f"[{resposta.status_code}] Encontrado: {url}")
                encontrados.append((url, resposta.status_code))
            else:
                print(f"[{resposta.status_code}] Não encontrado: {url}")
        except requests.exceptions.RequestException as e:
            print(f"[ERRO] Falha ao acessar {url}: {e}")
        time.sleep(0.2)

    return encontrados

def testar_fuzzing():
    base_url = "http://testphp.vulnweb.com"  # Substitua por um domínio de teste controlado
    palavras = carregar_palavras_chave()
    
    resultados = fuzzing_url(base_url, palavras)

    print("\nResumo do Fuzzing:")
    if resultados:
        for url, codigo in resultados:
            print(f" - [{codigo}] {url}")
    else:
        print("Nenhum endpoint acessível encontrado.")

if __name__ == "__main__":
    testar_fuzzing()
