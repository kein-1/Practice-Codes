
def Factorial(number):

    if (number <= 0):
        return 1
    return (number * Factorial(number-1))



def main():

    numb = int(input("Please input a number into number to calculate the factorial: "))
    print(type(numb))
    total = Factorial(numb)
    print("The sum of " + str(numb) + "!" + " is " + str(total) )

if __name__=="__main__":
    main()