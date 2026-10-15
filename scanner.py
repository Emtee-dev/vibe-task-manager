import socket

alvo = "127.0.0.1"
print(f"[*] Escaneando {alvo}... sou eu mesmo!")

for porta in [22, 80, 8080, 8000]:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((alvo, porta))
        print(f"[+] Porta {porta} ABERTA!")
        s.close()
    except:
        print(f"[-] Porta {porta} fechada")

print("[*] Fim do scan - feito por mim!")
