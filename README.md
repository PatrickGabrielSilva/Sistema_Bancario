# Sistema Bancário Simples

Este é um programa em Python que simula operações bancárias básicas via console. O usuário pode realizar depósitos, saques, consultar o extrato e sair.

## Funcionalidades

- **Depósito:** Adiciona valores positivos ao saldo.
- **Saque:** O usuário pode realizar até 3 saques por dia, com um limite de R$500 por saque e limitado ao saldo disponível.
- **Extrato:** Exibe o histórico de transações (depósitos e saques) e o saldo atual.
- **Sair:** Encerra o programa.

## Regras de Saque

- Limite de 3 saques por dia.
- O valor de cada saque não pode exceder R$500.
- O saque deve respeitar o saldo disponível na conta.

## Fluxo de Operações

1. O programa exibe um menu com as seguintes opções:
   - `[d]` para depositar.
   - `[s]` para sacar.
   - `[e]` para exibir o extrato.
   - `[q]` para sair.
2. O usuário escolhe a opção desejada e insere o valor nas operações de depósito e saque.
3. Após cada operação, o menu é exibido novamente até o usuário optar por sair.

## Como Executar

1. Clone este repositório ou copie o código para um arquivo Python (`.py`).
2. Execute o programa no terminal com o comando:
   ```bash
   python nome_do_arquivo.py
