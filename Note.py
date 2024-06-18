notes = {}  # Будет являться словарем с заметками

def add_note ():
    title = input("Введите название заметки: ")
    content = input("Введите текст заметки: ")
    notes[title] = content
    print("Заметка была добавлена.")
def del_note ():
    if not notes:
        print("Такой заметки нет, попробуйте ещё раз.")
        return
    print("Список заметок: ")
    for title in notes:
        print(title)
    title_to_delete = input("Введите название заметки для удаления: ")
    if title_to_delete in notes:
        del notes[title_to_delete]
        print("Заметка удалена.")
    else:
        print("Заметки с таким названием нет.")
def show_note ():
    if not notes:
        print("Список заметок пуст. Сначала нужно добавить заметку.")
    else:
        print("Список заметок: ")
        for title, content in notes.items():
            print(f"{title}: {content}")


while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Удалить заметку")
    print("3. Вывести список заметок")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_note();
    elif choice == "2":
        del_note();
    elif choice == "3":
        show_note();
    elif choice == "4":
        print("Вы вышли из заметок.")
        break
    else:
        print("Вы ошиблись с вводом значения. Повторите попытку ещё раз.")
