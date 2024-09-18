Sistema Bancário Simples
Este é um programa de console em Python que simula um sistema bancário básico. Ele permite ao usuário realizar operações como depósito, saque, exibição de extrato e encerrar a sessão.

Funcionalidades
Depósito: O usuário pode depositar valores positivos que são adicionados ao saldo.
Saque: O usuário pode realizar até 3 saques diários, respeitando um limite de R$500 por saque e o saldo disponível.
Extrato: Exibe todas as operações realizadas (depósitos e saques) e o saldo atual.
Sair: Finaliza o programa.
Regras de Saque
Limite diário de 3 saques.
O valor do saque não pode exceder o saldo disponível.
O limite por saque é de R$500.
Fluxo de Operações
O programa exibe um menu com opções:
[d] para depositar
[s] para sacar
[e] para exibir o extrato
[q] para sair
O usuário escolhe uma opção e o programa solicita os dados necessários (como o valor para depositar ou sacar).
Após a execução de cada operação, o menu é exibido novamente até que o usuário escolha a opção de sair.
Como executar
Clone este repositório ou copie o código para um arquivo Python (.py).
Execute o programa no terminal com o comando:
bash
Copiar código
python nome_do_arquivo.py
Exemplo de uso
text
Copiar código
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Digite o valor a ser depositado: 100
Depósito realizado com sucesso.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e
Extrato:
Depósito: +100.0
Saldo atual: 100.0
