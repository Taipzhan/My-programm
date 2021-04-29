import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="2001_bitlab_group"
)

def Addr():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    id = input('Введите id ресторана:')
    name = input('Введите название ресторана: ')
    address = input('Введите адрес: ')


    sql = "INSERT INTO restaurants (id, name,address) VALUES (%s,%s,%s)"
    val = (id,name,address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Ресторан добавлен.")
    print("================================================================")
def Dellr():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    id = input('Введите id ресторана:')
    sql = "DELETE FROM restaurants WHERE id = " + str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Ресторан удален.")
    print("================================================================")
def Updater():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    rid = input('Введите id ресторана:')
    name = input('Введите новое название ресторана: ')
    address = input('Введите новый адрес ресторана: ')

    sql = "UPDATE restaurants SET name = %s,address=%s WHERE id="+str(rid)
    val = (name,address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Ресторан обновлен.")
    print("================================================================")
def Vyvodr():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    sql = "SELECT id,name,address FROM restaurants"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print('id','  Ресторан','  Адрес')
    for i in result:
        print(i)
    print("================================================================")
def Addft():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    id = input('Введите id типа еды:')
    name = input('Введите название типа еды: ')
    print("================================================================")

    sql = "INSERT INTO food_types (id, name) VALUES (%s,%s)"
    val = (id,name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Тип еды добавлен.")
    print("================================================================")
def Dellft():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    id = input('Введите id типа еды:')
    sql = "DELETE FROM food_types WHERE id = " + str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Тип еды удален.")
    print("================================================================")
def Updateft():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    rid = input('Введите id типа еды:')
    name = input('Введите новое название типа еды: ')

    sql = "UPDATE food_types SET name = %s WHERE id="+str(rid)
    val = (name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Тип еды обновлен.")

def Vyvodft():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    sql = "SELECT id,name FROM food_types"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print('id','Тип еды')
    for i in result:
        print(i)
    print("================================================================")

def Addf():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    name = input('Введите название еды:')
    price = input('Введите цену еды:')
    description = input('Введите описание:')
    foodtype_id = input('Введите id типа еды:')
    restaurant_id = input('Введите id ресторана:')

    sql = "INSERT INTO foods (id, name, price, description, foodtype_id, restaurant_id) VALUES (NULL,%s,%s,%s,%s,%s)"
    val = (name,price,description, foodtype_id, restaurant_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Еда добавлена.")
    print("================================================================")
def Dellf():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    id = input('Введите id еды:')
    sql = "DELETE FROM foods WHERE id = " + str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Еда удалена.")
    print("================================================================")
def Updatef():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    id = input('Введите id еды:')
    name = input('Введите новое название еды:')
    price = int(input('Введите новую цену еды:'))
    description = input('Введите новое описание:')
    foodtype_id = int(input('Введите новый id типа еды:'))
    restaurant_id = int(input('Введите новый id ресторана:'))

    sql = "UPDATE foods SET name = %s,price = %s,description =%s,foodtype_id =%s,restaurant_id =%s WHERE id="+str(id)
    val = (name,price,description,foodtype_id,restaurant_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Еда обновлена.")
    print("================================================================")

def Vyvodf():
    global mydb
    mycursor = mydb.cursor()
    print("================================================================")
    sql = "SELECT id,name,price,description,foodtype_id,restaurant_id FROM foods"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print('id','Название',' Цена','Описание','id типа еды','id ресторана')
    for i in result:
        print(i)

while True:
    v=int(input(('Заказ еды, Администратор\n[1]Рестораны\n[2]Тип еды\n[3]Еда\n[4]Выйти\nВыберите цифру из списка для продолжения:')))
    if v == 1:
        print("================================================================")
        while True:
            print("================================================================")
            choice=int(input('Рестораны\n[1]Добавить\n[2]Удалить\n[3]Обновить\n[4]Вывести список ресторанов\n[5] Закончить\nВыберите цифру из списка для продолжения:'))
            if choice == 1:
                Addr()
            elif choice == 2:
                Dellr()
            elif choice == 3:
                Updater()
            elif choice == 4:
                Vyvodr()
            elif choice == 5:
                print("================================================================")
                break
    elif v == 2:
        print("================================================================")
        while True:
            print("================================================================")
            choice=int(input('Тип еды\n[1]Добавить\n[2]Удалить\n[3]Обновить\n[4]Вывести список типов еды\n[5]Закончить\nВыберите цифру из списка для продолжения:'))
            if choice == 1:
                Addft()
            elif choice == 2:
                Dellft()
            elif choice == 3:
                Updateft()
            elif choice == 4:
                Vyvodft()
            elif choice == 5:
                print("================================================================")
                break
    elif v == 3:
        print("================================================================")
        while True:
            print("================================================================")
            choice=int(input('Еда\n[1]Добавить\n[2]Удалить\n[3]Обновить\n[4]Вывести список еды\n[5] Закончить\nВыберите цифру из списка для продолжения:'))
            if choice == 1:
                Addf()
            elif choice == 2:
                Dellf()
            elif choice == 3:
                Updatef()
            elif choice == 4:
                Vyvodf()
            elif choice == 5:
                print("================================================================")
                break
    elif v==4:
        break