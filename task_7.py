flight_list = [
    {'id': 12, 'name': 'Bishkek-Moscow', 'price': 30000, 'time': '12:30'},
    {'id': 13, 'name': 'Bishkek-Tokyo', 'price': 60000, 'time': '12:30'},
    {'id': 14, 'name': 'Bishkek-Stambul', 'price': 55000, 'time': '12:30'},
    {'id': 15, 'name': 'Bishkek-Astana', 'price': 37000, 'time': '12:30'},
    {'id': 16,'name': 'Bishkek-Seoul', 'price': 40000, 'time': '12:30'}
]

for f in flight_list:
    print('-------------')
    print(f'Номер перелета: {f["id"]},\n')
    print(f'От куда-куда: {f["name"]},\n')
    print(f'Цена: {f["price"]},\n')
    print(f'Время вылета: {f["time"]},\n')
    print('-------------')

while True:
    try:
        f_number = int(input("Выберите номер перелета: "))
    except (ValueError, TypeError):
        print("Вы ввели неправильно значение!")
        print("Повторите...")
    else:
        break

fullname = input("Введите ФИО: ")

cost = int(input("Введите оплату за данный перелет: "))
dif=0
index_f=0-1

for i in flight_list:
    index_f=index_f+1
    if i['id']==f_number:
        break

dif=cost-flight_list[index_f]['price']


print(dif,cost)

if dif==0 or dif>0:
    print('-------------')
    print(fullname)
    print(f'Номер перелета: {flight_list[index_f]["id"]},\n')
    print(f'От куда-куда: {flight_list[index_f]["name"]},\n')
    print(f'Цена: {flight_list[index_f]["price"]},\n')
    print(f'Время вылета: {flight_list[index_f]["time"]},\n')
    print(f'ваша сдача:{dif}')
    print("Счастливого полета!!!")
    print('-------------')

else:
    print('у вас не хватает средств!!')