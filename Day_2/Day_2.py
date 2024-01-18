
import re
from string import ascii_letters
import math


if __name__ == "__main__":
    sum = 0
    totalpower = 0
    #game rules
    red = 12
    green = 13
    blue = 14
    colors = ['red', 'green', 'blue']
    with open(r'Day_2\input.txt', "r") as file:
        for line in file:
            mymap = {'red':0,'green':0,'blue':0}
            #first split the string into the different rounds
            split_str = re.split(":",line)
            game_id = int(split_str[0].lstrip(ascii_letters))
            regex = r'\d+|blue|green|red'
            x = re.findall(pattern = regex,string = split_str[1], flags = re.IGNORECASE)
            for i in range(1,len(x),2):
                if int(x[i-1]) > mymap[x[i]]:
                    mymap[x[i]] = int(x[i-1])
            print(game_id, mymap)
            if red >= mymap['red'] and blue >= mymap['blue'] and green >= mymap['green']:
                sum += game_id
            powerset = math.prod(mymap.values())
            totalpower += powerset
    print(sum)
    print(totalpower)

                


            
