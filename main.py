#Week 3: Homework
print('Month Converter')

userInput = int(input("Please enter a number between 1 - 12: "))

if not userInput < 1  and not userInput > 12:
    if userInput == 1:
        print('January')
    elif userInput == 2:
        print('February')
    elif userInput == 3:
        print('March')
    elif userInput == 4:
        print('April')
    elif userInput == 5:
        print('May')
    elif userInput == 6:
        print('June')
    elif userInput == 7:
        print('July')
    elif userInput == 8:
        print('August')
    elif userInput == 9:
        print('September')
    elif userInput == 10:
        print('October')
    elif userInput == 11:
        print('November')
    else:
        print('December')
else:
    print('That is not a valid option.')
