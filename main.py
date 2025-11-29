#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Processo:
    def __init__(self, pid):
        self.pid = pid
        self.relogio = 0  # Inicializa relógio lógico em 0

    def evento_interno(self):
        # Regra 1: Incrementa antes do evento
        self.relogio += 1
        print(f"[{self.pid}] Evento Interno. Relógio: {self.relogio}")

    def enviar_mensagem(self, destino_pid):
        # Regra 1: Incrementa
        self.relogio += 1
        # Regra 2 (envio): Inclui timestamp atual
        msg = {'origem': self.pid, 'timestamp': self.relogio}
        print(f"[{self.pid}] Enviando msg para {destino_pid}. Relógio: {self.relogio}, Timestamp da msg: {msg['timestamp']}")
        return msg

    def receber_mensagem(self, msg):
        timestamp_recebido = msg['timestamp']
        origem = msg['origem']
        
        # Regra 2 (recebimento): Max(local, recebido)
        # Nota: O ajuste acontece ANTES do incremento da execução do evento de recebimento
        self.relogio = max(self.relogio, timestamp_recebido)
        
        # Regra 1: Incrementa após o ajuste para processar o evento
        self.relogio += 1
        
        print(f"[{self.pid}] Recebeu msg de {origem} (Ts: {timestamp_recebido}). Novo Relógio: {self.relogio}")

def simular():
    p1 = Processo("P1")
    p2 = Processo("P2")
    p3 = Processo("P3")

    print("--- Início da Simulação de Lamport ---\n")

    # Sequência de Eventos Solicitada
    
    # 1. P1: Evento interno.
    p1.evento_interno()

    # 2. P2: Envia mensagem para P3.
    msg_p2_para_p3 = p2.enviar_mensagem("P3")

    # 3. P3: Recebe mensagem de P2.
    p3.receber_mensagem(msg_p2_para_p3)

    # 4. P1: Envia mensagem para P2.
    msg_p1_para_p2 = p1.enviar_mensagem("P2")

    # 5. P3: Evento interno.
    p3.evento_interno()

    # 6. P2: Recebe mensagem de P1.
    p2.receber_mensagem(msg_p1_para_p2)

    # 7. P2: Envia mensagem para P1.
    msg_p2_para_p1 = p2.enviar_mensagem("P1")

    # 8. P1: Recebe mensagem de P2.
    p1.receber_mensagem(msg_p2_para_p1)

    print("\n--- Estado Final dos Relógios ---")
    print(f"P1: {p1.relogio}")
    print(f"P2: {p2.relogio}")
    print(f"P3: {p3.relogio}")

if __name__ == "__main__":
    simular()