import dns.resolver

dominio = "zonetransfer.me"
tipos = ["A", "NS", "MX", "TXT"]

for tipo in tipos:
    try:
        respostas = dns.resolver.resolve(dominio, tipo)
        for r in respostas:
            print(f"[{tipo}] {r.to_text()}")
    except Exception as e:
        print(f"[{tipo}] Erro: {e}")
