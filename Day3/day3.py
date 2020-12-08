

def find_pattern(input_map):

    new_map = []

    first = input_map[0]

    print(len(first))
    n = 0
    for line in input_map:
        if line == first:
            print(n)
        n +=1





def main():

    input_map = [x.replace('\n', '') for x in open('input.txt','r').readlines()]


    find_pattern(input_map)

    #PART1

   


    #PART2

   







if __name__ == '__main__':
    main()