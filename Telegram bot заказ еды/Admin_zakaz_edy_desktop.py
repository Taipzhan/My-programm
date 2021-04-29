import telebot
import mysql.connector

bot = telebot.TeleBot('1796135688:AAEjViQtlMfnKo2-LGn05P8LtGEbI6EQIOc')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="2001_bitlab_group"
)


def Start(message):
    global menu
    text = ""
    text = text + "Выберите опцию поиска: \n"
    text = text + "1 - Поиск по типу еды\n"
    text = text + "2 - Поиск по ресторану\n"
    bot.send_message(message.chat.id, text)
    menu = "main"

def getAllFoodTypes():
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT * FROM food_types"
 mycursor.execute(sql)
 result = mycursor.fetchall()

 return result

def getAllRestaurants():
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT * FROM restaurants"
 mycursor.execute(sql)
 result = mycursor.fetchall()

 return result

def getFoodsByRestaurantId(id):
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT f.id, f.name, f.price, f.description, f.restaurant_id, f.foodtype_id, ft.name as foodType, r.name as restaurantName " \
       "FROM foods f " \
       "LEFT OUTER JOIN food_types ft ON f.foodtype_id = ft.id " \
       "LEFT OUTER JOIN restaurants r ON f.restaurant_id = r.id " \
       "WHERE f.restaurant_id = " + str(id)
 mycursor.execute(sql)
 result = mycursor.fetchall()

 return result

def getFoodByFoodType(id):
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT f.id, f.name, f.price, f.description, f.restaurant_id, f.foodtype_id, ft.name as foodType, r.name as restaurantName " \
       "FROM foods f " \
       "LEFT OUTER JOIN food_types ft ON f.foodtype_id = ft.id " \
       "LEFT OUTER JOIN restaurants r ON f.restaurant_id = r.id " \
       "WHERE f.foodtype_id = " + str(id)
 mycursor.execute(sql)
 result = mycursor.fetchall()
 return result

def getFood(id):
 global mydb
 mycursor = mydb.cursor()

 sql = "SELECT f.id, f.name, f.price, f.description, f.restaurant_id, f.foodtype_id, ft.name as foodType, r.name as restaurantName " \
 "FROM foods f " \
 "LEFT OUTER JOIN food_types ft ON ft.id = f.foodtype_id " \
 "LEFT OUTER JOIN restaurants r ON r.id = f.restaurant_id " \
 "WHERE f.id = "+str(id)

 mycursor.execute(sql)
 result = mycursor.fetchone()

 return result

def ByFood(id,ui):
    # Тут проверка покупал ли данный пользователь данную еду
    global mydb
    answ = str()
    counts = 0
    totals = 0
    mycursor = mydb.cursor()
    sql = "SELECT user_id,food_id FROM basket where user_id =%s and food_id = %s"
    val = (ui, id)
    mycursor.execute(sql, val)
    res = mycursor.fetchall()
    new = []
    for y in range(len(res)):
        for l in res[y]:
            new.append(l)

    if ui in new and int(id) in new:
        answ = 'YES'
    else:
        answ = 'NO'
    # Если пользователь покупал то добавляем его старое колл-во в копилку
    if answ == 'YES':
        sql = "SELECT count,total FROM basket where user_id =%s and food_id = %s"
        val = (ui, id)
        mycursor.execute(sql, val)
        res2 = mycursor.fetchall()
        new2 = []
        for y in range(len(res2)):
            for l in res2[y]:
                new2.append(l)
        totals = new2[1]
        counts = new2[0]
    # Теперь добавляем к старому новое колл-во
        sql = "SELECT count,total FROM basket where user_id =%s and food_id = %s"
        val = (ui, id)
        mycursor.execute(sql, val)
        res3 = mycursor.fetchall()
        new3 = []
        for y in range(len(res3)):
            for l in res3[y]:
                new3.append(l)
        totals += new3[1]
        counts += new3[0]
        # Тут обновляем уже сами ячейки
        sql = "UPDATE basket SET count = %s, total = %s WHERE user_id = %s and food_id= %s"
        val = (counts, totals, ui, id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " record updated.")
        return 'Корзина обновлена'
    # Тут добавление новой еды
    else:
        mycursor = mydb.cursor()
        foods = getFood(id)
        user_id = ui
        food_id = id
        count = 1
        total = foods[2]
        sql = "INSERT INTO basket (id,user_id,food_id,count,total) VALUES (NULL,%s,%s,%s,%s)"
        val = (user_id, food_id, count,total)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "")
        return 'Товар добавлен в корзину'

