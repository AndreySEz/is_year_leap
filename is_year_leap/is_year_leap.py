def visokosny(year):
    if year % 400 == 0:
       return True;
    elif year % 100 == 0:
     return False;
    elif year % 4 == 0:
      return True;
    else:
     return False;

year = int(input("Введите год: "));
if (visokosny(year)):
    print("Год високосный")
else:
    print("Год не високосный")