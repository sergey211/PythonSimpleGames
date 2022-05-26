import random
diapazon=3
popytokvsego=7
popytok=popytokvsego
print('Привет! Как тебя зовут?')
name=input()
print('Что ж, '+name+', я загадываю число от 1 до '+str(diapazon))
number = random.randint(1, int(diapazon))
print('Попробуй угадать.')
print('У тебя '+str(popytok)+' попыток')
usernumb=input()
ugadano=False
while not ugadano and popytok>0: 
    try:
        popytka = int(usernumb)
        if popytka>diapazon or popytka<1:
            print('Эй! Нужно ввести число от 1 до '+str(diapazon)+', давай еще раз')
            usernumb=input()
        else:
            popytok=popytok-1;
            if popytka<number:
                print('твое число слишком малюпасенькое)')
            elif popytka>number:
                print('твое число слишком большущее)')
            elif popytka==number:
                if popytokvsego-popytok==1:
                    print('Ого!! '+name+'!! С ПЕРВОЙ ПОПЫТКИ??!! Ты что ли ЭКСТРАСЕНС??!!)))')
                    break
                print('Чотенька!! Малайчынка!! Тебе понадобилось '+str(popytokvsego-popytok)+' попыток')
                ugadano=True
                break
            if popytok>0:  
                print('можешь попробовать угадать еще '+str(popytok)+' раз')  
                usernumb=input()                 
    except ValueError:
        print("Эээ бляха, ты же не число вводишь, давай-ка еще разок")
        usernumb=input()
        
print('Я загадал '+str(number))
print('Пока!)')