def GetBasket(id):
    global mydb
    mycursor = mydb.cursor()
    sql = "SELECT f.name,f.description,basket.count,basket.total,f.price" \
          " FROM basket LEFT JOIN foods f ON basket.food_id = f.id " \
          "WHERE basket.user_id ="+str(id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def Delbasket(id):
    global mydb
    mycursor = mydb.cursor()
    sql = "DELETE FROM basket WHERE basket.user_id ="+str(id)

    mycursor.execute(sql)
    mydb.commit()

menu = "main"

@bot.message_handler(content_types=["text"])
def handle_text(message):

 global menu

 if message.text.lower() == "/start":
   text=''
   text = text + "#########################\n"
   text = text + "Добро пожаловать в сервис заказа еды\n"
   text = text + "#########################\n"
   bot.send_message(message.chat.id, text)
   Start(message)

 else:
    if menu=="main":
        if message.text.lower() == "1":
            allFoodTypes = getAllFoodTypes()
            text = "#####################\n"
            for food in allFoodTypes:
                text = text+str(food[0]) + ") " + food[1] + "\n"
                menu = "choose_by_food_type"
            bot.send_message(message.chat.id, text)

        elif message.text.lower() == "2":
            allRestaurants = getAllRestaurants()
            text = "#####################\n"
            for rest in allRestaurants:
                text = text + str(rest[0]) + ") " + rest[1] + "\n"
                menu = "choose_by_restaurant"
            bot.send_message(message.chat.id, text)

    elif menu == "choose_by_food_type":
        menu = "buy_food"
        id = message.text.lower()
        foods = getFoodByFoodType(id)
        text = "#####################\nЕда\n"
        for food in foods:
            text = text + str(food[0]) + ") " + food[1] + " " + str(food[2]) + " KZT - " + food[7] + "\n"
        bot.send_message(message.chat.id, text)

    elif menu == "choose_by_restaurant":
        menu = "buy_food"
        id = message.text.lower()
        foods = getFoodsByRestaurantId(id)
        text = "#####################\nМеню\n"
        for food in foods:
            text = text+str(food[0])+ ") "+ food[1]+ " "+ str(food[2])+" KZT - "+ food[6] +"\n"
        bot.send_message(message.chat.id, text)

    elif menu == "buy_food":
        menu = "check"
        id = message.text.lower()
        ui = message.from_user.id
        foods = ByFood(id,ui)
        bot.send_message(message.chat.id, foods)
        text = '\nЖелаете купить еще что нибудь?\n1)Да \n2)Нет'
        bot.send_message(message.chat.id,text)

    elif menu == "check":
      if message.text.lower() =="1":
        Start(message)
      elif message.text.lower() =="2":
        ui = message.from_user.id
        food = GetBasket(ui)
        summ = 0
        text = "#############################\nВы заказали: \n"
        for i in food:
            text = text+ i[0]+" "+str(i[4]) + " KZT\n"
            text = text+"Колл-во:  "+str(i[2])
            text = text+"\nСостав: "+i[1] + "\n"
            summ+=i[3]
        text = text+"К оплате: " + str(summ)+"KZT"
        text = text+"\nСпасибо за покупку\n"
        bot.send_message(message.chat.id, text)
        Delbasket(ui)
bot.polling(none_stop=True, interval=0)
