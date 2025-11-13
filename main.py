def start():
    print("Вы просыпаетесь в тёмной комнате.")
    print("Что вы будете делать?")
    print("1 - Осмотреться вокруг")
    print("2 - Попробовать открыть дверь")
    print("3 - Попробовать открыть потайной люк в полу")
    choice = input("> ")

    if choice == "1":
        look_around()
    elif choice == "2":
        locked_door()
    elif choice == "3":
        boss_room()
    else:
        print("Неверный ввод. Попробуйте снова.\n")
        start()

def look_around():
    print("\nВы видите стол, на нём лежит ключ.")
    print("1 - Взять ключ")
    print("2 - Игнорировать и вернуться к двери")
    choice = input("> ")

    if choice == "1":
        print("\nВы берёте ключ. Может, он подойдёт к двери.")
        have_key()
    elif choice == "2":
        locked_door()
    else:
        print("Неверный ввод.\n")
        look_around()

def locked_door():
    print("\nВы подходите к двери. Она заперта.")
    print("1 - Вернуться и поискать что-то в комнате")
    print("2 - Постучать в дверь")
    choice = input("> ")

    if choice == "1":
        look_around()
    elif choice == "2":
        print("\nНикто не отвечает... Вы один.")
        locked_door()
    else:
        print("Неверный ввод.\n")
        locked_door()

def have_key():
    print("\nВы стоите перед дверью с ключом в руках.")
    print("1 - Попробовать открыть дверь ключом")
    print("2 - Подождать немного")
    choice = input("> ")

    if choice == "1":
        win()
    elif choice == "2":
        print("\nВы ждёте... но ничего не происходит.")
        have_key()
    else:
        print("Неверный ввод.\n")
        have_key()

def boss_room():
    print("\nВы спускаетесь по люку... и оказываетесь в логове монстра!")
    print("Босс огромен и рычит.")
    print("1 - Попробовать сразиться")
    print("2 - Сбежать обратно в комнату")
    choice = input("> ")

    if choice == "1":
        print("\nВы бросаетесь на босса, но он слишком силён.")
        print("Вы проиграли ")
        print("GAME OVER")
    elif choice == "2":
        print("\nВы в панике карабкаетесь обратно через люк.")
        start()
    else:
        print("Неверный ввод.\n")
        boss_room()

def win():
    print("\nВы вставляете ключ в замок и дверь открывается.")
    print("Солнечный свет ослепляет вас - вы на свободе!")
    print("Поздравляем, вы прошли квест! ")

if __name__ == "__main__":
    start()
