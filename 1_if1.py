"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input("Введите возраст:"))
    if age<=1:
      print("Титьку соси")
    elif age <=7 :
      print("Десткий сад")
    elif age <= 18:
      print("Школа")
    elif age <=23:
      print("ВУЗ")
    else:
      print("Работай!!!")
    

if __name__ == "__main__":
    main()
