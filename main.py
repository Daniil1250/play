# num1:int = 40
# num2:int = 20
# num3:int = 10

# num4:int = num1*num2*num3

# print(num4)

# num = 100
# CONST = 10

# s = num/CONST

# if s == 50:
#   print("OK")
# else:
#   print("NOT OK")


# def PrintSqure():
#   a = int(input("Введите значение стороны а прямоугольника: "))
#   b = int(input("Введите значение стороны b прямоугольника: "))
#   print("Площадь прямоугольника: ", a * b) # - Вывод двух аргументов
  
# PrintSqure()




# def PrintSqure() -> int:
#   a = int(input("Введите значение стороны а прямоугольника: "))
#   b = int(input("Введите значение стороны b прямоугольника: "))
#   rez = a * b
#   return rez
  



# def Calc(a:int, b:int) -> int:
#   rez = a * b
#   return rez
  
# print(Calc(10, 14))
  
  

# def Recursize():
#   def Greeting(st:str):
#     print(st)
#     if len(st) == 0:
#       return
#     else:
#       Greeting(st[:-1])
#   Greeting('Hello, word!')
  
  
# Recursize()
  



def Das() -> bool:
  playerChoise = input("Орел или решка ? ").strip().lower()
  return playerChoise == "орел"
  
  
def IsWin(coin:int, playerChoise:bool):
  if coin == playerChoise:
    print("Победа!")
  else:
    print("Поражение!")

def Main():
  import random
  coin = random.randint(0, 1)
  playerChoise = Das()
  IsWin(coin, playerChoise)
  
Main()
