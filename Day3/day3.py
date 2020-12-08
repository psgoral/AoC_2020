def main():

    # input_map = [x.strip() for x in open('gracjan.txt','r').readlines()]
    # new_map = []
    # for line in input_map:
    #     new_map.append(str(line) * 100)

    #ONELINER
    new_map = [line*100 for line in [x.strip() for x in open('input.txt','r').readlines()]]


    # fd = open('mapa.txt','w+')
    
    # for line in new_map:
    #     fd.write(str(line) + '\n')

    #PART 1
    pos = [0,0]
    move = [1,3]
    counter = 0
    
    while pos[0] < len(new_map):
        if pos[0] != 0 and pos[1] != 0:
            if new_map[pos[0]][pos[1]] == '#':
                counter +=1
        pos[0] += move[0]
        pos[1] += move[1]
        
    print(str(counter) + ' trees')

    #PART 2
    slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]

    answers = []
    answer = 1
    for slope in slopes:
        jumps = 0
        pos = [0,0]
        pos[0] += slope[0]
        pos[1] += slope[1]
        counter = 0
        while pos[0] < len(new_map):
            if pos[0] != 0:
                if new_map[pos[0]][pos[1]] == '#':
                    counter +=1
            pos[0] += slope[0]
            pos[1] += slope[1]
            # print(pos)
            jumps += 1
        print(str(slope) + ':\t' + str(jumps) + ' jumps,\t' + str(counter) + ' trees')
        answers.append(counter)
        answer *= counter
    

    print(answer)
    print(answers)






            

        

    



    # for x in range(17):
    #     new_map.append('')
        
    # counter = 0
    # pointer = 0
    # for line in input_map:
    #     if counter %17 ==0:
    #         pointer +=1
    #     new_map[pointer] = new_map[pointer] + line
    
    # for line in new_map:
    #     print(line)



    # find_pattern(input_map)

    #PART1

   


    #PART2

   







if __name__ == '__main__':
    main()