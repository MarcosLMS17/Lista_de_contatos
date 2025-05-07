import json
import os

arquivo = 'contatos.json'

def carregar_contatos():
    try:
        with open(arquivo, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open(arquivo, 'w', encoding='utf8') as file:
        json.dump(contatos, file, ensure_ascii=False, indent=2)

def adicionar_contatos(contatos):
    nome = input('Digite o nome do contato: ')


    while True:
        telefone = input('Digite o telefone (ex: 11912345678): ')
        if telefone.isdigit() and len(telefone) == 11 and telefone[2] == '9':
            break
        print('Telefone inválido! Use o formato com DDD + 9 + 8 dígitos. Ex: 11912345678')


    while True:
        email = input('Digite o e-mail do contato: ')
        if '@' in email and '.' in email[email.index('@'):]:
            break
        print('E-mail inválido! Exemplo válido: usuario@email.com')

    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }

    contatos.append(novo_contato)
    salvar_contatos(contatos)
    print('Contato salvo com sucesso!')

def exibir_contatos(contatos):
    if not contatos:
        print('Nenhum contato cadastrado!')
        return

    print('\nLista de Contatos:')
    for i, contato in enumerate(contatos, start=1):
        print(f'{i}. Nome: {contato["nome"]}')
        print(f'   Telefone: {contato["telefone"]}')
        print(f'   E-mail: {contato["email"]}')
        print('-' * 30)

def excluir_contato(contatos):
    if not contatos:
        print('Nenhum contato cadastrado!')
        return

    print('\nContatos cadastrados:')
    for i, contato in enumerate(contatos, start=1):
        print(f'{i}. {contato["nome"]} - {contato["telefone"]} - {contato["email"]}')

    nome = input('\nDigite o nome exato do contato que deseja excluir: ')
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contatos.remove(contato)
            salvar_contatos(contatos)
            print(f"\nContato '{nome}' excluído com sucesso!")
            return

    print(f"\nContato '{nome}' não encontrado.")

def menu():
    contatos = carregar_contatos()
    while True:
        print('\nMenu:')
        print('1 - Adicionar contato')
        print('2 - Exibir contatos')
        print('3 - Excluir contato')
        print('4 - Sair')
        opcao = input('Escolha uma opção (1/2/3/4): ')
        if opcao == '1':
            adicionar_contatos(contatos)
        elif opcao == '2':
            exibir_contatos(contatos)
        elif opcao == '3':
            excluir_contato(contatos)
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()
