import os
import time
from colorama import Fore, Style


def main():
    menu()


def clear():
    os.system('clear')


def invalid_option():
    for i in range(2, -1, -1):
        clear()
        print(Fore.RED + 'Opção Inválida' + Style.RESET_ALL)
        print(f'Voltando ao Menu Principal em {i} ...')
        time.sleep(1)


def menu():
    clear()
    print(Fore.GREEN + '+-------------«««Calculadora»»»-------------+' + Style.RESET_ALL)
    print('Escolha uma das operações abaixo:\n')
    print('«' + Fore.YELLOW + '1' + Style.RESET_ALL + '» SOMA')
    print('«' + Fore.YELLOW + '2' + Style.RESET_ALL + '» SUBTRAÇÃO')
    print('«' + Fore.YELLOW + '3' + Style.RESET_ALL + '» DIVISÃO')
    print('«' + Fore.YELLOW + '4' + Style.RESET_ALL + '» MULTIPLICAÇÃO')
    print('«' + Fore.YELLOW + '5' + Style.RESET_ALL + '» SAIR')
    print(Fore.GREEN + '+-------------------------------------------+ \n' + Style.RESET_ALL)
    option_menu()


option_main_menu = '1'


def option_menu():
    global option_main_menu
    option_main_menu = input('Digite a Opção Desejada => ')
    print(option_main_menu)
    clear()

    if '1' <= option_main_menu <= '4':
        operation_menu(option_main_menu)
    elif option_main_menu == '5':
        quit()
    else:
        invalid_option()
        menu()


def operation_menu(option):
    clear()
    print(Fore.GREEN + '+-------------«««Calculadora»»»-------------+ \n' + Style.RESET_ALL)
    num_one = int(input("Digite o primeiro número: "))
    num_two = int(input("Digite o Segundo número: "))
    if option == '1':
        result = num_one + num_two
        operator_char = '+'
    elif option == '2':
        result = num_one - num_two
        operator_char = '-'
    elif option == '3':
        result = num_one / num_two
        operator_char = '/'
    elif option == '4':
        result = num_one * num_two
        operator_char = '*'
    print(f'Resultado: {num_one} {operator_char} {num_two} = {result} \n')
    print('Aperte ' + Fore.YELLOW + 'ENTER ' + Style.RESET_ALL + ' para Continuar!')
    input()
    redo_menu()


def redo_menu():
    clear()
    print(Fore.GREEN + '+-------------«««Calculadora»»»-------------+ \n' + Style.RESET_ALL)
    print('Escolha uma das operações abaixo:\n')
    print('««' + Fore.YELLOW + '1' + Style.RESET_ALL + '»» Refazer a operação')
    print('««' + Fore.YELLOW + '2' + Style.RESET_ALL + '»» voltar ao Menu Principal \n')
    redo_menu_option = input('Digite a opção desejada => ')
    if redo_menu_option == "1":
        operation_menu(option_main_menu)
    elif redo_menu_option == "2":
        menu()
    else:
        invalid_option()


if __name__ == '__main__':
    main()
