def letterCounter(letter,password):
    sum = 0
    for l in password:
        if letter == l:
            sum +=1
    return sum

def main():

    input_passwords = [x.replace('\n', '') for x in open('input.txt','r').readlines()]

    #1-4 m: mrfmmbjxr
    
    #PART1
    valid = 0
    for pw in input_passwords:
        password = pw.split(' ')
        minmax = [int(x) for x in password[0].split('-')]
        letter = password[1].replace(':', '')
        if letterCounter(letter,password[2]) >= minmax[0] and letterCounter(letter,password[2]) <= minmax[1]:
            valid +=1

    print(str(valid) + ' passwords')

    #PART2
    valid = 0
    for pw in input_passwords:
        password = pw.split(' ')
        places = [int(x)-1 for x in password[0].split('-')]
        letter = password[1].replace(':', '')
        print(password[2])
        print(password[2][places[0]:places[0]+1])
        if (letter == password[2][places[0]:places[0]+1] and letter != password[2][places[1]:places[1]+1]) or (letter != password[2][places[0]:places[0]+1] and letter == password[2][places[1]:places[1]+1]):
            valid +=1

    print(str(valid) + ' passwords')


if __name__ == '__main__':
    main()