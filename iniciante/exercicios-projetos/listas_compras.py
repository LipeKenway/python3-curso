"""
Faça uma lista de compras com listas

* O usuario deve ter a possivilidade de inserir, apagar e listar valores da sua lista.

* Não permita que o programa quebre com erros de indices inexistentes na lista.
"""
import os

lista_compras = []

while True:   
    
    tamanho_lista = len(lista_compras)

    opcao = input('Selecione uma Opção -> [i]nserir | [a]pagar | [l]istar: ').lower()
    
    eh_um_digito = opcao.isdigit() 
    tamanho_opcao = len(opcao)
     
    if eh_um_digito:
        print('Por favor selecione uma opção valida.')
        continue
    
    if not eh_um_digito:

        if tamanho_opcao > 1:
            print('Digite apenas uma das letras permitidas.')
            continue
        
        # Inserir
        if opcao == 'i':
            os.system('cls')
            inserir = input('O que gostaria de adicionar na lista: ')
            lista_compras.append(inserir)
            
            os.system('cls')
            print(f'{inserir} foi adicionado a lista.')
            continue
            

        # Listar
        elif opcao == 'l':
            os.system('cls')
            if tamanho_lista == 0:
                print('Desculpe, mas não há itens ainda na sua lista.')
                continue
            
            else:
                print('-' * 50)
                print('Lista de Compras')
                
                for indice, item in enumerate(lista_compras):
                    print(f'\t{indice}: {item}')
                print('-' * 50)
        
        # Apagar
        elif opcao == 'a':
            os.system('cls')
            apagar = input('Escolha o indice para apagar: ')
            apagar_eh_digito = apagar.isdigit()

            if not apagar_eh_digito:
                print('Por favor, digite apenas numeros.')
                continue
            
            if tamanho_lista == 0:
                print('Nada para listar.')
                continue
            
            try:
                apagar = int(apagar)
                
                item_apagado = lista_compras.pop(apagar)
                del lista_compras[apagar]
               
                os.system('cls')
                print(f'{item_apagado} apagado com sucesso.')
            
            except IndexError:
                print('Indice não existe na lista.')
            
            except Exception:
                os.system('cls')
                print('Erro Desconhecido.')
            