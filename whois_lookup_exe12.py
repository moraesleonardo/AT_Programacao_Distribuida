import whois

dominio = "google.com"  # ou outro domínio

try:
    resultado = whois.whois(dominio)

    print("Resultado da consulta WHOIS:\n")

    for chave in resultado.keys():
        print(f"{chave}: {resultado[chave]}")
except Exception as e:
    print(f"Erro na consulta WHOIS: {type(e).__name__}: {e}")

