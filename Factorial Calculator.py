def userinput_function() :
    userinput = eval(input('>> Please enter a number : '))
    return userinput
def find_factorial_function(userinput) :
    if userinput == 0 or userinput == 1:
        print('>> Factorial of',userinput,'= 1')
    elif type(userinput) != int :
        print('>> Useinput must be a positive integer.')
    elif userinput < 0 and type(userinput) == int :
        print('>> Userinput must be greater than -1.')
    else :
        factorial = userinput
        other = userinput - 1
        if userinput > 1 :
            while other >= 2 :
                factorial = factorial * other
                other = other - 1
        print('>> Factorial of',userinput,'= ',factorial)
def main_function() :
    find_factorial_function(userinput_function())
def continue_function() :
    done = True
    while done :
        userinput2 = input('>> Press C to Continue or Press E to Exit : ')
        if userinput2 == 'c' or userinput2 == 'C' :
            return True
        elif userinput2 == 'e' or userinput2 == 'E' :
            return False
        else :
            print('>> Invalid Input !, Enter again')
            done = True
done = True
print()
print('     ============ Factorial Calculator ============')
print()
while done :
    main_function()
    done = continue_function()
