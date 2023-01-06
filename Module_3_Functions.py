def add_position(shopping_list):
    position = input('Введите название и количество')
    name, number = position.split()
    number = float(number)
    if name in shopping_list:
        shopping_list[name] += number
    else:
        shopping_list[name] = number
    return shopping_list

def remove_position(shopping_list):
    position = input('Введите название позиции, которую хотите удалить')
    shopping_list.pop(position, None)
    return shopping_list

def show_shopping_list(shopping_list):
    keys = sorted(shopping_list.keys())
    for key in keys:
        print(key, shopping_list[key])

#Сделать функцией print
def undefined(shopping_list):
    print ('Я вас не понял, введите одну из команд: [добавить, удалить, показать, выход]')

#Сделать функцией конструкцию с if
def action(x):
    if x == 'добавить':
        shopping_list = add_position(shopping_list)
    elif x == 'удалить':
        shopping_list = remove_position(shopping_list)
    elif x == 'показать':
        show_shopping_list(shopping_list)
    elif x == 'выход':
        exit
    else:
        undefined(shopping_list)

command = None
shopping_list = {}
while True:
    command = input('Введите команду')
    action(command)
