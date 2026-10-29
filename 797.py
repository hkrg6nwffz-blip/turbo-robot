age = 17
age = int(input("Сколько тебе лет ?"))
protect = input("Дополнительная проверка, назови свое имя ?")
if protect == "Никита":
   print ("Вход разрешен")
else:
   print ("Вход запрещен")
if age < 16:
   print ("Запись недоступна")
elif age < 18:
   print ("Нужно согласие родителей")
else :   
   print ("Можно записаться")               