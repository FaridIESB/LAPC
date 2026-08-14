import random

##############################
# ADICIONAR ITEM AO CARDAPIO #
##############################

cardapio = []

#Cria classe de itens de cardapio
class ItemCardapio:
    def __init__(self, nome, categoria, vegetariano, preco):
        self.nome = nome
        self.categoria = categoria
        self.vegetariano = vegetariano
        self.preco = preco

#Função para cadastrar os itens

def cadastro_cardapio():
    print()
    print("========================")
    print("| CADASTRAR ITEN       |")
    print("========================")
    print()

    nome = input("Qual o nome do item?  \n")
    categoria = input("\nQual é a categoria? ( prato / bebida / sobremesa)  \n")
    vegetariano = input("\nÉ vegerariano? (sim / não)  \n")
    #corrigir erro de virgula e ponto: https://pt.stackoverflow.com/questions/355237/n%C3%A3o-foi-poss%C3%ADvel-converter-string-para-float-por-qu%C3%AA
    preco = float(input("\nQual é o preço?  \n").replace(',', '.'))

    item = ItemCardapio(nome, categoria, vegetariano, preco)

# Adiciona itens
    cardapio.append(item)

    print()
    print("****************************")
    print("Item cadastrado com sucesso!")
    print("****************************")
    print()

######################################
# CADASTRO DE CLIENTES / FIDELIZAÇÃO #
######################################

#cria lista de clientes global
clientes = []

# Função de cadastro de cliente
def cadastro_cliente():
    print()
    print("========================")
    print("| CADASTRO DE CLIENTES |")
    print("========================")
    print()
    nome = input("Nome do cliente:")
    print()
    print()

    # Criar um ID de cliente https://docs.python.org/3/library/random.html
    num_fidelidade = random.randint(1, 100000)

    # adicionar dados em lista para alterar quantidade de compras no último indice em vez de tupla como antes
    cliente = [nome, num_fidelidade, 0]

    # adicionar cliente para a lista global
    clientes.append(cliente)

    print()
    print("**********************************************************************************")
    print(f"{nome.upper()} cadastrado com sucesso! \n\nNúmero de fidelidade: {num_fidelidade}")
    print("**********************************************************************************")
    print()


################
# FAZER PEDIDO #
################

pedidos = []

def realizar_pedido():
    print()
    print("========================")
    print("| REALIZAR PEDIDO      |")
    print("========================")
    print()

    extra = False

    # pegar dados do pedido
    id_cliente = input("Número de fidelidade do cliente:  \n")
    prato = input("Qual o prato?  \n")
    bebiba = input("\nQual a bebiba?  \n")
    sobremesa = input("\nQual o sobremesa?  \n")
    extra = input("\nMais alguma coisa?  \n")

    print()
    print("**********************************************************************************************************************")
    print(f"Seu pedido é: prato princípal: {prato.upper()}, para beber: {bebiba.upper()}, de sobremesa temos: {sobremesa.upper()}")
    if extra:
        print(f"Também temos {extra.upper()}")
    print("**********************************************************************************************************************")
    print()


    # adicionar pedido
    pedido = [prato, bebiba, sobremesa, extra]
    print(pedido)


    # VER SE TEM DESCONTO

    # Função de desconto, se cliente comprar 5 vezes ganha 15% de desconto
    def desconto(cliente):
        if cliente[2] == 5:
            print("***********************************")
            print("Parabéns, ganhou um desconto de 15%")
            print("***********************************")
            cliente[2] = 0

    # Procura o cliente pelo id e soma cada compra
    cliente_encontrado = False

    for cliente in clientes:
        if int(id_cliente) == cliente[1]:
            cliente_encontrado = True
            cliente[2] += 1
            desconto(cliente)

    if not cliente_encontrado:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Cliente não cadastrado. Não tem fidelidade")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    # enviar pedido pra cozinha
    pedidos.append(pedido)

    menu()



#########
# MENUS #
#########

# MENU CARDÁPIO

# Menu do cardápio para cadastrar mais itens ou voltar ao menu inicial

def menu_cardapio():

    cardapio_menu = True

    while cardapio_menu:
        print()
        print("******************************")
        print()
        print("Digite a opção:")
        print()
        print("1- Cadastrar item no cardápio\n")
        print("2- Voltar ao menu inicial")
        print()
        print("******************************")
        print()

        opcao = input("Digite a opção:")
        print()

        if opcao == "1":
            cadastro_cardapio()
        elif opcao == "2":
            cardapio_menu = False
        else:
            print(f"!!! Opção invalida, tente de novo !!!")


# MENU DE CADASTRO DE CLIENTES

# Menu do cardápio para cadastrar mais clientes ou voltar ao menu inicial

def menu_cadastro():

    cadastro = True

    while cadastro:
        print()
        print("******************************")
        print()
        print("Digite a opção:")
        print()
        print("1- Cadastrar Cliente\n")
        print("2- Voltar ao menu inicial")
        print()
        print("******************************")
        print()

        opcao = input("Digite a opção:")
        print()

        if opcao == "1":
            cadastro_cliente()
        elif opcao == "2":
            cadastro = False
        else:
            print(f"!!! Opção invalida, tente de novo !!!")



# MENU INICIAL

def menu():
    while True:
        print("")
        print(" ============================================================================================================ ")
        print("")
        print(r"  /$$$$$$$$ /$$                 /$$$$$$$                                       /$$$$$$  /$$     /$$ /$$$$$$  ")
        print(r" |__  $$__/|__/                | $$__  $$                                     /$$__  $$|  $$   /$$//$$__  $$ ")
        print(r"    | $$    /$$  /$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$       | $$  \__/ \  $$ /$$/| $$  \__/ ")
        print(r"    | $$   | $$ |____  $$      | $$$$$$$/ /$$__  $$ /$$_____/ |____  $$      |  $$$$$$   \  $$$$/ |  $$$$$$  ")
        print(r"    | $$   | $$  /$$$$$$$      | $$__  $$| $$  \ $$|  $$$$$$   /$$$$$$$       \____  $$   \  $$/   \____  $$ ")
        print(r"    | $$   | $$ /$$__  $$      | $$  \ $$| $$  | $$ \____  $$ /$$__  $$       /$$  \ $$    | $$    /$$  \ $$ ")
        print(r"    | $$   | $$|  $$$$$$$      | $$  | $$|  $$$$$$/ /$$$$$$$/|  $$$$$$$      |  $$$$$$/    | $$   |  $$$$$$/ ")
        print(r"    |__/   |__/ \_______/      |__/  |__/ \______/ |_______/  \_______/       \______/     |__/    \______/  ")
        print("")
        print(" ============================================================================================================ ")
        print("")
        print("")
        print("Bem vindos, escolha a opção:")
        print("")
        print(" 1- Cadastro de item de cardápio")
        print(" 2- Cadastro de cliente")
        print(" 3- Realizar pedido")
        print(" 4- Sair")
        print("")
        print("")
        print("")
        print("")
        opcao = input("Digite a opção:")
        print("")
        #escolhe entre as opções e leva as funções 
        if opcao == "1":
            menu_cardapio()
        elif opcao == "2":
            menu_cadastro()
        elif opcao == "3":
            realizar_pedido()
        elif opcao == "4":
            print()
            print("==============================")
            print("|                            |")
            print("|  Bom descanso, até amanhã! |")
            print("|                            |")
            print("==============================")
            print()
            return
        else:
            print(f"!!! Opção invalida, tente de novo !!!")

###########################################
###########################################
# CHAMA MENU INICIAL
###########################################
###########################################

menu()




