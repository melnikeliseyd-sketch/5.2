def start():
    print("Вы просыпаетесь в тёмной комнате.")
    print("Что вы будете делать?")
    print("1 - Осмотреться вокруг")
    print("2 - Попробовать открыть дверь")
    choice = input("> ")

    if choice == "1":
        look_around()
    elif choice == "2":
        locked_door()
    else:
        print("Неверный ввод. Попробуйте снова.\n")
        start()

def look_around():
    print("\nВы видите стол, на нём лежит ключ.")
    print("1 - Взять ключ")
    print("2 - Игнорировать и вернуться к двери")
    print("3 - Проверить странный шкаф")  # новая опция для секретной комнаты
    choice = input("> ")

    if choice == "1":
        print("\nВы берёте ключ. Может, он подойдёт к двери.")
        have_key()
    elif choice == "2":
        locked_door()
    elif choice == "3":
        secret_room()
    else:
        print("Неверный ввод.\n")
        look_around()

def locked_door():
    print("\nВы подходите к двери. Она заперта.")
    print("1 - Вернуться и поискать что то в комнате")
    print("2 - Постучать в дверь")
    choice = input("> ")

    if choice == "1":
        look_around()
    elif choice == "2":
        print("\nНикто не отвечает. Дверь по прежнему заперта.")
        locked_door()
    else:
        print("Неверный ввод.\n")
        locked_door()

def have_key():
    print("\nВы вставляете ключ в замок и дверь открывается.")
    print("вы на свободе!")
    print("Солнечный свет ослепляет вас - вы на свободе!")
    print("Поздравляем, вы прошли квест!")

def secret_room():
    print("\nВы обнаружили тайную дверь за старым шкафом!")
    print("Комната темна, но вы замечаете светящийся сундук.")
    print("1 - Открыть сундук")
    print("2 - Вернуться обратно")
    choice = input("> ")

    if choice == "1":
        print("\nВы открываете сундук и находите магический артефакт!")
        print("Теперь вы чувствуете себя сильнее и готовым к любым испытаниям.")
        print("1 - Осмотреться ещё раз")
        print("2 - Вернуться в комнату")
        sub_choice = input("> ")
        if sub_choice == "1":
            secret_room()
        elif sub_choice == "2":
            start()
        else:
            print("Неверный ввод.\n")
            secret_room()
    elif choice == "2":
        start()
    else:
        print("Неверный ввод.\n")
        secret_room()

# Start game
if __name__ == "__main__":
    start()
