"""
Escopo de funções em Python

Escopo significa o local onde aquele codigo pode atingir.

Existe o escopo global e local.

O Escopo global é o escopo onde todo o codigo é alcançavel.

O Escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.

Não temos acesso a nomes de escopos internos nos escopos externos.

A palavra global faz uma variavel do escopo externo ser 
a mesma no escopo interno.
"""
x = 1

def escopo():
    # global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)