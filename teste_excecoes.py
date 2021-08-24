try :
    arquivo = open("dados/contatos.csv", encoding="Latin_1", mode="w")
except FileNotFoundError :
    print("Arquivo não encontrado")
except PermissionError :
    print("Você não tem permissão para escrever neste arquivo")