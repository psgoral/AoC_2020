




def main():

    numbers = [int(x) for x in open('input.txt','r').readlines()]



    #PART1
    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == 2020 and num1 != num2:
                print(str(num1) + ' * ' + str(num2) + ' = '+ str(int(num1) * int(num2)))

    #PART2

    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 + num3 == 2020 and (num1 != num2 != num3):
                    print(str(num1) + ' * ' + str(num2) + ' * ' + str(num3) + ' = '+ str(num1 * num2 * num3))




if __name__ == '__main__':
    main()