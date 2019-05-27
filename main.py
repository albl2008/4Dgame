from check import checkGuess
from generateNumber import genNum
list=[0,1,2,3,4,5,6,7,8,9]
intentos = 0
number=[]

newNumber = genNum(list)
correct = newNumber.generatingNumber()

print (correct)

def play():
    global intentos
    intentos += 1
    while(True):
        try:
            numbers = input("Ingrese un numero de 4 cifras sin repetir ninguna de ellas")
            number=[]
            for i in range (len(numbers)):
                number.append(int(numbers[i]))
            if len(set(number))!=4:
                print("Ingrese sin repeticiones 4 cifras")
                play()
            else:
                checking = checkGuess(correct,number)
                answer = checking.verifyNumber()
                print("Bien:",answer[0],"Regular:",answer[1])
                if answer[0]!=4:
                    play()
                if answer[0]==4:
                    print("Ganaste despues de ",intentos," intentos")
        except ValueError:
            print("Ingrese numeros unicamente")

play()
    









