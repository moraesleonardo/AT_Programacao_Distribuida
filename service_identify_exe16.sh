#!/bin/bash

# Alvo remoto e rede local
ALVO_REMOTO="scanme.nmap.org"
REDE_LOCAL="192.168.0.0/24"   # ajuste conforme sua rede
PORTAS_COMUNS="22,80,443"

echo "==============================="
echo "INICIANDO VARREDURAS COM NMAP"
echo "==============================="

# 1. Varredura de serviços e versões
echo -e "\n[1/3] Varredura de serviços e versões em $ALVO_REMOTO"
nmap -sV $ALVO_REMOTO

# 2. Verificação de vulnerabilidades no alvo remoto
echo -e "\n[2/3] Verificação de vulnerabilidades conhecidas em $ALVO_REMOTO"
nmap --script vuln $ALVO_REMOTO | grep -iE "vuln|cve|VULNERABLE" || echo "Nenhuma vulnerabilidade relevante encontrada."

# 3. Varredura da rede local com portas comuns
echo -e "\n[3/3] Varredura da rede local $REDE_LOCAL (requer sudo)"
sudo nmap -sS -p $PORTAS_COMUNS -sV --script vuln $REDE_LOCAL | grep -iE "vuln|cve|VULNERABLE|open" || echo "Nenhum serviço vulnerável encontrado na rede local."

# Fim
echo -e "\nTodas as varreduras foram concluídas!"
