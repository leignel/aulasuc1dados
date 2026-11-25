while True:
    print("\n=== MENU ===")
    print("1 - Dizer olá")
    print("2 - Mostrar a tabuada do 2")
    print("0 - Sair")
    opcao = input("Opção: ")

    match opcao:                    
        case "1":
            print("Olá!")
        case "2":
            for i in range(1, 11):
                print(f"2 x {i} = {2 * i}")
        case "0":
            print("Até logo!")
        case _:
            print("Opção inválida.")

    if opcao == "0":
        break  