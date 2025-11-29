# Simulação de Relógios Lógicos de Lamport

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 📋 Sobre o Projeto

Este repositório contém a implementação prática do algoritmo de **Relógios Lógicos de Lamport**, um conceito fundamental na teoria de **Sistemas Distribuídos**.

Em ambientes distribuídos, relógios físicos raramente estão perfeitamente sincronizados devido à latência de rede e desvios de hardware (*clock drift*). Este projeto simula um sistema assíncrono onde a sincronização depende da relação "acontece-antes" ($\rightarrow$), garantindo uma ordenação parcial consistente dos eventos sem depender de um relógio global.

**Principais Conceitos Abordados:**
* Controle de Concorrência Distribuída.
* Troca de mensagens e Sincronização de Timestamps.
* Ordenação Causal de Eventos.

---

## ⚙️ Como Funciona

A simulação envolve 3 processos distintos ($P_1, P_2, P_3$) trocando mensagens. As regras de atualização do Relógio Lógico ($RL$) foram implementadas conforme descrito por Leslie Lamport:

1.  **Evento Local:** Antes de executar um evento interno, o processo incrementa seu relógio:  
    $RL_i = RL_i + 1$
2.  **Evento de Envio:** O processo incrementa seu relógio e anexa o timestamp $t = RL_i$ à mensagem.
3.  **Evento de Recebimento:** Ao receber uma mensagem com timestamp $t$, o destinatário ajusta seu relógio para:  
    $RL_j = max(RL_j, t) + 1$

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Execução
Clone o repositório e execute o script principal via terminal:

```bash
# Clone o repositório
git clone [https://github.com/dherii/simulacao-relogios-lamport.git](https://github.com/dherii/simulacao-relogios-lamport.git)

# Entre no diretório
cd simulacao-relogios-lamport

# Execute a simulação
python3 main.py